"""
Integration test for Splunk.

Requires:
- Running Splunk Enterprise
- Port 8089 accessible
- Valid credentials in config/.env

Skipped automatically in GitHub Actions.
"""

import os

import pytest

if os.getenv("CI"):
    pytest.skip(
        "Skipping Splunk integration tests in CI.",
        allow_module_level=True,
    )

from splunk_client import get_unique_failed_ips


def test_get_unique_failed_ips():
    """Verify Splunk connection and returned data."""

    ips = get_unique_failed_ips()

    assert isinstance(ips, list)
