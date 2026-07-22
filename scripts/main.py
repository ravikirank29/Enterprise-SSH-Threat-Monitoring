"""
Main entry point for the Splunk Threat Intelligence project.

This script orchestrates the complete enrichment workflow:

1. Retrieve failed SSH source IPs from Splunk.
2. Query AbuseIPDB for reputation information.
3. Generate a Splunk CSV lookup.
4. Copy the lookup into the Splunk application.
"""

import shutil
from ipaddress import ip_address
from pathlib import Path

from abuseipdb import check_ip
from lookup_builder import (
    append_to_lookup,
    initialize_lookup,
)
from splunk_client import get_unique_failed_ips

# ---------------------------------------------------------------------
# File Paths
# ---------------------------------------------------------------------

LOOKUP_FILE = (
    Path(__file__).resolve().parent.parent
    / "lookups"
    / "abuseipdb_lookup.csv"
)

SPLUNK_LOOKUP_DIR = Path(
    "/opt/splunk/etc/apps/Threat_Intelligence/lookups"
)

# ---------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------


def copy_lookup() -> None:
    """
    Copy the generated lookup file into the Splunk application lookup directory.
    """

    print("\n[*] Copying lookup to Splunk...")

    try:
        SPLUNK_LOOKUP_DIR.mkdir(parents=True, exist_ok=True)

        destination = SPLUNK_LOOKUP_DIR / LOOKUP_FILE.name

        shutil.copy2(LOOKUP_FILE, destination)

        print(f"[✓] Lookup copied successfully -> {destination}")

    except PermissionError:
        print("\n[!] Permission denied.")
        print("Run the following command manually:\n")
        print(
            "sudo cp lookups/abuseipdb_lookup.csv "
            "/opt/splunk/etc/apps/Threat_Intelligence/lookups/"
        )

    except Exception as exc:
        print(f"[ERROR] Failed to copy lookup: {exc}")


# ---------------------------------------------------------------------
# Main Workflow
# ---------------------------------------------------------------------


def main() -> None:
    """
    Execute the complete threat intelligence enrichment workflow.
    """

    print("=" * 70)
    print(" Enterprise SSH Threat Intelligence Enrichment ")
    print("=" * 70)

    initialize_lookup()

    print("\n[*] Retrieving unique failed SSH source IPs from Splunk...\n")

    ips = get_unique_failed_ips()

    print(f"[✓] Found {len(ips)} unique IP(s).\n")

    processed = 0
    skipped = 0
    failed = 0

    for ip in ips:

        print(f"[*] Processing {ip}")

        try:

            if ip_address(ip).is_private:
                print("    ↳ Private IP detected. Skipping.")
                skipped += 1
                continue

            response = check_ip(ip)

            append_to_lookup(response)

            print("    ↳ Threat intelligence added.")

            processed += 1

        except Exception as exc:
            failed += 1
            print(f"    [ERROR] {ip}: {exc}")

    copy_lookup()

    print("\n" + "=" * 70)
    print(" Threat Intelligence Enrichment Summary ")
    print("=" * 70)
    print(f"Total IPs Retrieved : {len(ips)}")
    print(f"Processed           : {processed}")
    print(f"Skipped (Private)   : {skipped}")
    print(f"Failed              : {failed}")
    print("=" * 70)

    if failed:
        print(
            "[!] Some IP addresses could not be enriched. "
            "Review the error messages above."
        )
    else:
        print("[✓] All public IPs enriched successfully.")

    print("=" * 70)


__all__ = [
    "main",
]


if __name__ == "__main__":
    main()