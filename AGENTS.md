# AGENTS.md - ha-dashboard-system-info

## Scope
- Gilt nur fuer `ha-dashboard-system-info/`.
- Ergaenzt das Top-Level-[AGENTS.md](/Users/bjoern/dev/ha-dev/ha-config/AGENTS.md).

## Ownership
- Dieses Projekt besitzt:
  - `dashboard/system_info.yaml`
  - `packages/sensors_system_info.yaml`
  - `packages/ha_dashboard_system_info.yaml`
- Alte Registrierungen in `/config/configuration.yaml` gelten nur als Altzustand und duerfen nicht wieder zum Sollzustand werden.

## Runtime Contract
- Funktionaler Deploy-Root ist `ha-dashboard-system-info-package`.
- Stabile Dashboard-Key-/Datei-Kombination:
  - Key `system-info`
  - Dashboard-Datei `/config/dashboards/system_info.yaml`
- Sensor-Entities muessen mit `project.yaml` und dem Runtime-Dependency-Register konsistent bleiben.

## Activation
- Aktivierungsworkflow:
  1. `ha core check`
  2. YAML/Config-Reload
  3. nur bei weiter fehlender Sidebar-Aktivierung `ha core restart`

## Validation
- Vor release-relevanten Aenderungen:
  - `python3 ./scripts/check_ha_contracts.py --project ha-dashboard-system-info`
  - `./scripts/deploy_ha_raspi.sh --project ha-dashboard-system-info-package --with-deps --dry-run`
