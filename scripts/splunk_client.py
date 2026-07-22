"""
Splunk client utilities for the Splunk Threat Intelligence project.

This module provides helper functions to connect to Splunk Enterprise
and retrieve unique source IP addresses from failed SSH authentication
events.
"""

import time

import splunklib.client as client
import splunklib.results as results

from config import (
    SPLUNK_HOST,
    SPLUNK_PASSWORD,
    SPLUNK_PORT,
    SPLUNK_USERNAME,
)

# Maximum time (in seconds) to wait for a Splunk search to complete.
SEARCH_TIMEOUT = 60


def connect():
    """
    Establish a connection to the Splunk Enterprise management API.

    Returns:
        splunklib.client.Service: Authenticated Splunk service object.

    Raises:
        RuntimeError: If the connection to Splunk fails.
    """
    try:
        return client.connect(
            host=SPLUNK_HOST,
            port=SPLUNK_PORT,
            username=SPLUNK_USERNAME,
            password=SPLUNK_PASSWORD,
        )
    except Exception as exc:
        raise RuntimeError(
            f"Failed to connect to Splunk: {exc}"
        ) from exc


def get_unique_failed_ips():
    """
    Retrieve unique source IP addresses from failed SSH authentication events.

    Returns:
        list[str]: Sorted list of unique source IP addresses.

    Raises:
        TimeoutError: If the search exceeds the configured timeout.
        RuntimeError: If the search cannot be completed.
    """
    service = connect()

    search_query = r"""
search index=linux_auth "Failed password"
| rex field=_raw "from (?<src_ip>\d{1,3}(?:\.\d{1,3}){3})"
| stats count by src_ip
"""

    try:
        job = service.jobs.create(search_query)

        start_time = time.time()

        while not job.is_done():
            if time.time() - start_time > SEARCH_TIMEOUT:
                raise TimeoutError(
                    f"Splunk search timed out after {SEARCH_TIMEOUT} seconds."
                )

            time.sleep(0.5)

        reader = results.JSONResultsReader(
            job.results(output_mode="json")
        )

        ips = []

        for item in reader:
            if isinstance(item, dict):
                src_ip = item.get("src_ip")
                if src_ip:
                    ips.append(src_ip)

        return sorted(set(ips))

    except Exception as exc:
        raise RuntimeError(
            f"Failed to retrieve failed SSH IP addresses: {exc}"
        ) from exc