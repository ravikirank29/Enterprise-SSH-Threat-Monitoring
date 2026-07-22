"""
CSV lookup builder for the Splunk Threat Intelligence project.

This module creates and maintains the Splunk lookup table used to enrich
authentication events with AbuseIPDB threat intelligence.
"""

import csv
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------
# Lookup Configuration
# ---------------------------------------------------------------------

LOOKUP_FILE = (
    Path(__file__).resolve().parent.parent
    / "lookups"
    / "abuseipdb_lookup.csv"
)

HEADERS = [
    "src_ip",
    "abuseConfidenceScore",
    "countryCode",
    "countryName",
    "isp",
    "domain",
    "usageType",
    "totalReports",
    "lastReportedAt",
]

# ---------------------------------------------------------------------
# Lookup File Management
# ---------------------------------------------------------------------


def initialize_lookup() -> None:
    """
    Create (or overwrite) the Splunk lookup file with the required headers.
    """

    LOOKUP_FILE.parent.mkdir(parents=True, exist_ok=True)

    with LOOKUP_FILE.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)


def append_to_lookup(response: dict[str, Any]) -> None:
    """
    Append a single AbuseIPDB response to the lookup CSV.

    Args:
        response: JSON response returned by the AbuseIPDB API.
    """

    data = response.get("data", {})

    row = [
        data.get("ipAddress", ""),
        data.get("abuseConfidenceScore", 0),
        data.get("countryCode", ""),
        data.get("countryName", ""),
        data.get("isp", ""),
        data.get("domain", ""),
        data.get("usageType", ""),
        data.get("totalReports", 0),
        data.get("lastReportedAt", ""),
    ]

    with LOOKUP_FILE.open(
        "a",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.writer(file)
        writer.writerow(row)


__all__ = [
    "initialize_lookup",
    "append_to_lookup",
]