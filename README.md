# ha-dashboard-system-info

Eigenstaendiges Home-Assistant-Subprojekt fuer das Dashboard `System Info`.

## Inhalt
- `dashboard/system_info.yaml`
  - produktive YAML-Dashboard-Definition fuer `/config/dashboards/system_info.yaml`

## Deployment
Deployment erfolgt ueber das Superprojekt `ha-config`:

```bash
cd /Users/bjoern/dev/ha-dev/ha-config
./scripts/deploy_ha_raspi.sh --project ha-dashboard-system-info
```

## Hinweis zur Dashboard-Registrierung
Die Registrierung des Dashboards erfolgt aktuell in `/config/configuration.yaml` unter
`lovelace.dashboards.system-info` mit `filename: dashboards/system_info.yaml`.
