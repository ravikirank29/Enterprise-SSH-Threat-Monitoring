# Lab Architecture

## Overview

The Enterprise SSH Threat Monitoring lab is designed to simulate a real-world Security Operations Center (SOC) environment for monitoring Linux authentication activity. The architecture consists of three primary systems: a Splunk Enterprise server, a Linux target server, and an attacker machine running Kali Linux.

The Ubuntu server continuously generates authentication logs during normal operation and attack simulations. These logs are forwarded to Splunk Enterprise using the Splunk Universal Forwarder, where they are indexed, analyzed, visualized, and used to generate alerts.

This architecture follows a centralized logging model commonly implemented in enterprise environments.

---

# Architecture Diagram

```text
                                Internet
                                    │
                                    │
                                    ▼
                         Kali Linux (Attacker)
                     Nmap • Hydra • SSH Client
                                    │
                                    │ SSH (Port 22)
                                    ▼
                    Ubuntu Linux Target Server
                   ─────────────────────────────
                     SSH Service (OpenSSH)
                     Authentication Logs
                     /var/log/auth.log
                     Splunk Universal Forwarder
                   ─────────────────────────────
                                    │
                         Forwarded Logs (TCP 9997)
                                    │
                                    ▼
                    Splunk Enterprise Server
                   ─────────────────────────────
                     Data Indexing
                     Search Processing
                     SPL Detection Rules
                     Dashboards
                     Scheduled Alerts
                   ─────────────────────────────
```

---

# Components

## 1. Splunk Enterprise Server

The Splunk Enterprise server acts as the centralized Security Information and Event Management (SIEM) platform.

### Responsibilities

- Receive authentication logs
- Index incoming events
- Execute SPL searches
- Correlate authentication events
- Visualize security data
- Generate alerts
- Support incident investigations

---

## 2. Ubuntu Linux Server

The Ubuntu server acts as the monitored endpoint.

### Responsibilities

- Host the SSH service
- Generate authentication logs
- Receive legitimate and malicious login attempts
- Forward logs to Splunk

### Important Log File

```
/var/log/auth.log
```

This file contains:

- Successful logins
- Failed logins
- Invalid usernames
- SSH daemon activity
- Authentication failures
- Session creation events

---

## 3. Splunk Universal Forwarder

The Splunk Universal Forwarder is installed on the Ubuntu server.

Its primary purpose is to securely forward log data to Splunk Enterprise.

### Responsibilities

- Monitor log files
- Forward new events in near real time
- Minimize system resource usage
- Maintain reliable event delivery

### Monitored Log

```
/var/log/auth.log
```

### Destination

```
Splunk Enterprise
TCP Port 9997
```

---

## 4. Kali Linux

Kali Linux represents the attacker machine.

It is used to simulate reconnaissance and brute-force attacks against the Ubuntu server.

### Tools Used

- Hydra
- Nmap
- OpenSSH Client

---

# Data Flow

The monitoring workflow follows the sequence below.

1. Kali Linux performs reconnaissance using Nmap.
2. Hydra launches SSH brute-force attacks.
3. Ubuntu records authentication events in `/var/log/auth.log`.
4. Splunk Universal Forwarder detects new log entries.
5. Events are forwarded to Splunk Enterprise.
6. Splunk indexes the events.
7. SPL detection rules analyze authentication activity.
8. Dashboards visualize security events.
9. Alerts notify analysts when brute-force thresholds are exceeded.

---

# Network Communication

| Source | Destination | Protocol | Port | Purpose |
|---------|-------------|----------|------|---------|
| Kali Linux | Ubuntu | SSH | 22 | Attack Simulation |
| Ubuntu | Splunk | TCP | 9997 | Log Forwarding |
| Analyst Browser | Splunk | HTTPS | 8000 | Web Interface |

---

# Security Controls

The lab includes several security controls to replicate enterprise monitoring practices.

### Centralized Logging

Authentication events are collected in one location to simplify monitoring and investigations.

### Continuous Monitoring

The Universal Forwarder continuously monitors the authentication log for new events.

### Detection Engineering

Custom SPL searches identify suspicious authentication patterns.

### Alerting

Splunk scheduled alerts notify analysts when brute-force attacks are detected.

---

# Design Decisions

## Why AWS?

AWS provides a flexible cloud environment for deploying enterprise infrastructure while closely resembling production environments.

---

## Why Ubuntu?

Ubuntu is widely used in enterprise Linux deployments and generates detailed SSH authentication logs suitable for security monitoring.

---

## Why Splunk Enterprise?

Splunk Enterprise provides powerful log indexing, search capabilities, visualization, and alerting features that are commonly used in enterprise Security Operations Centers.

---

## Why Splunk Universal Forwarder?

The Universal Forwarder is lightweight, efficient, and designed specifically for forwarding logs to Splunk with minimal resource consumption.

---

## Why Kali Linux?

Kali Linux includes industry-standard offensive security tools such as Hydra and Nmap, making it ideal for simulating realistic attack scenarios.

---

# Scalability

Although this project currently monitors a single Ubuntu server, the architecture can easily be expanded.

Future enhancements include:

- Multiple Linux servers
- Windows endpoints
- Sysmon integration
- Threat Intelligence feeds
- MITRE ATT&CK mapping
- Threat hunting dashboards
- Endpoint Detection and Response (EDR)
- SOAR integration

---

# Conclusion

This architecture demonstrates the core workflow of a modern Security Operations Center by combining centralized logging, attack simulation, detection engineering, dashboard visualization, and automated alerting.

While intentionally simplified for educational purposes, the design closely reflects enterprise security monitoring practices and provides a strong foundation for future enhancements.