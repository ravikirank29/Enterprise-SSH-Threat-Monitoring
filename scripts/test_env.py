"""
Environment variable tests.
"""

from config import (
    API_KEY,
    SPLUNK_HOST,
    SPLUNK_PASSWORD,
    SPLUNK_PORT,
    SPLUNK_USERNAME,
)


def test_environment_loaded():
    assert API_KEY
    assert SPLUNK_HOST
    assert SPLUNK_PORT
    assert SPLUNK_USERNAME
    assert SPLUNK_PASSWORD
