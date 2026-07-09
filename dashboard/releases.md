# Release v1.57.10

**Datum:** 2026-07-09  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.196** — Dynamischer MIN-SOC: Nachtprotokoll-Zukunftszeilen auch bei fehlendem evening_crossover filtern (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.57.9

**Datum:** 2026-07-09  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.195** — Dynamischer MIN-SOC: Alte Zukunftszeilen aus Nachtprotokoll-Store bereinigen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.57.8

**Datum:** 2026-07-09  
**Items:** 1  
**Gesamt-Deployment:** yaml_reload

## Bugfixes

- **STG-7.23** — Release-Pipeline: Dashboard-Release-Deploys triggern mehrfache Restarts (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.57.7

**Datum:** 2026-07-09  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.194** — Dynamischer MIN-SOC: Nachtprotokoll pro Stunde korrekt persistieren (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.57.6

**Datum:** 2026-07-09  
**Items:** 1  
**Gesamt-Deployment:** yaml_reload

## Bugfixes

- **STG-7.22** — AlphaESS Deploy-Verify ignoriert __pycache__ (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.57.5

**Datum:** 2026-07-09  
**Items:** 1  
**Gesamt-Deployment:** yaml_reload

## Bugfixes

- **STG-7.21** — Deployment-Prozess: unnötige HA-Core-Restarts vermeiden (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.57.4

**Datum:** 2026-07-09  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.193** — Dynamischer MIN-SOC: letzte Nacht tagsüber im Nachtprotokoll anzeigen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.57.3

**Datum:** 2026-07-08  
**Items:** 1  
**Gesamt-Deployment:** yaml_reload

## Bugfixes

- **STG-2.192** — Fix PV Dynamic MIN-SOC Write automation max validation error (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.57.2

**Datum:** 2026-07-08  
**Items:** 2  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.190** — Fix dynamic MIN-SOC night-log persistence (Store.async_save) (`core_restart`)
- **STG-2.191** — Fix PV Dynamic MIN-SOC Write automation overlap (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.57.1

**Datum:** 2026-07-08  
**Items:** 2  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.189** — SOC Plan Curve Plot bleibt leer: robuste Fehlerbehandlung und Logging (`core_restart`)
- **STG-3.86** — House Consumption Forecast rolling_24h: state_class auf None setzen und ausrollen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.57.0

**Datum:** 2026-07-08  
**Items:** 3  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.185** — Dynamisches MIN-SOC Nachtprotokoll: abgelaufene Nacht weiter sichtbar halten (`core_restart`)
- **STG-2.186** — Dynamische MIN-SOC Steuerung bis Morgen-Crossover statt Sonnenaufgang (`core_restart`)

## Bugfixes

- **STG-2.187** — Dynamischer MIN-SOC Zielwert darf Ist-SOC nie überschreiten (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.56.0

**Datum:** 2026-07-07  
**Items:** 2  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.182** — Dynamisches MIN-SOC Nachtprotokoll: Werte pro Zeile zum Zeitpunkt der Uhrzeit persistieren (`core_restart`)

## Bugfixes

- **STG-3.85** — House Consumption Forecast Rolling-24h Sensor: state class 'measurement' mit device class 'energy' ist ungültig (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.55.0

**Datum:** 2026-07-07  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.83** — House Consumption Forecast: Latest Forecast immer 24h in die Zukunft nachfuehren (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.54.0

**Datum:** 2026-07-07  
**Items:** 2  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.73** — PV-Forecast: Batched k-NN Prediction für alle Forecast-Stunden (`core_restart`)

## Bugfixes

- **STG-3.72** — PV Forecast: Windgeschwindigkeits-Parameter auf offiziellen Open-Meteo Namen pruefen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.53.0

**Datum:** 2026-07-07  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.181** — Dynamische MIN-SOC Nacht-Protokoll-Tabelle für Nachvollziehbarkeit (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.52.0

**Datum:** 2026-07-07  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.181** — Dynamische MIN-SOC Nacht-Protokoll-Tabelle für Nachvollziehbarkeit (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.52.1

**Datum:** 2026-07-05  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.180** — Regression-Fix: dynamic_min_soc_sensor Event-Listener ignoriert Attribut-only-Updates (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.52.0

**Datum:** 2026-07-05  
**Items:** 3  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-4.34** — Consumption Forecast Intraday-Chart auf 24h Vergangenheit/Zukunft und PV-Forecast-Farbschema anpassen (`yaml_reload`)

## Bugfixes

- **STG-2.179** — AlphaESS dynamic_min_soc_sensor: deprecated async_track_state_change durch async_track_state_change_event ersetzen (`core_restart`)
- **STG-3.82** — PV-Forecast Coordinator: _async_refresh_intraday_only Task beim HA-Stop-Event abbrechen (`core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.38.0

**Datum:** 2026-07-05  
**Items:** 3  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-4.34** — Consumption Forecast Intraday-Chart auf 24h Vergangenheit/Zukunft und PV-Forecast-Farbschema anpassen (`yaml_reload`)

## Bugfixes

- **STG-2.179** — AlphaESS dynamic_min_soc_sensor: deprecated async_track_state_change durch async_track_state_change_event ersetzen (`core_restart`)
- **STG-3.82** — PV-Forecast Coordinator: _async_refresh_intraday_only Task beim HA-Stop-Event abbrechen (`core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.51.2

**Datum:** 2026-07-05  
**Items:** 3  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.176** — Phase-3 Energiebilanz verwendet target_end_soc_pct als Untergrenze (`core_restart`)
- **STG-2.177** — Phase-3 Energiebilanz begrenzt PV-Überschuss bei voller Batterie (`core_restart`)

## Dokumentation

- **STG-2.178** — Phase-3 Dashboard-Texte präzisieren (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.51.1

**Datum:** 2026-07-04  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.175** — Phasen-Vorschau zeigt Load-up Phase nicht, wenn T2 auf Sunset fällt (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.51.0

**Datum:** 2026-07-04  
**Items:** 3  
**Gesamt-Deployment:** yaml_reload

## Neue Features

- **STG-4.33** — PV-Ereignisanzeige: eigenes Dashboard, aussagekräftigere Einträge, 24h/10-Eintrag-Filter (`yaml_reload`)

## Bugfixes

- **STG-2.174** — PV Dynamic MIN-SOC Write Automation: Setup-Fehler 'max' >= 2 beheben (`yaml_reload`)
- **STG-7.19** — Deploy-Pipeline: Mehrfache core_restart-Ausführung verhindern (`none`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.50.1

**Datum:** 2026-07-04  
**Items:** 1  
**Gesamt-Deployment:** yaml_reload

## Bugfixes

- **STG-4.32** — Dashboard: Markdown-Tabellenformatierung nach v1.50.0 reparieren (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.50.0

**Datum:** 2026-07-04  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.164** — SOC-Plan-Kurve: Nacht-Verlauf an Verbrauchsprognose und Min-SOC-Stufen ausrichten (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.49.0

**Datum:** 2026-07-04  
**Items:** 5  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.172** — Backlog Claim/Unassign: exklusive Zuweisung von Backlog-Items (`none`)
- **STG-2.173** — Backlog Claim: vor Claim prüfen, ob Item auf origin/main bereits vergeben ist (`none`)

## Bugfixes

- **STG-2.171** — Fix: Automation 'PV Dynamic MIN-SOC Write' meldet 'Already running' (`yaml_reload`)

## Technisch

- **STG-9.4** — PV-Forecast: Recorder- und SQLite-Zugriffe robust und performant machen (`core_restart`)
- **STG-9.6** — PV-Forecast: Thread-lokale SQLite-Verbindungen beim Shutdown für alle Threads schließen (`core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.48.1

**Datum:** 2026-07-03  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.170** — Fix: SOC-Plan-Kurve springt vor Sonnenaufgang auf alten dynamischen MIN-SOC (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.48.0

**Datum:** 2026-07-03  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.169** — SOC-Plan-Kurve in der Nacht aus prognostiziertem Verbrauch und dynamischem MIN-SOC berechnen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.47.0

**Datum:** 2026-07-03  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.168** — Dynamischen MIN-SOC auf maximal 50% begrenzen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.46.1

**Datum:** 2026-07-03  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.167** — Regression-Fix: dynamische MIN-SOC-Steuerung bleibt nach Crossover aktiv (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.46.0

**Datum:** 2026-07-03  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.166** — Dynamische MIN-SOC-Steuerung ab Cross-Over-Termin abends starten (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.45.0

**Datum:** 2026-07-03  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.165** — Dynamischer MIN-SOC: verzögerter Abfall mit Reserve-Puffer (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.44.1

**Datum:** 2026-07-02  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.163** — SOC-Plan-Kurve in der Nacht aktiv zum dynamischen MIN-SOC abfallen lassen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.44.0

**Datum:** 2026-07-02  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.162** — Dynamischen MIN-SOC in SOC-Plan-Kurve für die Nacht verwenden (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.43.1

**Datum:** 2026-07-02  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.161** — Dynamischer MIN-SOC bei Änderung der Eingaben neu berechnen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.43.0

**Datum:** 2026-07-02  
**Items:** 2  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.159** — Dynamischer MIN-SOC sofort neu berechnen bei Toggle (`yaml_reload`)

## Bugfixes

- **STG-2.160** — Dynamischer MIN-SOC direkt nach Sensor-Start berechnen (`core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.42.1

**Datum:** 2026-07-02  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.158** — MIN-SOC-Berechnung auch im disabled-Modus anzeigen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.42.0

**Datum:** 2026-07-02  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.157** — Dynamische MIN-SOC Steuerung in Night-Phase und Randphasen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.41.2

**Datum:** 2026-07-02  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.156** — Phasen-Vorschau: Null-Längen-Phasen vermeiden und Darstellung verbessern (`yaml_reload, core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.41.1

**Datum:** 2026-07-02  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.155** — Aktive Phase über HA-Neustart hinweg konsistent persistieren (`yaml_reload, core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.41.0

**Datum:** 2026-07-02  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.152** — Batteriesteuerung auf Phasenmodell Day / Load-up / Night umbauen (Basisversion) (`yaml_reload, core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.40.0

**Datum:** 2026-07-02  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.151** — Ziel-SOC Phase 3: Verfügbare Energie aus Batterie + PV mit Verbrauch vergleichen und erwarteten SOC zum Recovery zeigen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.39.0

**Datum:** 2026-07-02  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.150** — Ziel-SOC Phase 3: Angenommenen Verbrauch zwischen Abend- und Recovery-Crossover anzeigen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.38.4

**Datum:** 2026-07-01  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-8.13** — rpi_power: Workaround für NoneType-Fehler in binary_sensor update (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.38.3

**Datum:** 2026-07-01  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-3.81** — PV-Forecast: NumPy aus manifest.json requirements entfernen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.38.2

**Datum:** 2026-07-01  
**Items:** 2  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.149** — AlphaESS Charge Control: SOC-Plan-Kurve wird im Dashboard nicht mehr angezeigt (`yaml_reload`)
- **STG-3.80** — PV-Forecast: NumPy-Requirement an HA-System mit NumPy 2.x anpassen (`core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.38.1

**Datum:** 2026-07-01  
**Items:** 1  
**Gesamt-Deployment:** yaml_reload

## Bugfixes

- **STG-3.79** — PV-Forecast: AC-Entities im House Consumption Forecast Package konfigurieren (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.38.0

**Datum:** 2026-07-01  
**Items:** 3  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.76** — PV-Forecast: Intraday-Refresh-Intervall konfigurierbar und Deep-Copy-Overhead eliminieren (`core_restart`)

## Bugfixes

- **STG-3.75** — PV-Forecast: NumPy als hartes Requirement deklarieren (`core_restart`)

## Technisch

- **STG-1.4** — Anwesenheits-Tracking aus Zirkulationspumpe und House Consumption Forecast entfernen (`yaml_reload, core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.37.0

**Datum:** 2026-06-30  
**Items:** 3  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.67** — House Consumption Forecast: Hartkodierte Entity-IDs aus Dashboard und Package entfernen (`core_restart`)
- **STG-3.70** — House Consumption Forecast: Wettercode als kategoriales Feature one-hot encoden (`core_restart`)

## Technisch

- **STG-3.71** — House Consumption Forecast: Permutation-Feature-Selektion performancetechnisch begrenzen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.36.0

**Datum:** 2026-06-30  
**Items:** 3  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.59** — House Consumption Forecast: Feature-Skalierung korrigieren (Z-Score vs. MinMax) (`core_restart`)
- **STG-3.60** — House Consumption Forecast: Feature-Selektion einfuehren (`core_restart`)
- **STG-3.61** — House Consumption Forecast: Open-Meteo Wetterfeatures erweitern (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.35.0

**Datum:** 2026-06-29  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.37** — House Consumption Forecast: Cooling-Degree-Hours als wetterbasiertes Kühlfeature (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.34.1

**Datum:** 2026-06-28  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-3.58** — Bugfix: Feature-Einfluss-Tabelle zeigt falschen Gesamtforecast (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.34.0

**Datum:** 2026-06-28  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.57** — Feature-Einfluss-Tabelle für Temperatur und ACs im Consumption Forecast Dashboard (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.33.1

**Datum:** 2026-06-28  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-3.56** — SwitchBot AC Entity-IDs auf deutsche Namen korrigieren (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.33.0

**Datum:** 2026-06-28  
**Items:** 3  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.54** — Dashboard: SwitchBot AC-Steckdosen anzeigen (`yaml_reload`)
- **STG-3.55** — Forecast: SwitchBot AC-Zustände und -Leistung als Modell-Features nutzen (`core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.32.8

**Datum:** 2026-06-28  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-3.52** — AC-Modus aus House Consumption Forecast entfernen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.28.3

**Datum:** 2026-06-28  
**Items:** 2  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-3.52** — AC-Modus aus House Consumption Forecast entfernen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.32.7

**Datum:** 2026-06-28  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-3.51** — Forecast-Integrations: api_health Service-Call awaiten (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.32.6

**Datum:** 2026-06-28  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-8.12** — api_health: services.yaml hinzufügen um HA-Warnung zu vermeiden (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.32.5

**Datum:** 2026-06-28  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-3.49** — PV-Forecast: Training beschleunigen durch vektorisierte Distanz und Sunrise-Fenster-Filter (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.32.3

**Datum:** 2026-06-28  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-3.48** — PV-Forecast: _distance weiter robust machen und Exception-Typ diagnostizieren (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.32.2

**Datum:** 2026-06-28  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-3.47** — PV-Forecast: ForecastScheduler plant delayed Initial-Refresh nicht zuverlässig nach HA-Restart (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.32.1

**Datum:** 2026-06-28  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-3.46** — PV-Forecast: Mahalanobis-Distanz in model.py:_distance robust gegen fehlende/ungültige Features machen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.32.0

**Datum:** 2026-06-28  
**Items:** 2  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.44** — PV-Forecast Confidence: Modell-Band durch historische Kalibrierung relativieren (`core_restart`)

## Bugfixes

- **STG-3.45** — PV-Forecast: Drift-Score um MAE- und Bias-Anteil ergänzen (STG-4.5a Nachhole) (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.31.0

**Datum:** 2026-06-27  
**Items:** 1  
**Gesamt-Deployment:** yaml_reload

## Neue Features

- **STG-4.29** — SOC-Kurven visuell glätten ohne Rampen (shape: hvh) (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.30.0

**Datum:** 2026-06-27  
**Items:** 4  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.148** — SOC-Plan-Diagramm auf 24 + 12 Stunden Zeitfenster erweitern (`core_restart, yaml_reload`)

## Bugfixes

- **STG-2.147** — Min-SOC (Entladungsgrenze) in SOC-Plan-Kurve berücksichtigen (`core_restart`)
- **STG-4.28** — SOC-Ist- und SOC-Plan-Verlauf als Treppenfunktion darstellen (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.29.0

**Datum:** 2026-06-27  
**Items:** 7  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-6.15** — API Status Dashboard: Phase B — Open-Meteo Echtzeit-Status via zentralem api_health-Service (`core_restart`)
- **STG-6.16** — API Status Dashboard: Phase C — AlphaESS Modbus, DWD und SwitchBot BLE Status (`yaml_reload, core_restart`)

## Bugfixes

- **STG-2.146** — AlphaESS Evaluation Sensoren: Update dauert wieder >10s (`core_restart`)
- **STG-3.36** — House Consumption Forecast: Coordinator-Methoden-Aufrufe in IntervalEvaluator reparieren (`core_restart`)
- **STG-3.42** — House Consumption Forecast: Weather Archive Fetch Failed analysieren (`core_restart`)
- **STG-8.11** — Zirkulationspumpe: ZS7 Switch mit Retry - Already running (`yaml_reload`)

## Technisch

- **STG-2.11** — Entity-Layer entflechten: Attributes-Pruning, Rendering und Formatierung in Domain/Service verschieben (`core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.28.2

**Datum:** 2026-06-24  
**Items:** 1  
**Gesamt-Deployment:** none

## Bugfixes

- **STG-11.8** — Release Pipeline: Änderungen an ha-pv-config/packages müssen auch ha-pv-config-package deployen (`none`)


---

# Release v1.28.1

**Datum:** 2026-06-23  
**Items:** 2  
**Gesamt-Deployment:** none

## Bugfixes

- **STG-3.39** — House Consumption Forecast: Pre-existing Test-Failures beheben (`none`)


---

# Release v1.28.0

**Datum:** 2026-06-23  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.38** — House Consumption Forecast: AC-Modus-Schalter im Dashboard und als Modellfeature (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.27.6

**Datum:** 2026-06-22  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-11.7** — AlphaESS Batteriesteuerung: Min-SOC-Automation ID kleinschreiben und Bedingungen vereinfachen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.27.5

**Datum:** 2026-06-22  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-11.6** — AlphaESS Batteriesteuerung: Min-SOC-Automation in Automations-Paket verschieben (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.27.4

**Datum:** 2026-06-22  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-11.5** — AlphaESS Batteriesteuerung: Min-SOC-Anzeige zeigt korrekten Wert und broken Sensoren entfernt (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.27.3

**Datum:** 2026-06-22  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-11.4** — AlphaESS Batteriesteuerung: Min-SOC-Anzeige über UPS-Reserve-Sensor reparieren (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.27.2

**Datum:** 2026-06-22  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-11.3** — AlphaESS Batteriesteuerung: Min-SOC-Anzeige im Dashboard reparieren (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.27.1

**Datum:** 2026-06-22  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-11.2** — AlphaESS Batteriesteuerung: Min-SOC über number.batusescap steuern (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.27.0

**Datum:** 2026-06-22  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-11.1** — AlphaESS Batteriesteuerung: Min-SOC bei Max Battery automatisch anpassen und anzeigen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.26.5

**Datum:** 2026-06-21  
**Items:** 2  
**Gesamt-Deployment:** core_restart

## Technisch

- **STG-3.34** — House-Consumption-Forecast: ModelTrainingService aus Coordinator extrahieren (`core_restart`)
- **STG-3.35** — House-Consumption-Forecast: ForecastSnapshotBuilder aus Coordinator extrahieren (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.26.4

**Datum:** 2026-06-21  
**Items:** 3  
**Gesamt-Deployment:** core_restart

## Technisch

- **STG-3.31** — House-Consumption-Forecast: StateReaderService aus Coordinator extrahieren (`core_restart`)
- **STG-3.32** — House-Consumption-Forecast: WeatherContextService aus Coordinator extrahieren (`core_restart`)
- **STG-3.33** — House-Consumption-Forecast: PresenceContextService aus Coordinator extrahieren (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.26.3

**Datum:** 2026-06-21  
**Items:** 4  
**Gesamt-Deployment:** yaml_reload

## Bugfixes

- **STG-2.144** — PV-Config: Modbus-Hausverbrauch-Tool von hartkodierten Verbindungsdaten befreien (`none`)
- **STG-2.145** — PV-Config: Modbus-Hausverbrauchs-Sensor mit Triple-Guard absichern (`yaml_reload`)
- **STG-3.28** — PV-Forecast: Deploy-Dependency fuer V2-Entities korrigieren (`none`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.26.2

**Datum:** 2026-06-20  
**Items:** 1  
**Gesamt-Deployment:** yaml_reload

## Bugfixes

- **STG-6.18** — API Status Dashboard: HA-spezifische Zeitformatierung in Template-Sensoren korrigieren (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.26.1

**Datum:** 2026-06-20  
**Items:** 1  
**Gesamt-Deployment:** yaml_reload

## Bugfixes

- **STG-6.17** — API Status Dashboard Phase A: Template-Konfiguration korrigieren (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.26.0

**Datum:** 2026-06-20  
**Items:** 1  
**Gesamt-Deployment:** yaml_reload

## Neue Features

- **STG-6.14** — API Status Dashboard: Phase A — Dashboard-Seite + zentrale Template-Sensoren (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.25.3

**Datum:** 2026-06-20  
**Items:** 5  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-2.141** — DWD Dashboard: Forecast-Sensoren reparieren (weather.get_forecasts funktioniert nicht in Template-Trigger-Actions) (`yaml_reload, core_restart`)
- **STG-2.142** — DWD Dashboard: Wetterwarnungs-Entität optional machen oder ersetzen (`yaml_reload`)
- **STG-2.143** — DWD Dashboard: Robustere Fehleranzeige und ApexCharts-Optionalität (`yaml_reload`)

## Technisch

- **STG-2.138** — Batterie-Refactor Phase 4: Phase-3-Strategie in phase3_power_window.py auslagern (`core_restart`)
- **STG-2.139** — Batterie-Refactor Phase 5: Phase-1/Phase-2-Logik in phase1_phase2.py auslagern (`core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.25.2

**Datum:** 2026-06-20  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Technisch

- **STG-2.140** — Batterie-Refactor Phase 6: Auflösungslogik konsolidieren, Defaults zentralisieren und Phase-3-Duplikate entfernen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.25.1

**Datum:** 2026-06-20  
**Items:** 3  
**Gesamt-Deployment:** core_restart

## Technisch

- **STG-2.135** — Batterie-Refactor Phase 1: _build_snapshot() in sensor.py als Pipeline aufteilen (`core_restart`)
- **STG-2.136** — Batterie-Refactor Phase 2: Energy-Math und Capacity-Schätzung auslagern (`core_restart`)
- **STG-2.137** — Batterie-Refactor Phase 3: Forecast-Extraktion in forecast_parser.py auslagern (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.25.0

**Datum:** 2026-06-20  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-3.27** — PV-Forecast: Globaler Scale Factor lernt aus eigener Ausgabe (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.24.0

**Datum:** 2026-06-19  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.134** — Max-Battery Button fuer Batterie-Steuerung (`yaml_reload, core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.23.0

**Datum:** 2026-06-17  
**Items:** 2  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-2.133** — Ziel-SOC Phase 3 nie unter 80 % begrenzen (`yaml_reload, core_restart`)
- **STG-3.25** — PV-Forecast: Globaler Tages-Skalierungsfaktor für strukturelle Drift-Korrektur (`core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.22.0

**Datum:** 2026-06-12  
**Items:** 6  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.26** — PV-Forecast Dashboard V2: Globaler Skalierungsfaktor in Modell-Erklärung anzeigen (`yaml_reload`)
- **STG-8.3** — Zirkulationspumpe: Dashboard-Toggle für Anwesenheitserkennung (`yaml_reload`)

## Bugfixes

- **STG-3.24** — PV-Forecast: Auto-Retrain-Status in model_status Attributen exponieren (`core_restart`)

## Bugfixes

- **STG-4.20** — PV-Forecast: Gate-Agent-Follow-up zu STG-4.19 (Test + Recorder-Pruning) (`none`)

## Technisch

- **STG-2.132** — Batterie-Steuerung Dashboard: Configuration-Seite Berechnungserklärung konsistent mit Runtime-Logik (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.22.1

**Datum:** 2026-06-11  
**Items:** 1  
**Gesamt-Deployment:** yaml_reload

## Technisch

- **STG-2.131** — Batterie-Steuerung Dashboard: Configuration-Seite Berechnungserklärung konsistent mit Runtime-Logik (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.22.0

**Datum:** 2026-06-08  
**Items:** 4  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.23** — PV-Forecast: hourly_neighbor_matches auf eigenen Sensor auslagern (`core_restart`)

## Bugfixes

- **STG-2.130** — Phase-3 Renderer-Beschreibung korrigieren und no_evening_excess-Fallback prüfen (`core_restart`)
- **STG-3.21** — PV-Forecast: hourly_neighbor_matches verdrängt stündliche Daten auf Tomorrow-Sensoren (`core_restart`)
- **STG-3.22** — PV-Forecast: hourly_neighbor_matches verdrängt table_rows/hourly_forecast auf today (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.21.0

**Datum:** 2026-06-07  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.20** — PV-Forecast: Nachbar-Matches als natürlichsprachliche Wetter-Story (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.20.0

**Datum:** 2026-06-06  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.19** — PV-Forecast: Nachbar-Matches mit pro-Nachbar Top-Unterschieden (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.19.1

**Datum:** 2026-06-06  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-3.18** — PV-Forecast: Nachbar-Matches zeigen normalisierte statt absolute kWh-Werte (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.19.0

**Datum:** 2026-06-06  
**Items:** 2  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-4.23** — System Info Dashboard: Default-Seite auf 'system-info' setzen (`yaml_reload`)

## Bugfixes

- **STG-3.17** — PV-Forecast: Nachbar-Matches verschwinden durch Payload-Pruning (`core_restart`)

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.18.4

**Datum:** 2026-06-04  
**Items:** 1  
**Gesamt-Deployment:** none

## Bugfixes

- **STG-5.6** — Kaputte Tests fixen: backlog_integrity + circulation_pump (`none`)


---

# Release v1.18.3

**Datum:** 2026-06-04  
**Items:** 2  
**Gesamt-Deployment:** core_restart

## Erforderliche Schritte

1. `yaml_reload`
1. `core_restart`


---

# Release v1.18.2

**Datum:** 2026-06-04  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **STG-3.16** — PV-Forecast: Weather-Archive force_refresh lädt unnötig alles von API (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.18.1

**Datum:** 2026-05-24  
**Items:** 1  
**Gesamt-Deployment:** yaml_reload

## Bugfixes

- **STG-8.5** — Zirkulationspumpe: BLE-Verbindungsfehler bei SwitchBot führt zu unzuverlässigem Schalten (`yaml_reload`)

## Erforderliche Schritte

1. `yaml_reload`


---

# Release v1.18.0

**Datum:** 2026-05-24  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.15** — PV-Forecast Nachbar-Matches: Wetter-Features wieder in Dashboard-Tabelle anzeigen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.17.0

**Datum:** 2026-05-24  
**Items:** 4  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.13** — PV-Forecast Dashboard: Modell-Interpretation auf eigene Seite mit Amateur-Erklärungen (`core_restart`)
- **STG-3.14** — PV-Forecast: Nachbar-Matches mit echter Distanz, Uhrzeit und Feature-Delta anzeigen (`core_restart`)

## Bugfixes

- **BL-3.12** — PV-Forecast: Nachbar-Matches werden geprunt und sind im Dashboard nicht sichtbar (`core_restart`)
- **BL-3.13** — PV-Forecast Dashboard: Nachbar-Matches Tabelle wird nicht als Markdown-Tabelle gerendert (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.17.0

**Datum:** 2026-05-24  
**Items:** 4  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.13** — PV-Forecast Dashboard: Modell-Interpretation auf eigene Seite mit Amateur-Erklärungen (`core_restart`)
- **STG-3.14** — PV-Forecast: Nachbar-Matches mit echter Distanz, Uhrzeit und Feature-Delta anzeigen (`core_restart`)

## Bugfixes

- **BL-3.12** — PV-Forecast: Nachbar-Matches werden geprunt und sind im Dashboard nicht sichtbar (`core_restart`)
- **BL-3.13** — PV-Forecast Dashboard: Nachbar-Matches Tabelle wird nicht als Markdown-Tabelle gerendert (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.16.2

**Datum:** 2026-05-24  
**Items:** 2  
**Gesamt-Deployment:** core_restart

## Technisch

- **STG-2.11a** — Entity-Layer entflechten Phase A: Recorder-Pruning und Template-Rendering extrahieren (`core_restart`)
- **STG-2.11b** — Entity-Layer entflechten Phase B: Intervall-Berechnung in Coordinator/Service verschieben (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.16.1

**Datum:** 2026-05-24  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Bugfixes

- **BL-3.10** — Weather-Archive: Incremental-Fetch funktioniert nicht nach HA-Neustart (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.16.0

**Datum:** 2026-05-24  
**Items:** 1  
**Gesamt-Deployment:** core_restart

## Neue Features

- **STG-3.5** — PV-Forecast: Permutation Importance für Feature-Einfluss berechnen und anzeigen (`core_restart`)

## Erforderliche Schritte

1. `core_restart`


---

# Release v1.15.0

**Datum:** 2026-05-24  
**Items:** 3  
**Gesamt-Deployment:** none

## Neue Features

- **STG-3.8** — Weather-Archive Diagnose-Metriken in Model Health Tabelle anzeigen (`none`)
- **STG-3.9** — Inkrementelles Weather-Archive-Fetching: nur fehlende/stale Ranges von API holen (`none`)

## Bugfixes

- **STG-10.9** — Release-Pipeline: Robustheit und Backlog-Validierung nach v1.15.0-Incident (`none`)


---

# Release v1.15.0

**Datum:** 2026-05-24  
**Items:** 6  
**Gesamt-Deployment:** none

## Neue Features

- **STG-10.4** — DWD-Wetterdashboard: Regenradar-Integration (`none`)
- **STG-10.5** — DWD-Wetterdashboard: 7-Tage-Ausblick (Karten + Trenddiagramm) (`none`)
- **STG-10.6** — DWD-Wetterdashboard: Warnungen + Layout-Finalisierung und Abnahme (`none`)
- **STG-9.2** — Gate-Agent: Standardisiertes Prompt-Template erstellen (`none`)
- **STG-9.3** — Gate-Agent: Komplettes Optimierungspaket (Pre-Flight + Trivial-Bypass + Diff-Optimierer) (`none`)

## Dokumentation

- **STG-10.8** — Release-Prozess in rules.md und eigenes Guide dokumentieren (`none`)


---

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
