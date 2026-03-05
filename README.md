# ha-dashboard-system-info

Eigenstaendiges Home-Assistant-Subprojekt fuer das Dashboard `System Info`.

## Inhalt
- `dashboard/system_info.yaml`
  - produktive YAML-Dashboard-Definition fuer `/config/dashboards/system_info.yaml`
- `packages/sensors_system_info.yaml`
  - command_line- und Template-Sensoren fuer CPU, Speicher, Disk und Uptime
- `packages/ha_dashboard_system_info.yaml`
  - YAML-Dashboard-Registrierung fuer `system-info`

## Deployment
Deployment erfolgt ueber das Superprojekt `ha-config`:

```bash
cd /Users/bjoern/dev/ha-dev/ha-config
./scripts/deploy_ha_raspi.sh --project ha-dashboard-system-info-package --with-deps
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
