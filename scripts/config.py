"""
Configuration loader for the Splunk Threat Intelligence project.

This module loads environment variables from config/.env and exposes
configuration values used throughout the application.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# ---------------------------------------------------------------------
# Project paths
# ---------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / "config" / ".env"

# ---------------------------------------------------------------------
# Validate environment file
# ---------------------------------------------------------------------

if not ENV_FILE.exists():
    raise FileNotFoundError(
        f"Environment file not found: {ENV_FILE}"
    )

# Load environment variables
load_dotenv(ENV_FILE)

# ---------------------------------------------------------------------
# AbuseIPDB Configuration
# ---------------------------------------------------------------------

API_KEY = os.getenv("ABUSEIPDB_API_KEY")

# ---------------------------------------------------------------------
# Splunk Configuration
# ---------------------------------------------------------------------

SPLUNK_HOST = os.getenv("SPLUNK_HOST", "localhost")
SPLUNK_PORT = int(os.getenv("SPLUNK_PORT", "8089"))
SPLUNK_USERNAME = os.getenv("SPLUNK_USERNAME")
SPLUNK_PASSWORD = os.getenv("SPLUNK_PASSWORD")

# ---------------------------------------------------------------------
# Validate required configuration
# ---------------------------------------------------------------------

if not API_KEY:
    raise RuntimeError(
        "Missing required environment variable: "
        "ABUSEIPDB_API_KEY (expected in config/.env)"
    )

if not SPLUNK_USERNAME or not SPLUNK_PASSWORD:
    raise RuntimeError(
        "Missing required Splunk credentials "
        "(SPLUNK_USERNAME and/or SPLUNK_PASSWORD) "
        "in config/.env"
    )

# ---------------------------------------------------------------------
# Public exports
# ---------------------------------------------------------------------

__all__ = [
    "API_KEY",
    "SPLUNK_HOST",
    "SPLUNK_PORT",
    "SPLUNK_USERNAME",
    "SPLUNK_PASSWORD",
]