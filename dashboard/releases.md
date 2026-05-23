# Release v1.14.0

**Datum:** 2026-05-23  
**Items:** 3  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.12** — pv_forecast: Lokales Wetter-Archiv mit abgestufter Refresh-Strategie (`core_restart`)

## Bugfixes

- **STG-3.11** — pv_forecast: Offline-Fallback wenn Open-Meteo Archive API nicht erreichbar (`core_restart`)
- **STG-7.18** — Release-Deploy: Timeout/SSH-Fehler analysieren und Ablauf korrigieren (`none`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.13.0

**Datum:** 2026-05-23  
**Items:** 4  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.8** — Anwesenheitserkennung im Consumption Forecast per Dashboard-Toggle steuerbar (`yaml_reload, core_restart`)

## Bugfixes

- **STG-4.22** — Bugfix: pv_alphaess_battery_fill_level liefert unknown (`yaml_reload`)

## Bugfixes

- **STG-3.10** — pv_forecast: Modell-Training liefert keine Daten — Diagnose und Logging verbessern (`core_restart`)
- **STG-3.9** — pv_forecast: NameError 'np' in Exception-Handler bei Model-Training-Fehler (`core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.12.1

**Datum:** 2026-05-22  
**Items:** 1  
**Gesamt-Deployment:** yaml_reload

## Bugfixes

- **STG-4.21** — Bugfix: Markdown-Tabellen-Rendering in PV Forecast V2 (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.12.0

**Datum:** 2026-05-21  
**Items:** 4  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-4.19** — PV-Forecast: Mahalanobis Feature Weights im Modell-Status anzeigen (`core_restart`)

## Bugfixes

- **STG-7.17** — Release Pipeline: Deploy-Automatisierung und Drift-Handling stabilisieren (`none`)

## Bugfixes

- **STG-2.128** — SOC-Verlauf: IST-Kurve zeigt Anstieg vor dem realen Ereignis (15-Min-Bucket-Floor) (`core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.11.0

**Datum:** 2026-05-21  
**Items:** 7  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-4.17** — Energy-Dashboard: Erwarteter Morgen-Crossover in alphaess_integration berechnen (`core_restart`)
- **STG-6.13** — Konsolidiere Regel-Hierarchie: rules.md als Master, AGENTS.md als Spezialisierung (`none`)

## Bugfixes

- **STG-10.7** — DWD-Wetterdashboard: Bugfixes für Hero-Bereich und Stunden-Timeline (`yaml_reload`)
- **STG-2.86** — Zirkulationspumpe: Hardcoded Switch-Trigger auf dynamische Auswahl umstellen (`none`)

## Bugfixes

- **STG-2.50** — SOC-Regelung: Ursachen fuer fehlende Sensorwerte und robuste Degradationslogik ermitteln (`none`)
- **STG-4.16** — Energy-Dashboard: Crossover-Sensoren referenzieren falsche Quell-Entität (`yaml_reload`)
- **STG-8.2** — Zirkulationspumpe: SwitchBot IndexError bei turn_on abfangen (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.10.0

**Datum:** 2026-05-17  
**Items:** 1  
**Gesamt-Deployment:** none

## Neue Features

- **STG-2.126** — Min-SOC Sensor: Modbus als Primärquelle, Cloud als Fallback (`none`)


---

# Release v1.9.0

**Datum:** 2026-05-17  
**Items:** 1  
**Gesamt-Deployment:** none

## Neue Features

- **STG-10.3** — DWD-Wetterdashboard: Heute im Verlauf (Stunden-Timeline + Diagramme) (`none`)


---

# Release v1.8.0

**Datum:** 2026-05-17  
**Items:** 3  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-10.1** — DWD-Wetterdashboard: Projektstruktur und Entitäten-Setup (`deploy_project: ha-dashboard-dwd-package`)
- **STG-10.2** — DWD-Wetterdashboard: Hero-Bereich Jetzt & heute + Regen-Nowcast-Text (`none`)

## Bugfixes

- **STG-2.125** — STG-2.123 nachziehen: SOC Plan Curve Startup-Warnings auf Server deployen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`
1. `deploy_project: ha-dashboard-dwd-package`


---

# Release v1.7.0

**Datum:** 2026-05-17  
**Items:** 7  
**Gesamt-Deployment:** none

## Neue Features

- **STG-2.41** — Erreichbarkeitsprüfung P1→P2 im Fenster T1→T2 mit P90/P10-Betrachtung (`Deploy ha-pv-config package to HA`)
- **STG-6.9** — Backlog-Konflikte: UUID-basierte Auflösung bei konkurrierenden Änderungen (`none`)

## Bugfixes

- **STG-7.13** — Release-Pipeline: Atomarität und Submodule-Push-Resilienz (`none`)
- **STG-7.14** — Deploy-State-Drift: Reconciliation und Force-Override (`none`)
- **STG-7.15** — Backlog-Status: 'completed' vs 'done' normalisieren (`none`)
- **STG-7.16** — Release-Dashboard wird nicht aktualisiert — Dashboard-Release-Projekte bleiben zurück (`none`)

## Technisch

- **STG-2.39** — Tomorrow Reserve: Explizite morgige Recovery-Zeit statt heutiger Proxy (`Deploy ha-pv-config package to HA`)

## Erforderliche Schritte

1. `Deploy ha-pv-config package to HA`


---

# Release v1.6.0

**Datum:** 2026-05-17  
**Items:** 7  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.46** — Batterie-Steuerung: Dashboard-Beschreibungen klarer und verstaendlicher ueberarbeiten (`core_restart`)
- **STG-5.5** — Dashboard-YAML-Regression-Tests für ha-dashboard-energy einführen (`none`)

## Bugfixes

- **STG-2.123** — SOC Plan Curve: Startup-Warnings auf Debug-Level herunterstufen (`core_restart`)

## Bugfixes

- **STG-2.122** — Capacitaetsschaetzung: Update dauert >10s — DB-Query-Optimierung oder Caching (`core_restart`)
- **STG-7.12** — Release-Pipeline: Dashboard-Release-Projekte unabhaengig vom HA-Deploy-Status deployen (`none`)

## Technisch

- **STG-2.121** — AGENTS.md Konsistenz: Verbleibende 5 Subprojekte auf Template-Struktur bringen (`none`)
- **STG-2.24** — AGENTS.md Konsistenz: Template einführen und Subprojekte inkrementell aufräumen (`none`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.5.0

**Datum:** 2026-05-16  
**Items:** 4  
**Gesamt-Deployment:** none

## Neue Features

- **STG-7.8** — Deployment nur durch Release-Manager zulassen (`none`)

## Bugfixes

- **STG-2.120** — _check_enforced_dependencies wirft bei --all fälschlich Fehler (`none`)
- **STG-7.11** — Release-Pipeline: Submodule-Commit und -Push automatisieren (`none`)

## Technisch

- **STG-2.45** — T1-Dynamik verfeinern: Ladeleistungsmodell ueber Vorlauf-Fenster statt nur Best-Hour-Slot (`none`)


---

# Release v1.4.1

**Datum:** 2026-05-16  
**Items:** 2  
**Gesamt-Deployment:** none

## Bugfixes

- **STG-7.10** — released_items.json aus Submodule in Superproject verschieben (`none`)


---

# Release v1.4.0

**Datum:** 2026-05-16  
**Items:** 3  
**Gesamt-Deployment:** none

## Neue Features

- **STG-7.9** — Release-Workflow: Dashboard und Release-Notes müssen immer mitdeployed werden (`none`)

## Technisch

- **STG-2.20** — Deploy-Refactoring Phase C: Manifest-Engine in deploy_manifest.py extrahieren (`none`)
- **STG-2.21** — Deploy-Refactoring Phase D: Transaction-Core in deploy_core.py extrahieren (`none`)


---

# Release v1.3.1

**Datum:** 2026-05-16  
**Items:** 1  
**Gesamt-Deployment:** none

## Bugfixes

- **STG-2.118** — Orange Linie: Steiler Initialabfall auf 80% im Dashboard untersuchen (`none`)


---

# Release v1.3.0

**Datum:** 2026-05-16  
**Items:** 4  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-7.7** — Release Notes als statische HTML-Seiten in www/releases/ (`core_restart`)

## Bugfixes

- **STG-7.7a** — Release Pipeline für STG-7.7 nachholen + Link fixen (`yaml_reload`)

## Technisch

- **STG-2.18** — Deploy-Refactoring Phase A: RemoteExecutor-Interface einführen (`none`)
- **STG-2.19** — Deploy-Refactoring Phase B: Verify und HA-Restart in deploy_verify.py extrahieren (`none`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.2.1

**Datum:** 2026-05-16  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-7.1f** — Bugfix: releases.md Link führt auf Startseite (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.2.0

**Datum:** 2026-05-16  
**Items:** 4  
**Gesamt-Deployment:** yaml_reload

## Neue Features

- **STG-7.6** — Release Notes: Übersicht statt Wall-of-Text (`yaml_reload`)

## Bugfixes

- **STG-2.91** — SOC-Plan-Kurve: Forecast-Daten für nächsten Tag bei Über-Mitternacht-Forward (`none`)
- **STG-7.2** — Release Pipeline: YAML-Escaping in releases_card.yaml robuster machen (`none`)
- **STG-7.3** — Release Pipeline: !include Verhalten fuer einzelne Cards in HA validieren (`none`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.1.0

**Datum:** 2026-05-16  
**Items:** 9  
**Gesamt-Deployment:** yaml_reload

## Neue Features

- **STG-5.4** — pytest-cov einführen und Coverage-Schwellen definieren (`none`)
- **STG-7.1d** — Release Pipeline Erstaktivierung: Test-Release v1.0.0 und Doku (`none`)
- **STG-7.4** — Release Pipeline: Automatisches Deployment auf HA-Server beim Release (`none`)
- **STG-7.6** — Release Notes: Übersicht statt Wall-of-Text (`yaml_reload`)

## Bugfixes

- **STG-2.117** — PV-Forecast Bootstrap-CSV aktualisieren — Lücken zwischen altem CSV und heute schließen (`none`)
- **STG-2.91** — SOC-Plan-Kurve: Forecast-Daten für nächsten Tag bei Über-Mitternacht-Forward (`none`)
- **STG-7.1e** — Bugfix: duplicate command_line blocks in sensors_system_info.yaml (`yaml_reload`)
- **STG-7.2** — Release Pipeline: YAML-Escaping in releases_card.yaml robuster machen (`none`)
- **STG-7.3** — Release Pipeline: !include Verhalten fuer einzelne Cards in HA validieren (`none`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.1.0

**Datum:** 2026-05-16  
**Items:** 3  
**Gesamt-Deployment:** none

## Neue Features

- **STG-5.4** — pytest-cov einführen und Coverage-Schwellen definieren (`none`)
- **STG-7.1d** — Release Pipeline Erstaktivierung: Test-Release v1.0.0 und Doku (`none`)
- **STG-7.4** — Release Pipeline: Automatisches Deployment auf HA-Server beim Release (`none`)


---

# Release v1.0.1

**Datum:** 2026-05-16  
**Items:** 2  
**Gesamt-Deployment:** yaml_reload

## Bugfixes

- **STG-2.117** — PV-Forecast Bootstrap-CSV aktualisieren — Lücken zwischen altem CSV und heute schließen (`none`)
- **STG-7.1e** — Bugfix: duplicate command_line blocks in sensors_system_info.yaml (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`

---

# Release v1.0.0

**Datum:** 2026-05-16  
**Items:** 115  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.100** — System Info Dashboard: View 'HA Config Projekt Overview' anlegen (`yaml_reload`)
- **STG-2.101** — Projekt Overview: echte Versionsnummern und lesbare Zeitstempel (`yaml_reload`)
- **STG-2.109** — Sensor-Fallback und Outlier-Filter im Session-Log sichtbar machen (`core_restart`)
- **STG-2.116** — PV-History-Cache: Eigene SQLite-DB mit stündlichen Daten, 366-Tage-Training, kein Purge (`core_restart`)
- **STG-2.32** — T1 dynamisch an aktuelles SOC und Ladegeschwindigkeit koppeln (`core_restart`)
- **STG-2.35** — Periodische Verifikation im Skip-Apply-Pfad bei stabilem Self-Use (`core_restart`)
- **STG-2.48** — PV-Forecast Dashboard V2: Delta IST/Latest vs. BoD Diagramm erweitern (`yaml_reload`)
- **STG-2.51** — SOC-Regelung: Degradationslogik fuer Sensor-Missing statt Hard-Reset (`core_restart`)
- **STG-2.52** — SOC-Regelung: Telemetry-Erweiterung fuer Sensor-Missing-Analyse (`core_restart`)
- **STG-2.62** — Phasen-Hysterese: Rückschritte nach Erreichen einer höheren Phase verhindern (`core_restart`)
- **STG-2.63** — Dashboard-Fixierung: Abgeschlossene Phasen-Werte einfrieren (`core_restart`)
- **STG-2.67** — SQLite-Optimierung Teil 1: Query-LIMIT und Connection-Reuse (`core_restart`)
- **STG-2.68** — SQLite-Optimierung Teil 2: Executor-Timeout für Evaluation-Sensoren (`core_restart`)
- **STG-2.70** — house_consumption_forecast: k-NN Performance-Optimierung bei gleicher Forecast-Qualitaet (`core_restart`)
- **STG-2.71** — house_consumption_forecast: SCAN_INTERVAL auf 30 Minuten erhoehen (`core_restart`)
- **STG-2.73** — house_consumption_forecast: Vorhersage cachen input-basiert (`core_restart`)
- **STG-2.88** — Zirkulationspumpe: Stuck-/Recovery-Erkennung für beliebige Plugs designen (`yaml_reload`)
- **STG-2.89** — Batterie-Steuerung: Leistungskommando-Dispatch-Chart aus Dashboard entfernen (`yaml_reload`)
- **STG-2.90** — Batterie-Steuerung: Soll-SOC-Plan-Kurve (grün, 6h Forward) im Dashboard (`core_restart`)
- **STG-2.93** — Charge-Control Warm-Start Teil 1: Snapshot erweitern und sofort bei Live persistieren (`core_restart`)
- **STG-2.94** — Charge-Control Warm-Start Teil 2: Runtime-Sensor sofortige Initialisierung (`core_restart`)
- **STG-2.95** — Charge-Control Warm-Start Teil 3: Konsistenzmarker und Tests (`core_restart`)
- **STG-2.98** — Deploy-Metadaten: Pro-Projekt JSON mit Version, Zeit und Branch persistieren (`none`)
- **STG-2.99** — HA-Sensoren: Projekt-Deploy-Metadaten aus Server-JSON lesen (`yaml_reload`)
- **STG-4.12** — PV-Forecast V2 Dashboard: Tages-Verlaufsdiagramme in View 'Tabelle' – Temperatur entfernen, Forecast/Band als Spline-Kurven (`yaml_reload`)
- **STG-4.14** — Dashboard Session-Log visuell aufwerten (Farben, Struktur, Limit-Anzeige) (`yaml_reload`)
- **STG-4.4** — Zirkulationspumpe: Anwesenheitssteuerung auf Zeitfenster umstellen, Steuerung nur manuell (`yaml_reload`)
- **STG-4.5a** — PV-Forecast Confidence: Python-Code für kontinuierlichen Drift-Score und Band-Relativierung vorbereiten (`core_restart`)
- **STG-4.5b** — PV-Forecast Confidence: Template-Sensor Formel überarbeiten – relative Band-Penalty + kontinuierlicher Drift (`yaml_reload`)
- **STG-4.6a** — PV-Forecast V2 Dashboard: Default-Seite auf 'Heute' setzen (`yaml_reload`)
- **STG-4.6b** — PV-Forecast V2 Dashboard: Diagramme zwischen Modell- und Historie-Tab verschieben (`yaml_reload`)
- **STG-4.7** — PV-Forecast V2 Dashboard: Overview-Seite aus V1 als neue Seite übernehmen (`yaml_reload`)
- **STG-4.8** — PV-Forecast V2 Dashboard: Zeitraum-Historien-Diagramme in View Modell von 10 auf 14 Tage erweitern (`core_restart`)
- **STG-5.2** — Testabdeckung über alle Projekte analysieren und Handlungsempfehlung erarbeiten (`none`)
- **STG-5.3** — Smoke-Tests für testlose Subprojekte: alexa-automation, circulation-pump, dashboard-system-info, dashboard-zs7status (`yaml_reload`)
- **STG-6.11** — runtime_decision.py: Null-Handling konsistent machen und Snapshot-Fallback robuster gestalten (`core_restart`)
- **STG-6.12** — Backlog-Epic-Struktur analysieren und sauber regeln (oder ersetzen) (`none`)
- **STG-6.7** — Dashboard-Logging überarbeiten — verständliche Ereignisanzeige statt Fachbegriffe (`core_restart`)
- **STG-6.8** — AGENTS.md vereinheitlichen: allgemeine Regeln zentralisieren, nur projektspezifische Infos lokal belassen (`none`)
- **STG-7.1b** — Release Pipeline Skript: scripts/release_pipeline.py erstellen (`none`)
- **STG-7.1c** — Release Pipeline Dashboard: Releases-Seite in System-Info-Dashboard (`yaml_reload`)

## Bugfixes

- **STG-2.110** — SOC-Plan-Kurve: Maximalwert auf 100% begrenzen statt Ziel-SOC 105% (`core_restart`)
- **STG-2.111** — pv_forecast entity.py: native_value und available mit isinstance-Prüfungen härten (`core_restart`)
- **STG-2.112** — house_consumption_forecast: Past-only intervals sollten Forecast-Quantile auf None setzen (`core_restart`)
- **STG-2.115** — Recorder-Purge auf 30 Tage erhöhen — Dashboard-Charts fixen (`none`)
- **STG-2.22** — Zirkulationspumpe: Guard-Klausel für switch.turn_on/turn_off gegen Switchbot-BLE-Race-Condition (`yaml_reload`)
- **STG-2.23** — PV-Forecast v2: Template-Sensoren mit unit_of_measurement dürfen nicht den String 'unavailable' zurückgeben (`yaml_reload`)
- **STG-2.25** — Zirkulationspumpe: Guard-Klausel vervollständigen und konsistent machen (Follow-up zu STG-2.22) (`yaml_reload`)
- **STG-2.26** — PV-Forecast V2 Template-Sensoren: Fehlerbehandlung vereinheitlichen und Edge Cases härten (`yaml_reload`)
- **STG-2.30** — ForecastScheduler: CancelledError-Handling in teardown(), Typ-Hints für Tasks, WeakRef-Callbacks (`core_restart`)
- **STG-2.54** — Zirkulationspumpe: Durchspülungstimer bleibt nach Abwesenheit im Zustand idle (`yaml_reload`)
- **STG-2.87** — Zirkulationspumpe: Track Last Run End und Flush Timer Reset auf dynamischen Switch umstellen (`yaml_reload`)
- **STG-2.92** — Bugfix: SOC Plan Curve Sensor schreibt nie einen Zustand (`core_restart`)
- **STG-4.9** — PV-Forecast V2 Dashboard: Delta IST vs BoD – letzter Punkt soll letzte abgeschlossene Stunde sein (`yaml_reload`)

## Technisch

- **STG-1.1** — Shared Component Library: open_meteo_client.py und Recorder-Attribute-Helpers deduplizieren (`core_restart`)
- **STG-1.2** — Hartcodierte Defaults aus sensor.py in const.py pro Component auslagern (`core_restart`)
- **STG-2.1** — sensor.py God Objects entflechten – Coordinator / Entities / Utilities trennen (`core_restart`)
- **STG-2.10** — Coordinator entflechten (3/3): MeteoAdapter für Open-Meteo-API-Calls extrahieren (`core_restart`)
- **STG-2.103** — sensor.py Phase 1: State-Helper und DB-Queries extrahieren (`core_restart`)
- **STG-2.104** — sensor.py Phase 2: Sunrise/Sunset, Renderers und Forecast-Source extrahieren (`core_restart`)
- **STG-2.105** — sensor.py Phase 3: Phase3-Strategy und Solar-History extrahieren (`core_restart`)
- **STG-2.106** — sensor.py Phase 4: Control-Targets und Runtime-Decision extrahieren (`core_restart`)
- **STG-2.107** — sensor.py Phase 5: Konkrete Sensor-Klassen extrahieren (`core_restart`)
- **STG-2.108** — MeteoAdapter: Retry-Backoff mit konfigurierbarem Maximum absichern (`core_restart`)
- **STG-2.113** — entity.py Return-Typen: extra_state_attributes auf dict[str, Any] | None alignieren (`none`)
- **STG-2.13** — entity.py Code-Robustheit – explizite Returns und Typprüfungen vereinheitlichen (`core_restart`)
- **STG-2.14** — entity.py Divergenz-Dokumentation – state_class und projektspezifische Keys (`core_restart`)
- **STG-2.2** — except Exception: durch spezifische Exceptions ersetzen (25+ Vorkommen) (`core_restart`)
- **STG-2.27** — ForecastScheduler Basisklasse: Initial-Refresh-Scheduling (async_call_later, HA-Start-Listener) extrahieren (`core_restart`)
- **STG-2.28** — PV-Forecast: Intraday-Minute-Tick, Entity-Lifecycle und Teardown in ForecastScheduler integrieren (`core_restart`)
- **STG-2.31** — pv_forecast entity.py – _prune_attributes_for_recorder O(n²) beheben (`core_restart`)
- **STG-2.33** — GenCounter: Abflachende Hysterese statt Hard-Reset bei Last ≥ Generation (`core_restart`)
- **STG-2.34** — P1-Berechnung: Fenster-bezogen statt globaler Tagesvergleich (`core_restart`)
- **STG-2.36** — T2-Berechnung mit nichtlinearer SOC-Kurve korrigieren (`core_restart`)
- **STG-2.4** — Ungenutzte Imports in coordinator.py, entity.py und sensor.py bereinigen (`core_restart`)
- **STG-2.40** — Phase-1-Entlade-Logik bedingt auf T1-Nähe einschränken (`core_restart`)
- **STG-2.42** — house_consumption_forecast entity.py – _prune_attributes_for_recorder O(n²) beheben (`core_restart`)
- **STG-2.43** — pv_forecast entity.py – PvForecastIntervalSensor Caching einführen (`core_restart`)
- **STG-2.44** — house_consumption_forecast entity.py – IntervalSensor Cache-Granularität auf Minute fixen (`core_restart`)
- **STG-2.59** — Solar-Forecast-History: DB-Query-Last reduzieren (`core_restart`)
- **STG-2.6** — Gemeinsame Patterns in pv_forecast/entity.py und house_consumption_forecast/entity.py analysieren und deduplizieren (`core_restart`)
- **STG-2.60** — Usable-Capacity-Estimate: DB-Query-Last reduzieren (`core_restart`)
- **STG-2.61** — Night-History (Control-Target-Source): DB-Query-Last reduzieren (`core_restart`)
- **STG-2.7** — entity.py Review-Follow-up: ValueError-Handling, Template-Exceptions, Performance und Divergenzen (`core_restart`)
- **STG-2.8** — Coordinator entflechten (1/3): StateRepository für Persistenz und Storage extrahieren (`core_restart`)
- **STG-2.85** — T2-Berechnung: 15-Minuten-Slot-Ansatz durch direkte Cross-Over-Funktion ersetzen (`core_restart`)
- **STG-3.1** — Domain-Logik (model.py, history.py, interval.py, backtest.py) von homeassistant-Imports entkoppeln (`core_restart`)
- **STG-4.10** — PV-Forecast V2 Dashboard: Delta IST vs BoD – Code-Review-Follow-up (Duplikation, Client-Zeit, Invalid-Date) (`yaml_reload`)
- **STG-4.11** — PV-Forecast V2 Dashboard: Neue View 'Tabelle' – Code-Review-Follow-up (Duplikation, sum-Filter, Layout-Konsistenz) (`yaml_reload`)
- **STG-6.1** — Backlog-System auf UUID-basierte interne Referenzen umstellen (`none`)
- **STG-6.2** — Backlog-Datenmodell: uuid Feld optional in Template und Parser einführen (`none`)
- **STG-6.3** — Migrationsskript: Allen bestehenden Backlog-Items UUIDs vergeben (`none`)
- **STG-6.4** — Backlog-Validierung: UUID-Einzigartigkeit und Konsistenz prüfen (`none`)
- **STG-6.5** — Backlog-Referenzen: depends_on und superseded_by auf UUID umstellen (`none`)
- **STG-6.6** — Backlog-Dokumentation und Tooling-Abschluss für UUID-Referenzen (`none`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`
