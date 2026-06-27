"""Sensor platform for the API Health component."""

from __future__ import annotations

from typing import Any

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .helpers import build_attributes, compute_overall_status


def _compute_and_build(store: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    """Compute current state and attributes from the shared store."""
    state = compute_overall_status(store["reports"])
    attrs = build_attributes(store["reports"])
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
    ``api_health.report`` service. Every incoming report triggers an update.
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

    def _make_update_callback(self):
        def _callback() -> None:
            state, attrs = _compute_and_build(self._store)
            self._attr_native_value = state
            self._attr_extra_state_attributes = attrs
            self.async_write_ha_state()

        return _callback

    async def async_added_to_hass(self) -> None:
        self._store["listeners"].append(self._update_callback)

    async def async_will_remove_from_hass(self) -> None:
        if self._update_callback in self._store["listeners"]:
            self._store["listeners"].remove(self._update_callback)
