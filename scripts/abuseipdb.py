"""
AbuseIPDB client for the Splunk Threat Intelligence project.

This module queries the AbuseIPDB REST API to retrieve reputation
information for IP addresses used during threat intelligence enrichment.
"""

from typing import Any

import requests
from requests.exceptions import (
    ConnectionError,
    HTTPError,
    RequestException,
    Timeout,
)

from config import API_KEY

# ---------------------------------------------------------------------
# AbuseIPDB API Configuration
# ---------------------------------------------------------------------

API_URL = "https://api.abuseipdb.com/api/v2/check"
TIMEOUT = 30

# ---------------------------------------------------------------------
# Public Functions
# ---------------------------------------------------------------------


def check_ip(ip_address: str) -> dict[str, Any]:
    """
    Query AbuseIPDB for threat intelligence on an IP address.

    Args:
        ip_address: IPv4 or IPv6 address.

    Returns:
        Dictionary containing the AbuseIPDB API response.

    Raises:
        RuntimeError:
            If the request fails, the API returns an error,
            or the response is invalid.
    """

    headers = {
        "Key": API_KEY,
        "Accept": "application/json",
    }

    params = {
        "ipAddress": ip_address,
        "maxAgeInDays": 90,
        "verbose": True,
    }

    try:
        response = requests.get(
            API_URL,
            headers=headers,
            params=params,
            timeout=TIMEOUT,
        )

        response.raise_for_status()

        payload = response.json()

        if not payload.get("data"):
            raise RuntimeError(
                f"Unexpected API response for {ip_address}: {payload}"
            )

        return payload

    except Timeout as exc:
        raise RuntimeError(
            f"Request timed out while querying AbuseIPDB for {ip_address}."
        ) from exc

    except ConnectionError as exc:
        raise RuntimeError(
            f"Unable to connect to AbuseIPDB while querying {ip_address}."
        ) from exc

    except HTTPError as exc:
        status = response.status_code

        if status == 429:
            raise RuntimeError(
                "AbuseIPDB API rate limit exceeded. "
                f"Unable to process {ip_address}."
            ) from exc

        raise RuntimeError(
            f"HTTP {status} returned for {ip_address}: {response.text}"
        ) from exc

    except ValueError as exc:
        raise RuntimeError(
            f"Invalid JSON returned for {ip_address}."
        ) from exc

    except RequestException as exc:
        raise RuntimeError(
            f"Request failed for {ip_address}: {exc}"
        ) from exc


__all__ = [
    "check_ip",
]