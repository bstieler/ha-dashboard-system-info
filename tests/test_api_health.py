"""Unit tests for API Health helper logic.

These tests intentionally import only the HA-free helpers module so they can run
without a Home Assistant runtime.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

HELPERS_PATH = (
    Path(__file__).resolve().parents[1]
    / "custom_components"
    / "api_health"
    / "helpers.py"
)

_helpers_spec = importlib.util.spec_from_file_location("api_health_helpers", HELPERS_PATH)
assert _helpers_spec is not None and _helpers_spec.loader is not None
helpers = importlib.util.module_from_spec(_helpers_spec)
sys.modules[_helpers_spec.name] = helpers
_helpers_spec.loader.exec_module(helpers)

compute_overall_status = helpers.compute_overall_status
build_attributes = helpers.build_attributes
derive_api_health_report = helpers.derive_api_health_report


class TestApiHealthOverallStatus:
    """Tests for compute_overall_status."""

    def test_empty_reports_returns_unknown(self):
        assert compute_overall_status({}) == "unknown"

    def test_single_ok_returns_ok(self):
        assert compute_overall_status({"open_meteo": {"status": "ok"}}) == "ok"

    def test_failed_overrides_ok(self):
        reports = {
            "open_meteo": {"status": "ok"},
            "alphaess": {"status": "failed"},
        }
        assert compute_overall_status(reports) == "failed"

    def test_degraded_overrides_ok(self):
        reports = {
            "open_meteo": {"status": "ok"},
            "alphaess": {"status": "degraded"},
        }
        assert compute_overall_status(reports) == "degraded"

    def test_unknown_overrides_ok(self):
        reports = {
            "open_meteo": {"status": "ok"},
            "alphaess": {"status": "unknown"},
        }
        assert compute_overall_status(reports) == "unknown"

    def test_failed_overrides_degraded(self):
        reports = {
            "open_meteo": {"status": "degraded"},
            "alphaess": {"status": "failed"},
        }
        assert compute_overall_status(reports) == "failed"

    def test_missing_status_defaults_to_unknown(self):
        reports = {"open_meteo": {"timestamp": "2026-06-26T10:00:00"}}
        assert compute_overall_status(reports) == "unknown"


class TestApiHealthAttributes:
    """Tests for build_attributes."""

    def test_empty_reports_returns_empty_attributes(self):
        assert build_attributes({}) == {}

    def test_ok_report_includes_last_success(self):
        reports = {
            "open_meteo": {
                "status": "ok",
                "timestamp": "2026-06-26T10:00:00",
                "error": None,
                "details": "forecast fetched",
            }
        }
        attrs = build_attributes(reports)
        assert attrs["open_meteo_status"] == "ok"
        assert attrs["open_meteo_last_call"] == "2026-06-26T10:00:00"
        assert attrs["open_meteo_last_success"] == "2026-06-26T10:00:00"
        assert attrs["open_meteo_error"] is None
        assert attrs["open_meteo_details"] == "forecast fetched"

    def test_failed_report_omits_last_success(self):
        reports = {
            "open_meteo": {
                "status": "failed",
                "timestamp": "2026-06-26T10:00:00",
                "error": "timeout",
                "details": "archive fetch failed",
            }
        }
        attrs = build_attributes(reports)
        assert attrs["open_meteo_status"] == "failed"
        assert attrs["open_meteo_last_call"] == "2026-06-26T10:00:00"
        assert attrs["open_meteo_last_success"] is None
        assert attrs["open_meteo_error"] == "timeout"
        assert attrs["open_meteo_details"] == "archive fetch failed"

    def test_source_names_are_normalized(self):
        reports = {
            "Open-Meteo": {"status": "ok", "timestamp": "2026-06-26T10:00:00"},
            "alpha.ess": {"status": "ok", "timestamp": "2026-06-26T10:00:00"},
        }
        attrs = build_attributes(reports)
        assert "open_meteo_status" in attrs
        assert "alpha_ess_status" in attrs


class TestDeriveApiHealthReport:
    """Tests for derive_api_health_report."""

    def test_successful_live_call_is_ok(self):
        result = SimpleNamespace(warnings=[], cache_hits=0, cache_misses=1)
        report = derive_api_health_report("pv_forecast.open_meteo_forecast", result, timestamp="ts1")
        assert report["source"] == "pv_forecast.open_meteo_forecast"
        assert report["status"] == "ok"
        assert report["timestamp"] == "ts1"
        assert report["error"] is None
        assert "live" in report["details"]

    def test_cache_hit_is_ok(self):
        result = SimpleNamespace(warnings=[], cache_hits=1, cache_misses=0)
        report = derive_api_health_report("pv_forecast.open_meteo_forecast", result)
        assert report["status"] == "ok"
        assert "cache" in report["details"]

    def test_fetch_failure_is_failed(self):
        result = SimpleNamespace(
            warnings=["weather_forecast_fetch_failed"],
            cache_hits=0,
            cache_misses=1,
        )
        report = derive_api_health_report("pv_forecast.open_meteo_forecast", result)
        assert report["status"] == "failed"
        assert "weather_forecast_fetch_failed" in report["error"]

    def test_stale_cache_fallback_is_degraded(self):
        result = SimpleNamespace(
            warnings=["weather_archive_api_unavailable_using_stale"],
            cache_hits=1,
            cache_misses=0,
        )
        report = derive_api_health_report("pv_forecast.open_meteo_archive", result)
        assert report["status"] == "degraded"

    def test_gti_fallback_is_degraded(self):
        result = SimpleNamespace(
            warnings=["string_gti_fallback_inverter1"],
            cache_hits=0,
            cache_misses=1,
        )
        report = derive_api_health_report("pv_forecast.open_meteo_forecast", result)
        assert report["status"] == "degraded"

    def test_unknown_warning_is_degraded(self):
        result = SimpleNamespace(warnings=["something_unexpected"], cache_hits=0, cache_misses=1)
        report = derive_api_health_report("hcf.open_meteo_forecast", result)
        assert report["status"] == "degraded"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
