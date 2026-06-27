# AGENTS.md — ha-dashboard-system-info

## Scope

- Applies only to `ha-dashboard-system-info/` and all subdirectories beneath it.
- Complements the [root AGENTS.md](/AGENTS.md). The stricter rule wins.

## Ownership

- This project owns:
  - `dashboard/system_info.yaml`
  - `packages/sensors_system_info.yaml`
  - `packages/ha_dashboard_system_info.yaml`
- Old registrations in `/config/configuration.yaml` are legacy state only and must
  not be re-established as target state.

## Runtime Contract

- Functional deploy root: `ha-dashboard-system-info-package`.
- Stable dashboard key / file combination:
  - Key: `system-info`
  - Dashboard file: `/config/dashboards/system_info.yaml`
- Sensor entities must remain consistent with `project.yaml` and the runtime
  dependency register.

## Architecture Decisions

- No project-specific architecture decisions beyond root AGENTS.md.

## Deployment

- Activation workflow:
  1. `ha core check`
  2. YAML / config reload
  3. Only if sidebar activation is still missing: `ha core restart`
- The project now includes the `api_health` custom component
  (`custom_components/api_health/`). Changes to the component or to the
  `sensor: - platform: api_health` activation require an `ha core restart` to
  load the service and create `sensor.api_health_overall`. Dashboard and package
  YAML changes still only need a config reload after the component is loaded.

## Validation

- No project-specific validations — root checks apply.
