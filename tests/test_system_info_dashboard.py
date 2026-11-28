"""STG-4.114: the System dashboard views live in sibling files loaded via
view-level !include. HA resolves the include against the DEPLOYED loader
file, so every view file must ship next to it and carry its include deps."""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml
from dashboard_includes import view_include_paths

BASE_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = BASE_DIR.parent
DASHBOARD_YAML = BASE_DIR / "dashboard" / "system_info.yaml"

VIEW_FILES = (
    "system_info_system.yaml",
    "system_info_zirkulation.yaml",
    "system_info_status.yaml",
)
EXPECTED_VIEWS = (
    ("System", "system-info"),
    ("Zirkulation", "zirkulation"),
    ("Status", "status"),
)
LOADER_PROJECT = "ha-dashboard-system-info"


def _resolving_loader(base_dir: Path) -> type[yaml.SafeLoader]:
    """SafeLoader resolving view includes like HA; template includes stay markers."""

    class _Loader(yaml.SafeLoader):
        pass

    def _include(loader: yaml.SafeLoader, node: yaml.Node) -> object:
        rel = loader.construct_scalar(node)
        if rel.startswith("templates/") or rel == "releases_card.yaml":
            return {"__include__": rel}
        target = base_dir / rel
        return yaml.load(
            target.read_text(encoding="utf-8"),
            Loader=_resolving_loader(target.parent),
        )  # noqa: S506

    _Loader.add_constructor("!include", _include)
    return _Loader


class TestSystemInfoViewIncludes:
    def setup_method(self) -> None:
        manifest = json.loads((REPO_ROOT / "deploy" / "projects.json").read_text(encoding="utf-8"))
        self.projects = {project["id"]: project for project in manifest["projects"]}
        self.by_source = {project["source"]: project for project in manifest["projects"]}
        inventory = json.loads((REPO_ROOT / "deploy" / "inventory.json").read_text(encoding="utf-8"))
        self.inventory_pairs = {(item["repo_path"], item["server_path"]) for item in inventory["items"]}

    def test_loader_includes_exactly_the_extracted_views(self) -> None:
        assert [path.name for path in view_include_paths(DASHBOARD_YAML)] == list(VIEW_FILES)
        for name in VIEW_FILES:
            assert (DASHBOARD_YAML.parent / name).is_file(), f"view file {name} missing"

    def test_resolved_dashboard_keeps_all_views_and_stable_paths(self) -> None:
        resolved = yaml.load(
            DASHBOARD_YAML.read_text(encoding="utf-8"), Loader=_resolving_loader(DASHBOARD_YAML.parent)
        )  # noqa: S506
        assert [(view["title"], view["path"]) for view in resolved["views"]] == list(EXPECTED_VIEWS)

    def test_view_files_deploy_next_to_the_loader(self) -> None:
        loader = self.projects[LOADER_PROJECT]
        loader_dir = loader["target"].rsplit("/", 1)[0]
        for name in VIEW_FILES:
            source = f"ha-dashboard-system-info/dashboard/{name}"
            project = self.by_source.get(source)
            assert project is not None, f"{source} has no deploy project"
            assert project["ownership_mode"] == "paths_only"
            assert project["target"] == f"{loader_dir}/{name}"
            assert project.get("verify_reload") == "yaml_reload"
            assert project["id"] in loader["depends_on"], "loader must pull its view includes"
            assert (source, project["target"]) in self.inventory_pairs

    def test_view_file_includes_are_deploy_dependencies(self) -> None:
        templates_by_target = {
            project["target"].rsplit("/", 1)[1]: project["id"]
            for project in self.projects.values()
            if project["target"].startswith("/opt/homeassistant/config/dashboards/templates/")
        }
        for name in VIEW_FILES:
            path = DASHBOARD_YAML.parent / name
            project = self.by_source[f"ha-dashboard-system-info/dashboard/{name}"]
            includes = set(re.findall(r"!include\s+templates/(\S+)", path.read_text(encoding="utf-8")))
            for template in sorted(includes):
                assert template in templates_by_target
                assert templates_by_target[template] in project.get("depends_on", [])
        # The System view also includes the generated releases card.
        system_project = self.by_source["ha-dashboard-system-info/dashboard/system_info_system.yaml"]
        assert "releases_card.yaml" in (DASHBOARD_YAML.parent / "system_info_system.yaml").read_text(encoding="utf-8")
        assert "ha-dashboard-system-info-releases-card" in system_project.get("depends_on", [])

    def test_project_smoke_checks_cover_view_files(self) -> None:
        project = json.loads((BASE_DIR / "project.yaml").read_text(encoding="utf-8"))
        smoke_paths = {check.get("path") for check in project["smoke_checks"] if check["type"] == "remote_file_exists"}
        for name in VIEW_FILES:
            assert f"/opt/homeassistant/config/dashboards/{name}" in smoke_paths
