# Architecture

The project consists of three systems.

- Kali Linux
- Ubuntu Server
- Splunk Enterprise

Authentication logs are collected from Ubuntu using the Splunk Universal Forwarder and indexed in Splunk Enterprise.

Hydra generates brute-force attempts against the SSH service.

Splunk dashboards and alerts detect malicious activity.