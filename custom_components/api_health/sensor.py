"""Sensor platform for the API Health component."""

from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timedelta
from typing import Any

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.util import dt as dt_util

from .helpers import apply_staleness, build_attributes, compute_overall_status

# How often the sensor re-evaluates report staleness without a new report.
STALE_CHECK_INTERVAL = timedelta(minutes=30)


def _compute_and_build(store: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    """Compute current state and attributes from the shared store.

    Reports older than ``DEFAULT_MAX_REPORT_AGE`` are downgraded to
    ``unknown`` so a source that stopped reporting cannot pin the overall
    state (e.g. at ``failed``) forever.
    """
    reports = apply_staleness(store["reports"], dt_util.now())
    state = compute_overall_status(reports)
    attrs = build_attributes(reports)
    return state, attrs


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the API Health overall sensor."""
    async_add_entities([ApiHealthOverallSensor(hass)], update_before_add=True)


class ApiHealthOverallSensor(SensorEntity):
    """Aggregated worst-status sensor for reported API health.

    The sensor subscribes to the in-memory report store maintained by the
    ``api_health.report`` service. Every incoming report triggers an update;
    a periodic timer re-evaluates staleness in between reports.
    """

    _attr_name = "API Health Overall"
    _attr_unique_id = "api_health_overall"
    _attr_icon = "mdi:web"
    _attr_should_poll = False

    def __init__(self, hass: HomeAssistant) -> None:
        self.hass = hass
        self._store = hass.data["api_health"]
        state, attrs = _compute_and_build(self._store)
        self._attr_native_value = state
        self._attr_extra_state_attributes = attrs
        self._update_callback = self._make_update_callback()
        self._unsub_stale_check: Callable[[], None] | None = None

    def _make_update_callback(self) -> Callable[[], None]:
        def _callback() -> None:
            state, attrs = _compute_and_build(self._store)
            self._attr_native_value = state
            self._attr_extra_state_attributes = attrs
            self.async_write_ha_state()

        return _callback

    def _handle_stale_check(self, _now: datetime) -> None:
        """Periodic re-evaluation so stale reports age out without new data."""
        self._update_callback()

    async def async_added_to_hass(self) -> None:
        self._store["listeners"].append(self._update_callback)
        self._unsub_stale_check = async_track_time_interval(self.hass, self._handle_stale_check, STALE_CHECK_INTERVAL)

    async def async_will_remove_from_hass(self) -> None:
        if self._update_callback in self._store["listeners"]:
            self._store["listeners"].remove(self._update_callback)
        if self._unsub_stale_check is not None:
            self._unsub_stale_check()
            self._unsub_stale_check = None
