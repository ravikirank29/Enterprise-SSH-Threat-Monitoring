"""
Tests for configuration loading.
"""

from config import (
    API_KEY,
    SPLUNK_HOST,
    SPLUNK_PASSWORD,
    SPLUNK_PORT,
    SPLUNK_USERNAME,
)


def test_api_key_exists():
    assert API_KEY is not None
    assert len(API_KEY) > 0


def test_splunk_host():
    assert SPLUNK_HOST is not None


def test_splunk_port():
    assert isinstance(SPLUNK_PORT, int)


def test_splunk_username():
    assert SPLUNK_USERNAME is not None


def test_splunk_password():
    assert SPLUNK_PASSWORD is not None
