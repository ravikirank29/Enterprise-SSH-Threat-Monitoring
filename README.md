# 🛡️ Enterprise SSH Threat Monitoring & Detection Engineering using Splunk

<p align="center">
  <img src="images/banner.png"
       alt="Enterprise SSH Threat Monitoring and Detection Engineering project banner"
       width="100%">
</p>


<p align="center">
  <img src="https://img.shields.io/badge/AWS-EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS EC2">
  <img src="https://img.shields.io/badge/Ubuntu-24.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" alt="Ubuntu 24.04">
  <img src="https://img.shields.io/badge/Splunk-Enterprise-000000?style=for-the-badge&logo=splunk&logoColor=65A637" alt="Splunk Enterprise">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B" alt="Python 3.12">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/MITRE-ATT%26CK-CB2027?style=for-the-badge" alt="MITRE ATT&CK">
  <img src="https://img.shields.io/badge/Threat_Intelligence-AbuseIPDB-2D7FF9?style=for-the-badge" alt="AbuseIPDB">
  <img src="https://img.shields.io/badge/Detection-Engineering-0A66C2?style=for-the-badge" alt="Detection Engineering">
  <img src="https://img.shields.io/badge/SOC-Operations-0052CC?style=for-the-badge" alt="SOC Operations">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Completed">
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="MIT License">
</p>

---

## 📚 Table of Contents

- [🛡️ Enterprise SSH Threat Monitoring \& Detection Engineering using Splunk](#️-enterprise-ssh-threat-monitoring--detection-engineering-using-splunk)
  - [📚 Table of Contents](#-table-of-contents)
- [📌 Executive Overview](#-executive-overview)
- [🎯 Project Objectives](#-project-objectives)
- [🚀 Key Features](#-key-features)
  - [🔍 Detection Engineering](#-detection-engineering)
  - [🌐 Threat Intelligence Integration](#-threat-intelligence-integration)
  - [🐍 Python Automation](#-python-automation)
- [🏗️ High-Level Architecture](#️-high-level-architecture)
- [🔄 End-to-End Workflow](#-end-to-end-workflow)
  - [](#)
- [🛠️ Technology Stack](#️-technology-stack)
- [📂 Repository Structure](#-repository-structure)
- [☁️ AWS Infrastructure](#️-aws-infrastructure)
  - [Infrastructure Components](#infrastructure-components)
- [⚙️ Splunk Enterprise Configuration](#️-splunk-enterprise-configuration)
  - [Configuration Summary](#configuration-summary)
- [📡 Log Collection Pipeline](#-log-collection-pipeline)
- [🖥️ Splunk Universal Forwarder](#️-splunk-universal-forwarder)
    - [Forwarded Logs](#forwarded-logs)
- [⚔️ Attack Simulation](#️-attack-simulation)
  - [Attack Scenarios](#attack-scenarios)
- [🎯 Detection Engineering](#-detection-engineering-1)
  - [DET-001 — SSH Brute-Force Detection](#det-001--ssh-brute-force-detection)
    - [Objective](#objective)
    - [SPL](#spl)
    - [Expected Result](#expected-result)
    - [MITRE ATT\&CK](#mitre-attck)
  - [DET-002 — Successful SSH Login Detection](#det-002--successful-ssh-login-detection)
    - [Objective](#objective-1)
    - [SPL](#spl-1)
    - [Expected Result](#expected-result-1)
    - [MITRE ATT\&CK](#mitre-attck-1)
  - [DET-003 — Failed Login Trend](#det-003--failed-login-trend)
    - [Objective](#objective-2)
    - [SPL](#spl-2)
    - [Expected Result](#expected-result-2)
  - [DET-004 — Top Attacking IP Addresses](#det-004--top-attacking-ip-addresses)
    - [Objective](#objective-3)
    - [SPL](#spl-3)
    - [Expected Result](#expected-result-3)
  - [DET-005 — Password Spray Detection](#det-005--password-spray-detection)
    - [Objective](#objective-4)
    - [SPL](#spl-4)
    - [MITRE ATT\&CK](#mitre-attck-2)
  - [DET-006 — High-Risk Source IP Detection](#det-006--high-risk-source-ip-detection)
    - [Objective](#objective-5)
    - [SPL](#spl-5)
    - [Expected Result](#expected-result-4)
  - [DET-007 — Authentication Dashboard Metrics](#det-007--authentication-dashboard-metrics)
- [🧠 Detection Summary](#-detection-summary)
- [🌍 Threat Intelligence Integration](#-threat-intelligence-integration-1)
  - [Enriched Threat Intelligence](#enriched-threat-intelligence)
- [🐍 Python Automation](#-python-automation-1)
  - [Automation Workflow](#automation-workflow)
  - [Project Scripts](#project-scripts)
    - [Automation Benefits](#automation-benefits)
- [🚨 Alerting](#-alerting)
- [📊 SOC Dashboard](#-soc-dashboard)
  - [Dashboard Panels](#dashboard-panels)
- [🔎 Investigation Workflow](#-investigation-workflow)
- [🖼️ Project Gallery](#️-project-gallery)
  - [☁️ AWS Infrastructure](#️-aws-infrastructure-1)
  - [🖥️ Splunk Enterprise](#️-splunk-enterprise)
  - [📄 Authentication Events](#-authentication-events)
  - [🔍 SSH Brute-Force Detection](#-ssh-brute-force-detection)
  - [📊 SOC Dashboard](#-soc-dashboard-1)
  - [🌍 Threat Intelligence Enrichment](#-threat-intelligence-enrichment)
- [📁 Documentation](#-documentation)
- [🎯 Skills Demonstrated](#-skills-demonstrated)
    - [Security Operations](#security-operations)
    - [Splunk](#splunk)
    - [Cloud](#cloud)
    - [Threat Intelligence](#threat-intelligence)
    - [Programming](#programming)
    - [Security Frameworks](#security-frameworks)
- [💡 Lessons Learned](#-lessons-learned)
- [🚀 Future Enhancements](#-future-enhancements)
- [👨‍💻 Author](#-author)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
  - [⭐ If you found this project useful, consider giving it a star!](#-if-you-found-this-project-useful-consider-giving-it-a-star)

---

# 📌 Executive Overview

Enterprise SSH Threat Monitoring is a Security Operations Center (SOC) project that demonstrates how organizations can detect, investigate, and enrich SSH brute-force attacks using Splunk Enterprise, Python automation, and external Threat Intelligence.

The project simulates real-world SSH password attacks against a Linux server, forwards authentication logs to Splunk through the Universal Forwarder, detects malicious authentication attempts using custom SPL searches, enriches attacker IP addresses with AbuseIPDB Threat Intelligence, and presents the findings through operational SOC dashboards.

Unlike basic SIEM labs that stop after log collection, this project follows the complete detection engineering lifecycle—from log ingestion and attack simulation to alerting, enrichment, investigation, and reporting.

---

# 🎯 Project Objectives

- Detect SSH brute-force attacks in real time
- Build production-style SPL detection rules
- Automate Threat Intelligence enrichment
- Generate actionable security alerts
- Visualize attacks through SOC dashboards
- Investigate malicious activity using indexed logs
- Demonstrate enterprise SIEM architecture
- Apply Detection Engineering methodologies

---

# 🚀 Key Features

## 🔍 Detection Engineering

- SSH Brute-force Detection
- Successful Login Detection
- Password Spray Identification
- High-Risk Source IP Detection
- Authentication Trend Analysis
- Failed Login Threshold Alerts
- MITRE ATT&CK Mapping

---

## 🌐 Threat Intelligence Integration

The project automatically enriches attacker IP addresses using the AbuseIPDB API.

Each detected attacker IP is evaluated for:

- Abuse Confidence Score
- Country
- ISP
- Domain
- Usage Type
- Total Reports
- Last Reported Date

This enrichment enables analysts to prioritize investigations based on reputation instead of relying solely on authentication logs.

---

## 🐍 Python Automation

Custom Python scripts automate the enrichment workflow by:

- Extracting unique attacker IPs from Splunk
- Querying AbuseIPDB
- Building Threat Intelligence lookup tables
- Updating Splunk lookups automatically
- Eliminating repetitive analyst tasks

---

# 🏗️ High-Level Architecture


<p align="center">
  <img src="diagrams/architecture.png"
       alt="High-level architecture showing Kali Linux, Ubuntu Server, Splunk Universal Forwarder, Splunk Enterprise, and AbuseIPDB threat intelligence integration"
       width="100%">
</p>

<p align="center">
  <i>Figure 1. High-level architecture illustrating log collection, detection engineering, and threat intelligence enrichment.</i>
</p>

The environment consists of four primary components:

| Component | Purpose |
|------------|----------|
| Kali Linux | Attack simulation |
| Ubuntu Server | SSH target |
| Splunk Universal Forwarder | Log forwarding |
| Splunk Enterprise | Detection, dashboards, investigation |

Authentication events generated on the Ubuntu server are collected by the Universal Forwarder and securely transmitted to Splunk Enterprise. Detection searches identify suspicious authentication patterns, while Python automation enriches attacker IPs using AbuseIPDB before dashboards present actionable security insights.

---

# 🔄 End-to-End Workflow

```text
Attacker (Kali Linux)
          │
          ▼
SSH Brute-force Attack
          │
          ▼
Ubuntu Server (auth.log)
          │
          ▼
Splunk Universal Forwarder
          │
          ▼
Splunk Enterprise Index
          │
          ▼
SPL Detection Searches
          │
          ▼
Python Threat Intelligence Enrichment
          │
          ▼
AbuseIPDB API
          │
          ▼
Threat Intelligence Lookup
          │
          ▼
SOC Dashboard & Investigation
```

<p align="center">
  <em>Figure 2. End-to-end workflow illustrating log collection, detection, enrichment, and SOC investigation.</em>
</p>
---

# 🛠️ Technology Stack

| Category | Technologies |
|-----------|--------------|
| Cloud | AWS EC2 |
| Operating System | Ubuntu Server |
| SIEM | Splunk Enterprise |
| Log Collection | Splunk Universal Forwarder |
| Programming | Python |
| Query Language | SPL |
| Threat Intelligence | AbuseIPDB API |
| Version Control | Git & GitHub |
| Security Framework | MITRE ATT&CK |
| Documentation | Markdown |

---

# 📂 Repository Structure

```text
Enterprise-SSH-Threat-Monitoring
│
├── config/
├── diagrams/
├── docs/
├── images/
├── lookups/
├── scripts/
├── screenshots/
├── requirements.txt
├── pyproject.toml
├── README.md
└── LICENSE
```

---

# ☁️ AWS Infrastructure

The environment was deployed entirely on AWS EC2 to replicate an enterprise monitoring environment.

## Infrastructure Components

| Instance | Purpose |
|-----------|----------|
| Ubuntu EC2 | SSH Target Server |
| Splunk EC2 | SIEM Platform |
| Kali Linux VM | Attack Machine |

The infrastructure was designed to simulate realistic attack scenarios while remaining lightweight enough for a personal cybersecurity lab.


---

# ⚙️ Splunk Enterprise Configuration

Splunk Enterprise serves as the Security Information and Event Management (SIEM) platform responsible for collecting, indexing, searching, and visualizing authentication events generated by the Linux server.

## Configuration Summary

| Component | Status |
|-----------|--------|
| Splunk Enterprise | Installed |
| Management Port | 8000 |
| Receiving Port | 9997 |
| Linux Authentication Logs | Indexed |
| Search Head | Configured |
| Dashboards | Created |
| Alerts | Enabled |

---

# 📡 Log Collection Pipeline

Authentication events generated on the Ubuntu server are continuously monitored by the Splunk Universal Forwarder.

```
/var/log/auth.log
        │
        ▼
Splunk Universal Forwarder
        │
        ▼
TCP 9997
        │
        ▼
Splunk Enterprise
        │
        ▼
linux_auth Index
```

Every authentication event is indexed in near real-time, allowing analysts to investigate suspicious activity as it occurs.

---

# 🖥️ Splunk Universal Forwarder

The Splunk Universal Forwarder provides secure and lightweight log forwarding from the Linux server.

### Forwarded Logs

- SSH Authentication Logs
- Failed Password Attempts
- Successful Logins
- Invalid User Attempts
- Privilege Escalation Events (if generated)

---

# ⚔️ Attack Simulation

To validate the detection pipeline, SSH brute-force attacks were simulated against the Ubuntu server from a Kali Linux attacker machine.

## Attack Scenarios

- Failed Password Attempts
- Multiple Login Failures
- Successful Authentication
- Password Spray Simulation
- High-Volume Login Attempts

This generated realistic authentication events that could be detected and investigated through Splunk.

---

# 🎯 Detection Engineering

One of the primary goals of this project was to develop production-style SPL detections capable of identifying malicious SSH authentication activity.

Each detection follows a practical SOC workflow and maps to relevant MITRE ATT&CK techniques where applicable.

---

## DET-001 — SSH Brute-Force Detection

### Objective

Identify source IP addresses generating an excessive number of failed SSH login attempts.

### SPL

```spl
index=linux_auth "Failed password"
| rex field=_raw "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by src_ip
| where count>=5
| sort -count
```

### Expected Result

- Source IP
- Failed Login Count

### MITRE ATT&CK

- T1110 — Brute Force

---

## DET-002 — Successful SSH Login Detection

### Objective

Identify successful SSH authentications.

### SPL

```spl
index=linux_auth "Accepted password"
| rex field=_raw "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| table _time host user src_ip
```

### Expected Result

- Login Time
- Username
- Source IP

### MITRE ATT&CK

- T1078 — Valid Accounts

---

## DET-003 — Failed Login Trend

### Objective

Visualize failed authentication attempts over time.

### SPL

```spl
index=linux_auth "Failed password"
| timechart span=5m count
```

### Expected Result

Trend graph displaying authentication spikes.

---

## DET-004 — Top Attacking IP Addresses

### Objective

Identify the most active attacking systems.

### SPL

```spl
index=linux_auth "Failed password"
| rex field=_raw "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| top src_ip
```

### Expected Result

Top attacker IP addresses ranked by frequency.

---

## DET-005 — Password Spray Detection

### Objective

Detect one IP attempting to authenticate against multiple user accounts.

### SPL

```spl
index=linux_auth "Failed password"
| rex field=_raw "for (invalid user )?(?<user>\S+)"
| rex field=_raw "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| stats dc(user) as targeted_users by src_ip
| where targeted_users>=3
```

### MITRE ATT&CK

- T1110.003 — Password Spraying

---

## DET-006 — High-Risk Source IP Detection

### Objective

Display attacker IPs enriched through Threat Intelligence.

### SPL

```spl
index=linux_auth
| lookup abuseipdb_lookup src_ip OUTPUT abuseConfidenceScore countryCode isp
| table src_ip abuseConfidenceScore countryCode isp
```

### Expected Result

Threat Intelligence enriched attacker list.

---

## DET-007 — Authentication Dashboard Metrics

Key operational metrics include:

- Failed Logins
- Successful Logins
- Unique Attackers
- Top Source Countries
- Top ISPs
- Highest Abuse Scores
- Authentication Timeline

---

# 🧠 Detection Summary

| Detection | Purpose |
|-----------|---------|
| DET-001 | SSH Brute Force |
| DET-002 | Successful Login |
| DET-003 | Authentication Trend |
| DET-004 | Top Attackers |
| DET-005 | Password Spray |
| DET-006 | Threat Intelligence |
| DET-007 | Dashboard Metrics |

---

# 🌍 Threat Intelligence Integration

To provide meaningful context for detected attacker IP addresses, the project integrates with the AbuseIPDB API. Every unique source IP extracted from Splunk is automatically queried, allowing analysts to distinguish between unknown addresses and IPs with a documented history of malicious activity.

## Enriched Threat Intelligence

Each attacker IP is enriched with:

| Field | Description |
|--------|-------------|
| IP Address | Source attacker IP |
| Abuse Confidence Score | Reputation score (0–100) |
| Country | Geographic location |
| ISP | Internet Service Provider |
| Domain | Registered domain |
| Usage Type | Hosting, ISP, Data Center, etc. |
| Total Reports | Number of abuse reports |
| Last Reported | Most recent report date |

The enriched data is stored as a Splunk lookup table and automatically referenced by detection searches and dashboards.

---

# 🐍 Python Automation

Python scripts automate the Threat Intelligence workflow, eliminating manual lookups and enabling repeatable enrichment.

## Automation Workflow

```
Splunk Search
      │
      ▼
Extract Unique IPs
      │
      ▼
Query AbuseIPDB API
      │
      ▼
Generate CSV Lookup
      │
      ▼
Update Splunk Lookup
      │
      ▼
Dashboard Enrichment
```

## Project Scripts

| Script | Purpose |
|---------|---------|
| main.py | Executes the complete automation workflow |
| splunk_client.py | Retrieves attacker IPs from Splunk |
| abuseipdb.py | Queries the AbuseIPDB API |
| lookup_builder.py | Creates the lookup CSV |
| config.py | Loads environment variables and credentials |

### Automation Benefits

- Eliminates repetitive analyst tasks
- Enriches detections automatically
- Produces reusable lookup tables
- Improves investigation speed
- Demonstrates Python automation within a SOC workflow

---

# 🚨 Alerting

Custom SPL searches can be configured as scheduled alerts to notify analysts when suspicious authentication activity exceeds defined thresholds.

Example alert conditions include:

- More than 5 failed logins from a single IP
- Password spray attempts
- Successful logins following multiple failures
- Connections from high-risk IP addresses
- Authentication spikes within a defined time window

---

# 📊 SOC Dashboard

The Splunk dashboard provides analysts with a centralized view of authentication activity and attacker intelligence.

## Dashboard Panels

- Failed Login Timeline
- Successful Login Timeline
- Top Attacking IP Addresses
- Failed Logins by Host
- Authentication Volume
- Threat Intelligence Summary
- Abuse Confidence Scores
- Top Countries
- Top ISPs

The dashboard enables analysts to rapidly identify attack trends, prioritize investigations, and assess the severity of authentication events.

---

# 🔎 Investigation Workflow

The investigation process follows a structured SOC methodology.

1. SSH attack is launched against the Ubuntu server.
2. Authentication events are written to `auth.log`.
3. Splunk Universal Forwarder forwards logs.
4. Splunk indexes incoming events.
5. SPL detections identify suspicious activity.
6. Python automation enriches attacker IPs.
7. Dashboards display enriched security events.
8. Analysts investigate affected hosts and attacker behavior.

This workflow mirrors the lifecycle commonly used by enterprise Security Operations Centers.

---

# 🖼️ Project Gallery

The following screenshots highlight the deployment, detection workflow, dashboards, and threat intelligence enrichment implemented throughout the project.

## ☁️ AWS Infrastructure

<p align="center">
  <img src="screenshots/aws/01-ec2-instances.png"
       alt="AWS EC2 instances hosting the Ubuntu SSH target server and Splunk Enterprise SIEM"
       width="100%">
</p>

<p align="center">
<i>AWS EC2 infrastructure hosting the Ubuntu SSH target server and Splunk Enterprise SIEM.</i>
</p>

---

## 🖥️ Splunk Enterprise

<p align="center">
<img src="screenshots/splunk/04-splunk-home.png"
     alt="Splunk Enterprise home dashboard displaying the SIEM interface"
     width="100%">
</p>

<p align="center">
<i>Splunk Enterprise interface used for log ingestion, searching, visualization, and security monitoring.</i>
</p>

---


## 📄 Authentication Events

<p align="center">
<img src="screenshots/splunk/08-linux-auth-events.png"
     alt="Linux SSH authentication events indexed in Splunk from the auth.log file"
     width="100%">
</p>

<p align="center">
<i>Linux SSH authentication events successfully collected and indexed from the <code>/var/log/auth.log</code> file.</i>
</p>

---


## 🔍 SSH Brute-Force Detection

<p align="center">
<img src="screenshots/dashboard/12-bruteforce-table.png"
     alt="Splunk search results identifying SSH brute-force attacks and repeated failed login attempts"
     width="100%">
</p>

<p align="center">
<i>Custom SPL detection highlighting repeated failed SSH login attempts and identifying suspicious source IP activity.</i>
</p>

---

## 📊 SOC Dashboard

<p align="center">
<img src="screenshots/dashboard/11-dashboard.png"
     alt="Interactive Splunk SOC dashboard visualizing authentication activity and security metrics"
     width="100%">
</p>

<p align="center">
<i>Interactive SOC dashboard providing real-time visibility into authentication events, attack trends, and security metrics.</i>
</p>

---

## 🌍 Threat Intelligence Enrichment

<p align="center">
<img src="screenshots/threat-intelligence/21-threat-intelligence-enrichment.png"
     alt="Threat intelligence enrichment in Splunk using AbuseIPDB reputation data for attacker IP addresses"
     width="100%">
</p>

<p align="center">
<i>Automatic enrichment of attacker IP addresses using AbuseIPDB threat intelligence to provide reputation and contextual information.</i>
</p>

---

# 📁 Documentation

Additional documentation is available in the `docs/` directory, including:

- Deployment Guide
- Splunk Configuration
- Threat Intelligence Workflow
- Detection Engineering Notes
- Architecture Documentation

---

# 🎯 Skills Demonstrated

This project demonstrates practical experience in:

### Security Operations

- SIEM Operations
- Detection Engineering
- Incident Investigation
- Log Analysis
- Security Monitoring

### Splunk

- SPL Development
- Dashboards
- Alerting
- Lookups
- Data Indexing

### Cloud

- AWS EC2
- Ubuntu Administration
- Linux Log Management

### Threat Intelligence

- AbuseIPDB API
- IOC Enrichment
- Reputation Analysis

### Programming

- Python
- REST API Integration
- CSV Processing
- Automation

### Security Frameworks

- MITRE ATT&CK
- Detection Engineering Methodology

---

# 💡 Lessons Learned

Through this project, I gained practical experience in designing and implementing an end-to-end detection engineering workflow.

Key takeaways include:

- Building enterprise-style SIEM architectures
- Developing effective SPL detection searches
- Working with Linux authentication logs
- Automating repetitive SOC tasks with Python
- Integrating external Threat Intelligence sources
- Investigating SSH authentication attacks
- Designing dashboards for operational visibility
- Documenting technical projects for knowledge sharing

---

# 🚀 Future Enhancements

Planned improvements include:

- GeoIP visualizations
- Automated case creation with TheHive
- VirusTotal integration
- Email and Slack alerting
- Sigma rule mapping
- Additional Linux detections
- Windows event monitoring
- Detection tuning and false-positive reduction
- SOAR integration with Shuffle
- ATT&CK Navigator heat maps

---

# 👨‍💻 Author

**Ravi Kiran Kambhampati**

Cybersecurity & Cloud Operations Graduate

- Detection Engineering
- SOC Operations
- Splunk
- Python Automation
- Threat Intelligence
- AWS

GitHub: [ravikirank29](https://github.com/ravikirank29)

LinkedIn: [Ravi Kiran Kambhampati](https://www.linkedin.com/in/ravi-kiran-kambhampati/)

---

# 🤝 Contributing

Contributions, suggestions, and feedback are welcome. Feel free to open an issue or submit a pull request if you have ideas for improving this project.

---

# 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for additional information.

---

## ⭐ If you found this project useful, consider giving it a star!

