"""
Integration test for AbuseIPDB.

Requires:
- Valid ABUSEIPDB_API_KEY in config/.env
- Internet connection

Skipped automatically in GitHub Actions.
"""

import os

import pytest

if os.getenv("CI"):
    pytest.skip(
        "Skipping AbuseIPDB integration tests in CI.",
        allow_module_level=True,
    )

from abuseipdb import check_ip


def test_check_ip():
    """Verify AbuseIPDB API returns a valid response."""

    result = check_ip("8.8.8.8")

    assert result is not None
    assert isinstance(result, dict)
