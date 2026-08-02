# ha-dashboard-system-info

Eigenstaendiges Home-Assistant-Subprojekt fuer das Dashboard `System`.

## Inhalt
- `dashboard/system_info.yaml`
  - produktive YAML-Dashboard-Definition fuer `/config/dashboards/system_info.yaml`
  - Consolidated **System** topic view (STG-4.102): three Sections-layout views —
    `System` (Raspberry Pi values/charts, releases, API status), `Zirkulation`
    (circulation pump control/status/logbook) and `Status` (printer, Tado
    heating, PV status). Replaces the former separate sidebar dashboards
    `circulation-pump` and `zs7-status` (both kept registered but hidden as
    `*_legacy.yaml` until owner acceptance).
- `dashboard/system_info_legacy.yaml`
  - pre-consolidation dashboard kept until owner acceptance (not registered)
- `packages/sensors_system_info.yaml`
  - command_line- und Template-Sensoren fuer CPU, Speicher, Disk und Uptime
- `packages/ha_dashboard_system_info.yaml`
  - YAML-Dashboard-Registrierung fuer `system-info`

## Cross-project coupling (read-only)

The consolidated dashboard renders entities owned by other projects (see
`deploy/runtime_dependencies.json`): circulation pump helpers
(`ha-circulation-pump`), printer/heating status packages (`ha-dashboard-zs7status`),
AlphaESS PV entities (`ha-pv-config` / `ha-alphaess-package`), energy analysis
sensors (`ha-dashboard-energy`) and the ApexCharts standard template
(`dashboard-templates`, consumed via `!include templates/apexcharts_standard.yaml`).

## Design-system exceptions (docs/design-system.md §5)

Documented deviations from the default card set in `dashboard/system_info.yaml`:

- **Markdown documentation blocks** (no UI elements): deploy overview table,
  API external-connections table, Tado warning log tail, PV capacity
  bandwidths, and the generated `releases_card.yaml` include (written by the
  release pipeline, intentionally not restructured).
- **Core `entities` cards** for dense diagnostic groups (attribute rows and
  fault registers): Druckerstatus, Trommeln/Komponenten, Batterie,
  Netz & Energie, Analyse/Prognose, Speicher-Kapazitaet, Generator/Strings,
  Systemstatus.
- **`history-graph` / `logbook`** for the pump Soll/Ist state history —
  binary/state histories cannot be rendered as ApexCharts line charts.

## Deployment
Deployment erfolgt ueber das Superprojekt `ha-config`:

```bash
cd /Users/bjoern/dev/ha-dev/ha-config
./scripts/deploy_ha_raspi.sh --project ha-dashboard-system-info-package --with-deps
```

Release-relevanter Deploy mit Contract-/Smoke-Verifikation:

```bash
./scripts/deploy_ha_raspi.sh --project ha-dashboard-system-info-package --with-deps --verify
```

Low-level Deploys bleiben moeglich:

```bash
./scripts/deploy_ha_raspi.sh --project ha-dashboard-system-info
./scripts/deploy_ha_raspi.sh --project ha-system-info-package
./scripts/deploy_ha_raspi.sh --project ha-dashboard-system-info-package
```

## Hinweis zur Dashboard-Registrierung
- Sollzustand ist die repo-owned Registrierung ueber `/config/packages/ha_dashboard_system_info.yaml`.
- Eine alte Registrierung in `/config/configuration.yaml` unter `lovelace.dashboards.system-info`
  kann als Altzustand noch vorhanden sein, ist aber nicht mehr der gewuenschte Betriebsweg.

## Project Contract
- Maschinenlesbarer Vertrag: `project.yaml`
- Contract-Check:

```bash
python3 ./scripts/check_ha_contracts.py --project ha-dashboard-system-info
```
