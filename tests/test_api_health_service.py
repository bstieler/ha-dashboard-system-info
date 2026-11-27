"""Service-path tests for the API Health component (STG-8.57).

These tests exercise the full runtime path ``async_setup`` → registered
``api_health.report`` handler → listener → ``ApiHealthOverallSensor`` state
with a mocked HomeAssistant instance (the pattern used by the other
custom-component test suites, e.g. ha-pv-config/tests).
"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from homeassistant.util import dt as dt_util

COMPONENT_ROOT = Path(__file__).resolve().parents[1] / "custom_components"
if str(COMPONENT_ROOT) not in sys.path:
    sys.path.insert(0, str(COMPONENT_ROOT))

import api_health  # noqa: E402
from api_health.sensor import ApiHealthOverallSensor  # noqa: E402


def _make_hass() -> tuple[MagicMock, dict[tuple[str, str], Any]]:
    """Return a mocked hass plus the registry of registered service handlers."""
    hass = MagicMock()
    hass.data = {}
    registered: dict[tuple[str, str], Any] = {}

    def _register(domain: str, service: str, handler: Any, schema: Any = None) -> None:
        registered[(domain, service)] = handler

    hass.services.async_register.side_effect = _register
    return hass, registered


def _service_call(data: dict[str, Any]) -> MagicMock:
    call = MagicMock()
    call.data = data
    return call


async def _added_sensor(hass: MagicMock) -> ApiHealthOverallSensor:
    """Create the sensor and run async_added_to_hass with the timer mocked."""
    sensor = ApiHealthOverallSensor(hass)
    sensor.async_write_ha_state = MagicMock()
    with patch("api_health.sensor.async_track_time_interval", return_value=MagicMock()):
        await sensor.async_added_to_hass()
    return sensor


class TestApiHealthServicePath:
    async def test_setup_registers_report_service(self) -> None:
        hass, registered = _make_hass()
        assert await api_health.async_setup(hass, {}) is True
        assert (api_health.DOMAIN, api_health.SERVICE_REPORT) in registered
        assert hass.data[api_health.DOMAIN] == {"reports": {}, "listeners": []}

    async def test_report_updates_sensor_state_and_attributes(self) -> None:
        hass, registered = _make_hass()
        await api_health.async_setup(hass, {})
        handler = registered[(api_health.DOMAIN, api_health.SERVICE_REPORT)]
        sensor = await _added_sensor(hass)

        await handler(
            _service_call(
                {
                    "source": "open_meteo",
                    "status": "failed",
                    "timestamp": None,
                    "error": "timeout",
                    "details": None,
                }
            )
        )

        assert sensor.native_value == "failed"
        attrs = sensor.extra_state_attributes
        assert attrs["open_meteo_status"] == "failed"
        assert attrs["open_meteo_error"] == "timeout"
        assert attrs["open_meteo_last_call"] is not None
        sensor.async_write_ha_state.assert_called_once()

    async def test_missing_timestamp_defaults_to_now(self) -> None:
        hass, registered = _make_hass()
        await api_health.async_setup(hass, {})
        handler = registered[(api_health.DOMAIN, api_health.SERVICE_REPORT)]

        await handler(_service_call({"source": "open_meteo", "status": "ok"}))

        stored = hass.data[api_health.DOMAIN]["reports"]["open_meteo"]
        parsed = datetime.fromisoformat(stored["timestamp"])
        assert parsed.tzinfo is not None
        assert abs((dt_util.now() - parsed).total_seconds()) < 60

    async def test_datetime_timestamp_is_serialized(self) -> None:
        hass, registered = _make_hass()
        await api_health.async_setup(hass, {})
        handler = registered[(api_health.DOMAIN, api_health.SERVICE_REPORT)]
        moment = datetime(2026, 6, 26, 10, 0, 0)

        await handler(_service_call({"source": "open_meteo", "status": "ok", "timestamp": moment}))

        stored = hass.data[api_health.DOMAIN]["reports"]["open_meteo"]
        assert stored["timestamp"] == moment.isoformat()

    async def test_worst_status_wins_across_sources(self) -> None:
        hass, registered = _make_hass()
        await api_health.async_setup(hass, {})
        handler = registered[(api_health.DOMAIN, api_health.SERVICE_REPORT)]
        sensor = await _added_sensor(hass)

        await handler(_service_call({"source": "open_meteo", "status": "ok"}))
        assert sensor.native_value == "ok"
        await handler(_service_call({"source": "alphaess", "status": "degraded"}))
        assert sensor.native_value == "degraded"

    async def test_listener_removed_on_will_remove(self) -> None:
        hass, registered = _make_hass()
        await api_health.async_setup(hass, {})
        handler = registered[(api_health.DOMAIN, api_health.SERVICE_REPORT)]
        sensor = await _added_sensor(hass)

        await sensor.async_will_remove_from_hass()
        assert hass.data[api_health.DOMAIN]["listeners"] == []

        await handler(_service_call({"source": "open_meteo", "status": "failed"}))
        sensor.async_write_ha_state.assert_not_called()

    async def test_stale_check_timer_is_registered_and_cancelled(self) -> None:
        hass, _ = _make_hass()
        await api_health.async_setup(hass, {})
        unsub = MagicMock()
        sensor = ApiHealthOverallSensor(hass)
        with patch("api_health.sensor.async_track_time_interval", return_value=unsub) as track:
            await sensor.async_added_to_hass()
            track.assert_called_once()
        await sensor.async_will_remove_from_hass()
        unsub.assert_called_once()

    async def test_periodic_check_ages_out_stale_failed_report(self) -> None:
        hass, registered = _make_hass()
        await api_health.async_setup(hass, {})
        handler = registered[(api_health.DOMAIN, api_health.SERVICE_REPORT)]
        sensor = await _added_sensor(hass)

        await handler(_service_call({"source": "alphaess", "status": "failed"}))
        assert sensor.native_value == "failed"

        # Simulate the source having stopped reporting long ago.
        report = hass.data[api_health.DOMAIN]["reports"]["alphaess"]
        report["timestamp"] = "2000-01-01T00:00:00+00:00"
        sensor.async_write_ha_state.reset_mock()

        sensor._handle_stale_check(dt_util.now())

        assert sensor.native_value == "unknown"
        assert sensor.extra_state_attributes["alphaess_status"] == "unknown"
        sensor.async_write_ha_state.assert_called_once()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
