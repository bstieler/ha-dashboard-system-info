"""API Health custom component.

Provides a central service ``api_health.report`` that other integrations can use
to publish real-time status of external API calls. The component exposes a single
sensor entity ``sensor.api_health_overall`` that shows the worst reported status.
"""

from __future__ import annotations

from datetime import datetime
import logging
from typing import Any
from zoneinfo import ZoneInfo

import voluptuous as vol
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

from .helpers import build_attributes, compute_overall_status

DOMAIN = "api_health"
_LOGGER = logging.getLogger(__name__)

SERVICE_REPORT = "report"

REPORT_SCHEMA = vol.Schema(
    {
        vol.Required("source"): cv.string,
        vol.Required("status"): vol.In(["ok", "degraded", "failed", "unknown"]),
        vol.Optional("timestamp"): cv.datetime,
        vol.Optional("error"): cv.string,
        vol.Optional("details"): cv.string,
    }
)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the API Health service and shared state."""
    hass.data.setdefault(DOMAIN, {"reports": {}, "listeners": []})

    async def handle_report(call: ServiceCall) -> None:
        """Store a status report and notify listeners."""
        data: dict[str, Any] = dict(call.data)
        source = data["source"]
        timestamp = data.get("timestamp")
        if isinstance(timestamp, datetime):
            data["timestamp"] = timestamp.isoformat()
        elif timestamp is None:
            tz = ZoneInfo(str(hass.config.time_zone))
            data["timestamp"] = datetime.now(tz).isoformat()

        store = hass.data[DOMAIN]
        store["reports"][source] = data
        for listener in store["listeners"]:
            listener()

        _LOGGER.debug("API health report from %s: %s", source, data.get("status"))

    hass.services.async_register(
        DOMAIN,
        SERVICE_REPORT,
        handle_report,
        schema=REPORT_SCHEMA,
    )
    return True
