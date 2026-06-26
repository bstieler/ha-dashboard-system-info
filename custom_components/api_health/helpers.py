"""Pure logic for the API Health component.

This module intentionally does not import Home Assistant, so it can be unit-tested
in any Python environment.
"""

from __future__ import annotations

from typing import Any

# Warnings that indicate the API call itself failed.
FAILURE_WARNING_CODES = {
    "weather_archive_fetch_failed",
    "weather_forecast_fetch_failed",
    "string_gti_fetch_failed",
}

# Warnings that indicate a successful fallback (stale cache, degraded data).
DEGRADED_WARNING_PREFIXES = (
    "weather_archive_api_unavailable_using_stale",
    "weather_archive_api_unavailable_empty",
    "string_gti_fallback",
)


def compute_overall_status(reports: dict[str, dict[str, Any]]) -> str:
    """Return the worst status across all reported sources.

    Priority (high to low): failed > degraded > unknown > ok.
    An empty report set is treated as ``unknown``.
    """
    if not reports:
        return "unknown"
    statuses = [r.get("status", "unknown") for r in reports.values()]
    if "failed" in statuses:
        return "failed"
    if "degraded" in statuses:
        return "degraded"
    if "unknown" in statuses:
        return "unknown"
    if all(status == "ok" for status in statuses):
        return "ok"
    return "unknown"


def derive_api_health_report(
    source: str,
    result: Any,
    *,
    timestamp: str | None = None,
) -> dict[str, Any]:
    """Derive an api_health.report payload from a weather fetch result.

    ``result`` is expected to expose at least ``warnings`` (list[str]).
    It may provide ``cache_hits``/``cache_misses`` (PV adapter) or
    ``cache_hit`` (HCF adapter); missing counters default to zero.
    """
    warnings = list(getattr(result, "warnings", []) or [])
    cache_hits = int(getattr(result, "cache_hits", 0) or 0)
    cache_misses = int(getattr(result, "cache_misses", 0) or 0)
    if cache_hits == 0 and cache_misses == 0:
        # Fall back to the boolean flag used by the house-consumption adapter.
        if getattr(result, "cache_hit", False):
            cache_hits = 1
        else:
            cache_misses = 1

    if cache_hits > 0 and cache_misses == 0:
        source_type = "cache"
    elif cache_misses > 0 and cache_hits == 0:
        source_type = "live"
    else:
        source_type = "mixed"

    has_failure = any(code in warnings for code in FAILURE_WARNING_CODES)
    has_fallback = any(
        any(str(code).startswith(prefix) for prefix in DEGRADED_WARNING_PREFIXES)
        for code in warnings
    )

    if has_failure:
        status = "failed"
    elif has_fallback or warnings:
        status = "degraded"
    else:
        status = "ok"

    error = ", ".join(warnings) if warnings else None
    details = f"source={source_type}, cache_hits={cache_hits}, cache_misses={cache_misses}"

    return {
        "source": source,
        "status": status,
        "timestamp": timestamp,
        "error": error,
        "details": details,
    }


def _safe_source_key(source: str) -> str:
    """Normalize a source name for use in entity attributes."""
    return source.lower().strip().replace("-", "_").replace(".", "_").replace(" ", "_")


def build_attributes(reports: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """Build extra_state_attributes from the current reports.

    For each source ``<name>`` the following attributes are emitted:
    - ``<name>_status``
    - ``<name>_last_call``
    - ``<name>_last_success`` (only when the latest report status is ``ok``)
    - ``<name>_error``
    - ``<name>_details``
    """
    attrs: dict[str, Any] = {}
    for source, report in reports.items():
        safe = _safe_source_key(source)
        attrs[f"{safe}_status"] = report.get("status")
        attrs[f"{safe}_last_call"] = report.get("timestamp")
        attrs[f"{safe}_last_success"] = (
            report.get("timestamp") if report.get("status") == "ok" else None
        )
        attrs[f"{safe}_error"] = report.get("error")
        attrs[f"{safe}_details"] = report.get("details")
    return attrs
