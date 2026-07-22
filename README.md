# Enterprise SSH Threat Monitoring & Detection Engineering with Splunk

<p align="center">
  <img src="images/banner.png" alt="Enterprise SOC Banner" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazonaws&logoColor=white" alt="AWS">
  <img src="https://img.shields.io/badge/Splunk-Enterprise-65A637?logo=splunk&logoColor=white" alt="Splunk">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Ubuntu-24.04-E95420?logo=ubuntu&logoColor=white" alt="Ubuntu">
  <img src="https://img.shields.io/badge/Kali-Linux-557C94?logo=kalilinux&logoColor=white" alt="Kali Linux">
  <img src="https://img.shields.io/badge/MITRE-ATT%26CK-8B0000" alt="MITRE ATT&CK">
  <img src="https://img.shields.io/badge/Detection-Engineering-1f6feb" alt="Detection Engineering">
  <img src="https://img.shields.io/badge/License-MIT-2ea44f" alt="License">
</p>

<p align="center"><b>Enterprise SOC Project · Splunk SIEM · Detection Engineering · Threat Intelligence · Python Automation</b></p>

<p align="center">
  <a href="#-executive-overview">Overview</a> ·
  <a href="#-solution-architecture">Architecture</a> ·
  <a href="#-detection-catalog">Detections</a> ·
  <a href="#-python-automation">Automation</a> ·
  <a href="#-soc-dashboards">Dashboards</a> ·
  <a href="#-skills-demonstrated">Skills</a> ·
  <a href="#-author">Author</a>
</p>

---

## 📖 Executive Overview

Security Operations Centers process millions of events daily — detecting malicious activity takes more than log collection; it requires correlation, enrichment, automation, and actionable intelligence.

This project shows how a modern SOC detects, investigates, and prioritizes SSH authentication attacks using **Splunk Enterprise**, **Python automation**, and **threat intelligence enrichment**, all inside an AWS-hosted lab.

The environment continuously collects Linux authentication logs from an Ubuntu server, forwards them into Splunk, detects suspicious SSH activity with custom SPL analytics, enriches attacker IPs with AbuseIPDB reputation data, and surfaces investigation-ready dashboards for analysts.

The focus throughout is **detection engineering** — building analytics that turn raw authentication logs into meaningful, MITRE-aligned detections rather than relying on out-of-the-box rules.

**This project demonstrates:**

| | | |
|---|---|---|
| Centralized log collection | Enterprise SIEM deployment | Detection engineering |
| Threat intelligence enrichment | Python automation | Splunk SDK integration |
| MITRE ATT&CK mapping | Automated lookup generation | SOC dashboards & alerting |

The end goal is to simulate how enterprise security teams identify, investigate, and prioritize SSH brute-force attacks while reducing manual analysis through automation.

---

## 🎯 Objectives

- Deploy enterprise infrastructure in AWS and configure Splunk Enterprise + Universal Forwarder
- Collect Linux authentication logs and simulate SSH attacks from Kali Linux
- Develop custom SPL detections for brute force, password spraying, and targeted account attacks
- Detect successful logins that follow repeated failures
- Enrich attacker IPs using threat intelligence, automated end-to-end with Python
- Build investigation dashboards, scheduled alerts, and MITRE ATT&CK-mapped detections
- Demonstrate a complete SOC investigation workflow, start to finish

---

## ⭐ Highlights

| Capability | Description |
|---|---|
| ☁️ **AWS Infrastructure** | Amazon EC2 deployment |
| 📊 **SIEM** | Splunk Enterprise |
| 📥 **Log Collection** | Splunk Universal Forwarder |
| 🔍 **Detection Engineering** | Custom SPL analytics |
| 🌍 **Threat Intelligence** | AbuseIPDB REST API |
| 🐍 **Automation** | Python + Splunk SDK |
| 📄 **Lookup Tables** | Automated CSV generation |
| 🚨 **Alerting** | Scheduled Splunk searches |
| 📈 **Dashboards** | SOC investigation dashboards |
| 🛡️ **Framework** | MITRE ATT&CK |

---

## 🏆 Key Features

**Security Monitoring** — Linux authentication and SSH login monitoring, failed/successful auth detection, source IP tracking, user account monitoring.

**Detection Engineering** — Custom SPL detections for brute force, password spraying, high-volume failures, post-failure successful logins, targeted accounts, and high-confidence malicious IPs.

**Threat Intelligence** — AbuseIPDB queries for IP reputation, abuse confidence scores, ISP and geolocation data, and historical abuse reports — enriching Splunk searches automatically.

**Automation** — Python handles Splunk SDK searches, IP extraction, AbuseIPDB requests, JSON parsing, lookup generation, CSV updates, and error handling end-to-end.

---

## 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Cloud | AWS EC2 |
| Operating System | Ubuntu Server 24.04 |
| SIEM | Splunk Enterprise |
| Log Forwarding | Splunk Universal Forwarder |
| Attack Platform | Kali Linux |
| Language | Python 3 |
| Detection | SPL |
| Threat Intelligence | AbuseIPDB |
| API | REST |
| Automation | Splunk SDK |
| Framework | MITRE ATT&CK |
| Version Control | Git |

---

## 📂 Repository Structure

```text
splunk-threat-intel/
│
├── docs/
│   ├── architecture/
│   ├── dashboards/
│   ├── detections/
│   ├── setup/
│   └── screenshots/
│
├── images/
│   ├── architecture.png
│   ├── dashboard.png
│   ├── detection.png
│   └── banner.png
│
├── lookups/
│   └── abuseipdb_lookup.csv
│
├── scripts/
│   ├── abuseipdb.py
│   ├── lookup_builder.py
│   └── main.py
│
├── searches/
│   ├── DET-001.spl
│   ├── DET-002.spl
│   ├── DET-003.spl
│   ├── DET-004.spl
│   ├── DET-005.spl
│   ├── DET-006.spl
│   └── DET-007.spl
│
├── LICENSE
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🏗️ Solution Architecture

This project simulates a production-inspired SOC pipeline: it collects Linux authentication events, detects SSH-based attacks, enriches suspicious IPs with external threat intelligence, and delivers actionable insight through Splunk dashboards — combining telemetry, automation, and threat intelligence to improve detection and investigation.

The architecture has six major components:

1. AWS Cloud Infrastructure
2. Ubuntu Linux Endpoint
3. Splunk Universal Forwarder
4. Splunk Enterprise
5. Python Automation Engine
6. AbuseIPDB Threat Intelligence Platform

Together, these transform raw authentication logs into enriched security detections.

### Architecture Diagram

```text
                    ┌────────────────────────────┐
                    │        Kali Linux          │
                    │  SSH Brute Force Attacks   │
                    └─────────────┬──────────────┘
                                  │
                                  ▼
                 ┌────────────────────────────────┐
                 │      Ubuntu Linux Server       │
                 │  OpenSSH · auth.log             │
                 │  Authentication Events         │
                 └──────────────┬─────────────────┘
                                │
                                ▼
               ┌──────────────────────────────────┐
               │ Splunk Universal Forwarder (UF)  │
               │ Monitors auth.log · Forwards      │
               └──────────────┬───────────────────┘
                              │
                              ▼
              ┌───────────────────────────────────┐
              │      Splunk Enterprise SIEM       │
              │  Indexing · Parsing · Searching   │
              │  Detection Engineering            │
              │  Dashboards · Alerts              │
              └──────────────┬────────────────────┘
                             │  Splunk SDK
                             ▼
          ┌─────────────────────────────────────┐
          │     Python Automation Scripts       │
          │  Extract suspicious IPs             │
          │  Query AbuseIPDB · Validate         │
          │  Generate CSV lookup                │
          └──────────────┬──────────────────────┘
                         │
                         ▼
            ┌─────────────────────────────┐
            │    AbuseIPDB REST API       │
            │  Reputation · ISP           │
            │  Country · Abuse Reports    │
            └─────────────┬───────────────┘
                          │
                          ▼
               Splunk Lookup Table (CSV)
                          │
                          ▼
              Detection Enrichment
                          │
                          ▼
             SOC Dashboards & Alerts
```

---

## 🔄 End-to-End Data Flow

<p align="center">
  <img src="screenshots/threat-intelligence/25-project-workflow.png" width="100%">
</p>

| Step | Stage | Description |
|---|---|---|
| 1 | **Attack Simulation** | Kali Linux performs SSH authentication attempts against the Ubuntu server, generating both legitimate and malicious events in `/var/log/auth.log`. |
| 2 | **Log Collection** | Splunk Universal Forwarder continuously monitors `auth.log` and securely forwards new events to Splunk Enterprise. |
| 3 | **Event Indexing** | Splunk parses, timestamps, classifies, and indexes each event, making it searchable via SPL. |
| 4 | **Detection Engineering** | Custom SPL searches flag brute force, password spraying, targeted accounts, and post-failure successful logins. |
| 5 | **Threat Intel Automation** | Python queries Splunk for attacker IPs, deduplicates them, queries AbuseIPDB, and regenerates the CSV lookup. |
| 6 | **Threat Intel Correlation** | Splunk joins authentication events with the lookup table, adding abuse score, country, ISP, domain, and report history. |
| 7 | **SOC Investigation** | Analysts review enriched events in dashboards — source IP, username, failure counts, and reputation — to prioritize response. |

---

## ☁️ AWS Infrastructure

| Component | Purpose |
|---|---|
| Amazon EC2 | Hosts the Ubuntu server |
| Security Groups | Controls inbound SSH access |
| Elastic IP | Public accessibility |
| Ubuntu Server | Authentication target |
| Splunk Enterprise | Centralized SIEM |
| Splunk Universal Forwarder | Secure log forwarding |

**Why AWS?** Cloud-native infrastructure, elastic scalability, secure networking, and public accessibility for testing make AWS a closer match to real enterprise environments than a local VM lab.

---

## 📥 Log Collection Pipeline

```text
Ubuntu auth.log → Splunk Universal Forwarder → Splunk Enterprise
   → Index: linux_auth → Detection Searches → Threat Intel Enrichment
   → Dashboards → Alerts → SOC Investigation
```

The **Universal Forwarder** handles telemetry collection — monitoring logs and forwarding them reliably with minimal CPU and memory overhead. **Splunk Enterprise** then owns everything downstream: indexing, normalization, search, detection engineering, dashboards, alerting, and threat intel correlation.

---

## ⚔️ Attack Simulation

Controlled SSH attacks launched from Kali Linux validate the detection pipeline, covering:

- SSH brute-force attempts
- Invalid username attempts
- Password spraying
- Multiple failed logins
- Successful login after repeated failures

These scenarios generate realistic telemetry that exercises every custom SPL detection, from collection through investigation.

---

## 🎯 Detection Engineering

Rather than relying on Splunk's built-in detections, every analytic here was custom-built using SPL, statistical aggregation, event correlation, threshold-based logic, threat intel enrichment, and MITRE ATT&CK mapping — designed to cut false positives while giving analysts real investigative context.

### Detection Catalog

| ID | Detection | MITRE Technique | Severity |
|---|---|---|---|
| DET-001 | SSH Brute Force Detection | T1110 | High |
| DET-002 | Password Spraying Detection | T1110.003 | High |
| DET-003 | High Authentication Failure Volume | T1110 | Medium |
| DET-004 | Successful Login After Multiple Failures | T1110 | Critical |
| DET-005 | Targeted Account Detection | T1110 | Medium |
| DET-006 | Threat Intelligence Match | T1583 / T1584 | High |
| DET-007 | Brute Force + Threat Intel Correlation | T1110 | Critical |

<details>
<summary><b>DET-001 — SSH Brute Force Detection</b></summary>

**Objective:** Identify source IPs generating excessive failed SSH login attempts against one or more accounts.

**Detection Logic:** Monitor auth logs → count failed SSH logins → aggregate by source IP → trigger on threshold breach.

**MITRE ATT&CK:** Credential Access — T1110 (Brute Force)

**Investigation Value:** Quickly surfaces external hosts running credential attacks against Linux systems.
</details>

<details>
<summary><b>DET-002 — Password Spraying Detection</b></summary>

**Objective:** Detect a single source IP attempting authentication against multiple accounts with a limited password set.

**Detection Logic:** Group failed logins by source IP → count unique usernames → alert when one IP targets multiple accounts.

**MITRE ATT&CK:** Credential Access — T1110.003 (Password Spraying)

**Investigation Value:** Password spraying often evades traditional brute-force thresholds and is common in enterprise environments.
</details>

<details>
<summary><b>DET-003 — High Authentication Failure Volume</b></summary>

**Objective:** Identify systems seeing unusually large numbers of failed authentication events.

**Detection Logic:** Aggregate failures → monitor for spikes → flag abnormal login activity.

**MITRE ATT&CK:** Credential Access — T1110

**Investigation Value:** Surfaces attack campaigns or operational issues affecting authentication services.
</details>

<details>
<summary><b>DET-004 — Successful Login After Multiple Failures</b></summary>

**Objective:** Detect successful SSH logins immediately following repeated failed attempts.

**Detection Logic:** Track failed logins → identify a subsequent success → correlate by source IP and username.

**MITRE ATT&CK:** Credential Access — T1110

**Investigation Value:** A success following repeated failures may indicate a compromised credential — flagged for immediate analyst review.
</details>

<details>
<summary><b>DET-005 — Targeted Account Detection</b></summary>

**Objective:** Identify accounts receiving an abnormal number of authentication attempts.

**Detection Logic:** Aggregate by username → rank targeted accounts → identify repeated targeting.

**MITRE ATT&CK:** Credential Access — T1110

**Investigation Value:** Highlights privileged or high-value accounts that may need additional monitoring.
</details>

<details>
<summary><b>DET-006 — Threat Intelligence Match</b></summary>

**Objective:** Identify authentication attempts from IPs with a known malicious reputation.

**Detection Logic:** Extract source IP → look up against AbuseIPDB → enrich with reputation data → prioritize malicious infrastructure.

**MITRE ATT&CK:** Resource Development

**Investigation Value:** Cuts investigation time by immediately flagging known malicious infrastructure.
</details>

<details>
<summary><b>DET-007 — SSH Brute Force + Threat Intelligence Correlation</b></summary>

**Objective:** Correlate brute-force behavior with external threat intelligence to surface high-confidence attacks, combining behavioral analytics with reputation scoring to cut false positives.

**Detection Workflow:**
```
Authentication Events → Extract Source IP → Count Failed Logins
   → Threat Intel Lookup → MITRE ATT&CK Mapping
   → Dynamic Severity Assignment → SOC Alert
```

**Detection Criteria:** An alert fires when the failed login count exceeds threshold, the source IP exists in the threat intel lookup, and the abuse confidence score exceeds the configured threshold.

**Dynamic Severity Model:**

| Conditions | Severity |
|---|---|
| Score ≥ 100 & Failures ≥ 200 | Critical |
| Score ≥ 100 & Failures ≥ 50 | High |
| Score ≥ 90 | Medium |
| Otherwise | Low |

**MITRE ATT&CK:** Credential Access — T1110 (Brute Force)

**Analyst Context:** Each alert includes source IP, failed login count, abuse confidence score, country, ISP, domain, usage type, abuse report count, first/last seen, and last abuse report — so analysts can prioritize without manually querying external sources.
</details>

---

## 🌍 Threat Intelligence Integration

For every suspicious source IP, the enrichment process retrieves an abuse confidence score, country code and name, ISP, domain, usage type, total abuse reports, and last-reported date from **AbuseIPDB**. The results are stored in a Splunk CSV lookup and joined automatically with authentication events during SPL searches — letting analysts distinguish generic auth failures from attacks tied to infrastructure with a known history of abuse.

---

## 🐍 Python Automation

Manual threat intel enrichment doesn't scale in a modern SOC, so a Python pipeline automates the entire workflow end to end.

| Script | Purpose |
|---|---|
| `main.py` | Orchestrates the complete automation workflow |
| `abuseipdb.py` | Communicates with the AbuseIPDB REST API |
| `lookup_builder.py` | Generates Splunk CSV lookup tables |

**Workflow:**

1. Run a Splunk search via the Splunk SDK
2. Retrieve and deduplicate source IPs from failed SSH events
3. Query the AbuseIPDB REST API for each IP
4. Validate responses and handle errors, timeouts, and connection failures
5. Parse JSON and generate an updated CSV lookup
6. Store the lookup in the Splunk lookup directory for future enrichment

### Splunk SDK Integration

The Splunk Python SDK executes SPL searches, retrieves results, and extracts suspicious source IPs directly against live indexed data — no manual exports required.

### Robust API Handling

Defensive programming keeps the pipeline reliable: HTTP status and JSON validation, request timeouts, connection/exception handling, missing-field checks, and rate-limit awareness so enrichment keeps running through temporary API issues.

### Generated Lookup Schema

| Field | Description |
|---|---|
| `src_ip` | Source IP address |
| `abuseConfidenceScore` | Abuse confidence rating |
| `countryCode` | Country code |
| `countryName` | Country name |
| `isp` | Internet Service Provider |
| `domain` | Associated domain |
| `usageType` | Network usage classification |
| `totalReports` | Number of abuse reports |
| `lastReportedAt` | Last reported abuse timestamp |

This lookup is consumed directly via the `lookup` command, enriching events in real time without repeated API calls.

---

## 📊 SOC Dashboards

Custom dashboards give analysts immediate operational visibility, including:

- Failed and successful SSH authentication attempts
- Top attacking IP addresses and most-targeted accounts
- Authentication activity over time
- Threat intelligence matches and abuse confidence score distribution
- Country of origin for attacker IPs and high-severity detections

## 🚨 Scheduled Alerting

Scheduled searches continuously evaluate authentication events against the detection catalog above, generating alerts for brute force, password spraying, high-volume failures, post-failure successes, and threat intel matches — with severity set by the DET-007 dynamic model.

---

## 🔍 SOC Investigation Workflow

| Step | Action |
|---|---|
| 1. Alert Generation | A scheduled SPL search flags suspicious behavior and fires an alert |
| 2. Event Review | Analyst reviews source IP, username, auth status, failure count, timestamps |
| 3. Threat Intel Enrichment | Source IP is enriched automatically via the AbuseIPDB lookup |
| 4. Risk Assessment | Analyst weighs behavior, reputation score, history, and account targeting |
| 5. Investigation | Analyst prioritizes, investigates, searches related activity, and escalates if needed |

---

## 📷 Project Gallery

| Architecture | Splunk Dashboard |
|---|---|
| ![Architecture](screenshots/architecture/01-architecture.png) | ![Dashboard](screenshots/dashboard/09-dashboard.png) |

| Threat Intel Enrichment | Python Automation |
|---|---|
| ![Enrichment](screenshots/threat-intelligence/21-threat-intelligence-enrichment.png) | ![Automation](screenshots/threat-intelligence/20-python-automation.png) |

**Generated Lookup**

<p align="center"><img src="screenshots/threat-intelligence/23-abuseipdb-lookup.csv.png" width="100%"></p>

---

## 💡 Lessons Learned

- **Security Monitoring** — designing centralized log pipelines and understanding authentication telemetry
- **Detection Engineering** — writing production-style SPL, threshold-based detections, false-positive reduction, and MITRE mapping
- **Threat Intelligence** — integrating REST APIs into SIEM workflows to sharpen analyst context
- **Python Automation** — parsing JSON, building resilient API integrations, and generating Splunk-compatible lookups
- **Cloud Security** — deploying and operating cloud-hosted monitoring infrastructure on AWS

---

## 🚀 Future Enhancements

| Area | Ideas |
|---|---|
| Detection Engineering | Geo-anomaly detection, impossible travel, credential stuffing, UBA, time-based anomalies |
| Threat Intelligence | VirusTotal, AlienVault OTX, GreyNoise, MISP, URLHaus integrations |
| Automation | Scheduled enrichment jobs, IOC expiration handling, multi-source correlation |
| SOC Enhancements | Risk-based alerting, SOAR integration, case management, Slack/email notifications |
| Infrastructure | Multi-endpoint monitoring, Windows/Sysmon, Active Directory, container logs |

---

## 🏅 Skills Demonstrated

| Category | Skills |
|---|---|
| SIEM & Monitoring | Splunk Enterprise, SPL, log collection, event correlation, dashboards, alerting |
| Detection Engineering | Custom detections, SSH brute force & spraying detection, MITRE ATT&CK mapping, dynamic severity |
| Threat Intelligence | AbuseIPDB, IOC correlation, reputation scoring, REST API integration |
| Programming & Automation | Python, Splunk SDK, JSON/CSV processing, exception handling |
| Cloud & Infrastructure | AWS, Ubuntu, Kali Linux, Splunk Universal Forwarder, SSH monitoring |

---

## 📄 License

Licensed under the **MIT License** — free to use, modify, and distribute in accordance with its terms.

---

## 👨‍💻 Author

**Ravi Kiran Kambhampati**
*Cybersecurity & Cloud Operations Graduate*

Focused on detection engineering, security operations, threat intelligence, cloud security, SIEM engineering, incident response, and security automation.

[LinkedIn](https://www.linkedin.com/in/ravikirankambhampati/) · [GitHub Repository](https://github.com/ravikirank29/Enterprise-SSH-Threat-Monitoring)

---

<p align="center">⭐ If this project was useful, consider starring the repository — it helps others find it and supports continued development.</p>

<p align="center"><b>Built for Blue Teaming, Detection Engineering, and Continuous Learning.</b></p>
