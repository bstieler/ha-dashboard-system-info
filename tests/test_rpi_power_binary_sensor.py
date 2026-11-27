"""Regression tests for the rpi_power repair-issue cleanup (STG-8.57).

``rpi_bad_power`` is not installed in the test venv, so a minimal stub is
registered before the component is imported.
"""

from __future__ import annotations

import sys
import types
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

COMPONENT_ROOT = Path(__file__).resolve().parents[1] / "custom_components"
if str(COMPONENT_ROOT) not in sys.path:
    sys.path.insert(0, str(COMPONENT_ROOT))

if "rpi_bad_power" not in sys.modules:
    _stub = types.ModuleType("rpi_bad_power")
    _stub.UnderVoltage = MagicMock  # type: ignore[attr-defined]
    _stub.new_under_voltage = MagicMock()  # type: ignore[attr-defined]
    sys.modules["rpi_bad_power"] = _stub

from rpi_power.binary_sensor import RaspberryChargerBinarySensor  # noqa: E402


def _make_sensor(under_voltage_value: bool) -> tuple[RaspberryChargerBinarySensor, MagicMock]:
    under_voltage = MagicMock()
    under_voltage.get.return_value = under_voltage_value
    sensor = RaspberryChargerBinarySensor(under_voltage)
    sensor.hass = MagicMock()
    return sensor, under_voltage


class TestRpiPowerRepairIssue:
    def test_under_voltage_creates_issue(self) -> None:
        sensor, _ = _make_sensor(True)
        with (
            patch("rpi_power.binary_sensor.create_issue") as create,
            patch("rpi_power.binary_sensor.delete_issue") as delete,
        ):
            sensor.update()
        create.assert_called_once()
        delete.assert_not_called()
        assert sensor.is_on is True

    def test_normalized_voltage_deletes_issue(self) -> None:
        sensor, under_voltage = _make_sensor(True)
        with (
            patch("rpi_power.binary_sensor.create_issue"),
            patch("rpi_power.binary_sensor.delete_issue") as delete,
        ):
            sensor.update()
            under_voltage.get.return_value = False
            sensor.update()
        delete.assert_called_once_with(sensor.hass, "rpi_power", "under_voltage_detected")
        assert sensor.is_on is False

    def test_missing_client_marks_entity_unavailable(self) -> None:
        sensor, _ = _make_sensor(False)
        sensor._under_voltage = None
        sensor.update()
        assert sensor.available is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
