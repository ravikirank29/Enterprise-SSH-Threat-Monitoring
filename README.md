# 🛡️ Enterprise SSH Threat Monitoring using Splunk

<p align="center">
  <strong>Enterprise SOC Detection Engineering Lab</strong>
</p>

<p align="center">
  AWS • Splunk Enterprise • Ubuntu • Kali Linux • Detection Engineering • SPL
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/AWS-EC2-orange" alt="AWS">
  <img src="https://img.shields.io/badge/Splunk-Enterprise-green" alt="Splunk">
  <img src="https://img.shields.io/badge/Ubuntu-Linux-E95420" alt="Ubuntu">
  <img src="https://img.shields.io/badge/SIEM-Detection%20Engineering-blueviolet" alt="SIEM">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" alt="License">
</p>

---

## 📌 Overview

**Enterprise SSH Threat Monitoring using Splunk** is an end-to-end Security Operations Center (SOC) lab designed to simulate, detect, investigate, and monitor suspicious SSH authentication activity against Linux servers.

The project demonstrates the complete security monitoring lifecycle:

**Attack Simulation → Log Generation → Log Collection → Centralized SIEM → Detection Engineering → Dashboard Visualization → Automated Alerting → SOC Investigation**

The environment was built using AWS EC2, Ubuntu Linux, Kali Linux, Splunk Enterprise, and the Splunk Universal Forwarder.

Linux SSH authentication events generated on the monitored Ubuntu server are recorded in `/var/log/auth.log`. The Splunk Universal Forwarder continuously monitors this log file and forwards events to the Splunk Enterprise server.

Custom Splunk Search Processing Language (SPL) queries are then used to identify suspicious authentication patterns, including repeated login failures, brute-force behavior, targeted user accounts, and successful authentication activity.

The resulting security telemetry is presented through a centralized SOC dashboard and scheduled alerts.

> **Security Notice:** All attack simulations and security testing documented in this repository were performed exclusively within an authorized and controlled lab environment.

---

## 📑 Table of Contents

- [Project Objectives](#-project-objectives)
- [Architecture](#️-architecture)
- [Architecture Components](#-architecture-components)
- [Data Flow](#-data-flow)
- [Technology Stack](#️-technology-stack)
- [Project Workflow](#-project-workflow)
- [AWS Infrastructure](#️-aws-infrastructure)
- [Log Collection Pipeline](#-log-collection-pipeline)
- [Attack Simulation](#-attack-simulation)
- [Detection Engineering](#-detection-engineering)
- [Detection Catalog](#-detection-catalog)
- [SOC Dashboard](#-soc-dashboard)
- [Automated Alerting](#-automated-alerting)
- [SOC Investigation Workflow](#-soc-investigation-workflow)
- [Project Screenshots](#-project-screenshots)
- [Repository Structure](#️-repository-structure)
- [Documentation](#-documentation)
- [Skills Demonstrated](#-skills-demonstrated)
- [Lessons Learned](#-lessons-learned)
- [Version 1.0](#-version-10)
- [Future Roadmap](#-future-roadmap)
- [License](#-license)
- [Author](#-author)

---

# 🎯 Project Objectives

The primary objective of this project is to demonstrate how a Security Operations Center can detect and investigate credential-based attacks targeting Linux SSH services.

The project was designed to:

- Deploy a centralized SIEM using Splunk Enterprise.
- Monitor Linux SSH authentication activity.
- Collect authentication logs using the Splunk Universal Forwarder.
- Centralize security telemetry in a dedicated Splunk index.
- Simulate controlled SSH authentication attacks.
- Develop custom SPL detection rules.
- Identify repeated authentication failures.
- Identify the most active source IP addresses.
- Identify frequently targeted user accounts.
- Monitor successful SSH authentications.
- Detect potential successful authentication following repeated failures.
- Build an operational SOC monitoring dashboard.
- Configure scheduled Splunk alerts.
- Document the complete attack-to-detection lifecycle.

---

# 🏗️ Architecture

The project implements an end-to-end SSH threat monitoring pipeline.

<p align="center">
  <img src="diagrams/architecture.png" alt="Enterprise SSH Threat Monitoring Architecture" width="100%">
</p>

The architecture separates the environment into four primary components:

```text
Kali Linux
    │
    │ Controlled SSH Authentication Testing
    │ TCP/22
    ▼
Ubuntu Target Server
    │
    │ /var/log/auth.log
    ▼
Splunk Universal Forwarder
    │
    │ Log Forwarding
    │ TCP/9997
    ▼
Splunk Enterprise
    │
    ├── linux_auth Index
    ├── SPL Searches
    ├── Detection Rules
    ├── Dashboards
    └── Scheduled Alerts
    │
    ▼
SOC Analyst
    │
    ├── Monitoring
    ├── Investigation
    └── Incident Response
```

---

# 🧩 Architecture Components

## 1. Kali Linux

Kali Linux represents the security testing system within the controlled lab.

It is used to generate authentication telemetry for validating the monitoring environment.

Tools used during testing include:

- Nmap
- Hydra
- SSH client

The generated authentication activity allows the Splunk detections and alerts to be tested against realistic security events.

---

## 2. Ubuntu Target Server

The Ubuntu EC2 instance acts as the monitored Linux endpoint.

The server hosts the OpenSSH service and generates authentication events.

The primary log source monitored in this project is:

```text
/var/log/auth.log
```

This log contains events related to:

- Failed authentication attempts
- Successful authentications
- Invalid usernames
- SSH daemon activity
- Authentication failures
- Session creation
- Session termination

---

## 3. Splunk Universal Forwarder

The Splunk Universal Forwarder is installed on the Ubuntu target server.

Its responsibility is to continuously monitor the authentication log and forward newly generated events to the Splunk Enterprise server.

The forwarding path is:

```text
/var/log/auth.log
        │
        ▼
Splunk Universal Forwarder
        │
        │ TCP/9997
        ▼
Splunk Enterprise
```

---

## 4. Splunk Enterprise

Splunk Enterprise serves as the centralized Security Information and Event Management platform.

Its responsibilities include:

- Receiving authentication logs.
- Indexing security events.
- Executing SPL searches.
- Running detection logic.
- Supporting threat hunting.
- Visualizing security events.
- Generating scheduled alerts.
- Supporting SOC investigations.

Authentication events are stored within the dedicated:

```text
linux_auth
```

index.

---

## 5. SOC Analyst

The SOC analyst represents the defensive security workflow.

The analyst uses Splunk to:

- Monitor authentication activity.
- Review triggered alerts.
- Investigate suspicious source IPs.
- Identify targeted accounts.
- Analyze authentication timelines.
- Determine whether suspicious activity requires escalation.

---

# 🔄 Data Flow

The complete monitoring lifecycle follows this sequence:

```text
Controlled Security Test
        │
        ▼
SSH Authentication Activity
        │
        ▼
Ubuntu OpenSSH Service
        │
        ▼
/var/log/auth.log
        │
        ▼
Splunk Universal Forwarder
        │
        ▼
TCP Port 9997
        │
        ▼
Splunk Enterprise
        │
        ▼
linux_auth Index
        │
        ▼
SPL Detection Rules
        │
        ├───────────────┐
        ▼               ▼
    Dashboard         Alert
        │               │
        └───────┬───────┘
                ▼
        SOC Investigation
```

---

# 🛠️ Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| Cloud Infrastructure | AWS EC2 | Host cloud-based lab infrastructure |
| SIEM | Splunk Enterprise | Centralized log analysis and detection |
| Target System | Ubuntu Linux | Monitored Linux endpoint |
| Testing System | Kali Linux | Controlled security testing |
| Log Collection | Splunk Universal Forwarder | Forward authentication logs |
| Log Source | `/var/log/auth.log` | Linux authentication telemetry |
| Attack Simulation | Hydra | Generate controlled authentication activity |
| Reconnaissance | Nmap | Validate exposed SSH service |
| Protocol | SSH | Remote authentication |
| Detection Language | SPL | Security detection and analysis |
| Visualization | Splunk Dashboards | SOC monitoring |
| Alerting | Splunk Alerts | Automated detection notification |

---

# 🚀 Project Workflow

The project was implemented using the following workflow.

### Phase 1 — Infrastructure Deployment

AWS EC2 instances were deployed to host:

- Splunk Enterprise
- Ubuntu monitored endpoint

Network communication was configured using AWS security groups.

---

### Phase 2 — Splunk Deployment

Splunk Enterprise was installed and configured as the centralized SIEM platform.

A dedicated index was created:

```text
linux_auth
```

Splunk was configured to receive forwarded data on:

```text
TCP/9997
```

---

### Phase 3 — Endpoint Log Collection

The Splunk Universal Forwarder was installed on the Ubuntu target server.

The forwarder was configured to monitor:

```text
/var/log/auth.log
```

Authentication events were then forwarded to Splunk Enterprise.

---

### Phase 4 — Data Validation

Log ingestion was validated using:

```spl
index=linux_auth
```

This confirmed that authentication events were successfully reaching Splunk.

---

### Phase 5 — Controlled Attack Simulation

Authentication testing was performed against the Ubuntu SSH service from the Kali Linux system.

This generated security telemetry including:

- Failed login attempts
- Successful authentication
- Invalid username activity
- Repeated authentication attempts

---

### Phase 6 — Detection Engineering

Custom SPL queries were developed to analyze authentication behavior and identify suspicious patterns.

---

### Phase 7 — Dashboard Development

Detection results were integrated into a centralized SOC monitoring dashboard.

---

### Phase 8 — Alerting

Scheduled Splunk alerts were configured to automatically identify authentication activity exceeding predefined thresholds.

---

# ☁️ AWS Infrastructure

The lab uses AWS EC2 to host the Splunk Enterprise and Ubuntu target systems.

The architecture includes:

```text
AWS VPC
│
├── Splunk Enterprise EC2
│   ├── Splunk Web
│   ├── Splunk Indexer
│   └── TCP Receiver
│
└── Ubuntu Target EC2
    ├── OpenSSH
    ├── auth.log
    └── Splunk Universal Forwarder
```

Required communication includes:

| Source | Destination | Port | Purpose |
|---|---|---:|---|
| Testing System | Ubuntu Target | 22 | SSH |
| Ubuntu Target | Splunk Enterprise | 9997 | Log Forwarding |
| Analyst | Splunk Enterprise | 8000 | Splunk Web |

AWS security groups were configured to permit only the network communication required for the lab.

---

# 📥 Log Collection Pipeline

Reliable log collection is the foundation of the project.

The primary authentication log is:

```text
/var/log/auth.log
```

The ingestion pipeline is:

```text
SSH Event
    │
    ▼
OpenSSH
    │
    ▼
/var/log/auth.log
    │
    ▼
Splunk Universal Forwarder
    │
    ▼
TCP/9997
    │
    ▼
Splunk Enterprise
    │
    ▼
linux_auth
```

The Universal Forwarder continuously monitors the log file and sends new authentication events to the Splunk Enterprise server.

This provides centralized visibility into Linux authentication activity.

---

# 🧪 Attack Simulation

Controlled authentication testing was performed to validate the complete monitoring pipeline.

The simulation followed this workflow:

```text
Reconnaissance
      │
      ▼
SSH Service Identification
      │
      ▼
Controlled Authentication Testing
      │
      ▼
Authentication Events Generated
      │
      ▼
Events Written to auth.log
      │
      ▼
Events Forwarded to Splunk
      │
      ▼
Detection Rules Executed
      │
      ▼
Dashboard Updated
      │
      ▼
Alert Triggered
```

The purpose of the simulation was to generate representative telemetry for defensive detection engineering.

All testing was performed exclusively against systems owned and controlled within the lab environment.

---

# 🔎 Detection Engineering

The core technical focus of this project is detection engineering.

Raw authentication events were transformed into actionable security information using custom SPL searches.

The detection strategy focused on identifying:

- Authentication failure spikes
- Repeated failed login attempts
- Suspicious source IP activity
- Frequently targeted user accounts
- Successful SSH authentications
- Potential authentication success following repeated failures

All SPL detection queries are maintained separately in the:

```text
spl/
```

directory.

This allows detection logic to be version-controlled independently from the documentation.

---

# 🧠 Detection Catalog

## Detection 1 — Failed SSH Login Trend

### Purpose

Identify changes and spikes in failed SSH authentication activity.

```spl
index=linux_auth "Failed password"
| timechart count
```

### SOC Use Case

A sudden increase in authentication failures may indicate automated credential guessing or other suspicious authentication behavior.

---

## Detection 2 — Successful SSH Login Trend

### Purpose

Monitor successful SSH authentications.

```spl
index=linux_auth "Accepted password"
| timechart count
```

### SOC Use Case

Successful login monitoring provides a baseline for legitimate authentication activity and supports investigations into potentially compromised accounts.

---

## Detection 3 — Top Attacking Source IPs

### Purpose

Identify source IP addresses generating the highest volume of failed authentication attempts.

```spl
index=linux_auth "Failed password"
| rex "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by src_ip
| sort -count
```

### SOC Use Case

This allows analysts to quickly prioritize the most active suspicious sources.

---

## Detection 4 — Most Targeted Users

### Purpose

Identify user accounts receiving the highest number of failed authentication attempts.

```spl
index=linux_auth "Failed password"
| rex "for (invalid user )?(?<user>\w+)"
| stats count by user
| sort -count
```

### SOC Use Case

This provides visibility into accounts that may be specifically targeted during credential attacks.

---

## Detection 5 — SSH Brute-Force Detection

### Purpose

Identify source IP addresses exceeding the configured failed-login threshold.

```spl
index=linux_auth "Failed password"
| rex "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by src_ip
| where count >= 5
```

### Detection Threshold

```text
5 or more failed authentication attempts
```

### SOC Use Case

The detection provides a simple threshold-based mechanism for identifying potential brute-force behavior.

> Detection thresholds should be tuned for the environment. A production environment may require baselining, allowlists, time-window logic, and additional context to reduce false positives.

---

## Detection 6 — Successful Login After Multiple Failures

### Purpose

Identify scenarios where repeated authentication failures may be followed by a successful authentication.

This use case is intended to help identify potential credential compromise and should correlate failure and success events using source IP, username, and time.

The validated correlation query is maintained in:

```text
spl/06_successful_after_failures.spl
```

### SOC Use Case

A successful authentication following repeated failures may warrant higher-priority investigation than failed attempts alone.

---

# 📊 SOC Dashboard

The **Enterprise SSH Threat Monitoring Dashboard** provides centralized visibility into authentication activity.

The dashboard includes panels for:

- Failed SSH Login Trend
- Successful SSH Login Trend
- Top Attacking IP Addresses
- Most Targeted User Accounts
- SSH Brute-Force Detection
- Successful Authentication After Multiple Failures

The dashboard allows analysts to move from high-level monitoring to focused investigation.

A typical workflow is:

```text
Failed Login Spike
        │
        ▼
Identify Source IP
        │
        ▼
Identify Targeted User
        │
        ▼
Review Authentication Timeline
        │
        ▼
Check for Successful Login
        │
        ▼
Investigate
```

---

# 🚨 Automated Alerting

A scheduled Splunk alert was configured to automatically identify potential SSH brute-force activity.

The alert uses threshold-based detection logic.

```text
Authentication Events
        │
        ▼
Scheduled SPL Search
        │
        ▼
Threshold Evaluation
        │
        ▼
Results Found?
      /     \
    No       Yes
    │         │
    ▼         ▼
Continue    Trigger Alert
Monitoring     │
               ▼
        SOC Investigation
```

The alert configuration includes:

| Setting | Configuration |
|---|---|
| Alert Type | Scheduled |
| Detection | SSH Brute Force |
| Trigger Condition | Results greater than zero |
| Data Source | `linux_auth` |
| Priority | High |

This demonstrates the transition from passive log monitoring to automated security detection.

---

# 🕵️ SOC Investigation Workflow

When suspicious authentication activity is detected, an analyst can follow this investigation process.

### 1. Review the Alert

Determine:

- Detection time
- Source IP
- Number of failed attempts

### 2. Identify Targeted Accounts

Determine which usernames were targeted by the suspicious source.

### 3. Review Authentication Timeline

Analyze authentication events before and after the alert.

### 4. Check for Successful Authentication

Determine whether the suspicious source successfully authenticated.

### 5. Investigate Additional Activity

Review other available telemetry associated with the source or account.

### 6. Determine Severity

Classify the activity based on available evidence.

### 7. Respond

In a production environment, potential response actions could include:

- Blocking a malicious source
- Disabling or protecting a compromised account
- Resetting credentials
- Reviewing endpoint activity
- Escalating the incident

---

# 📸 Project Screenshots

The following screenshots provide evidence of the implementation and validation of the lab.

> If a screenshot does not appear, verify that its filename matches the path below.

---

## Splunk Enterprise Dashboard

<p align="center">
  <img src="screenshots/dashboard/01-dashboard-overview.png" alt="Enterprise SSH Threat Monitoring Dashboard" width="100%">
</p>

The dashboard provides centralized visibility into Linux authentication activity and suspicious SSH behavior.

---

## Linux Authentication Events

<p align="center">
  <img src="screenshots/splunk/01-linux-auth-events.png" alt="Linux Authentication Events in Splunk" width="95%">
</p>

Authentication telemetry collected from `/var/log/auth.log` is forwarded to Splunk and indexed for analysis.

---

## Brute-Force Detection

<p align="center">
  <img src="screenshots/dashboard/02-brute-force-detection.png" alt="SSH Brute Force Detection in Splunk" width="95%">
</p>

Custom SPL detection logic identifies sources generating authentication failures above the configured threshold.

---

## Successful Login Investigation

<p align="center">
  <img src="screenshots/dashboard/03-success-after-failures.png" alt="Successful Authentication Investigation" width="95%">
</p>

Authentication correlation can help analysts identify potentially suspicious successful logins occurring around repeated authentication failures.

---

## Alert Trigger History

<p align="center">
  <img src="screenshots/alerts/02-alert-trigger-history.png" alt="Splunk Alert Trigger History" width="95%">
</p>

Scheduled alerts automatically surface suspicious authentication activity for analyst investigation.

---

# 🗂️ Repository Structure

```text
Enterprise-SSH-Threat-Monitoring/
│
├── README.md
├── LICENSE
├── .gitignore
├── CHANGELOG.md
│
├── docs/
│   ├── 01_Project_Overview.md
│   ├── 02_Lab_Architecture.md
│   ├── 03_AWS_Deployment.md
│   ├── 04_Splunk_Configuration.md
│   ├── 05_Log_Collection.md
│   ├── 06_Attack_Simulation.md
│   ├── 07_Detection_Engineering.md
│   ├── 08_Dashboard.md
│   ├── 09_Alerting.md
│   └── 10_Lessons_Learned.md
│
├── diagrams/
│   ├── architecture.drawio
│   ├── architecture.png
│   └── architecture.svg
│
├── spl/
│   ├── 01_failed_login_trend.spl
│   ├── 02_successful_login_trend.spl
│   ├── 03_top_attacking_ips.spl
│   ├── 04_targeted_users.spl
│   ├── 05_brute_force_detection.spl
│   ├── 06_successful_after_failures.spl
│   ├── 07_authentication_statistics.spl
│   └── 08_recent_security_events.spl
│
├── screenshots/
│   ├── aws/
│   ├── splunk/
│   ├── attacks/
│   ├── dashboard/
│   └── alerts/
│
└── images/
```

---

# 📚 Documentation

Detailed technical documentation is available in the `docs/` directory.

| Document | Description |
|---|---|
| `01_Project_Overview.md` | Project objectives, scope, and business problem |
| `02_Lab_Architecture.md` | Architecture and component design |
| `03_AWS_Deployment.md` | AWS infrastructure deployment |
| `04_Splunk_Configuration.md` | Splunk Enterprise configuration |
| `05_Log_Collection.md` | Authentication log ingestion pipeline |
| `06_Attack_Simulation.md` | Controlled attack simulation and validation |
| `07_Detection_Engineering.md` | SPL detection design |
| `08_Dashboard.md` | SOC dashboard implementation |
| `09_Alerting.md` | Automated alerting workflow |
| `10_Lessons_Learned.md` | Technical challenges and lessons learned |

---

# 💡 Skills Demonstrated

This project demonstrates hands-on experience with:

### Security Operations

- SOC Monitoring
- Security Event Analysis
- Alert Investigation
- Incident Triage
- Authentication Monitoring

### SIEM

- Splunk Enterprise
- Splunk Universal Forwarder
- Log Ingestion
- Index Management
- SPL
- Dashboard Development
- Alert Engineering

### Detection Engineering

- Detection Rule Development
- Threshold-Based Detection
- Authentication Analysis
- Detection Validation
- Security Event Correlation

### Cloud

- AWS EC2
- AWS VPC
- AWS Security Groups
- Cloud Networking

### Linux

- Ubuntu Administration
- OpenSSH
- Linux Authentication Logs
- Service Configuration
- Log Analysis

### Security Testing

- Kali Linux
- Nmap
- Controlled Authentication Testing
- Attack Simulation

### Engineering

- Git
- GitHub
- Technical Documentation
- Architecture Design
- Version Control

---

# 🧠 Lessons Learned

Several important lessons emerged while building the project.

### Reliable Telemetry Comes First

Detection engineering depends on reliable data collection.

Before building detections, the complete ingestion pipeline had to be validated:

```text
Log Source → Forwarder → Network → Receiver → Index → Search
```

### Cloud Defaults Affect Security Testing

Ubuntu cloud images may use SSH configurations that differ from traditional Linux installations.

Understanding effective SSH configuration was necessary to validate authentication telemetry.

### Detection Rules Require Validation

A query returning results does not automatically make it a reliable detection.

Detection logic must be tested against representative telemetry and reviewed for false positives and false negatives.

### Dashboards Should Support Decisions

The purpose of a SOC dashboard is not simply to display data.

Each panel should help answer an investigation question.

### Alerts Require Tuning

Static thresholds are useful for demonstrating detection concepts, but production detections require tuning based on environment size, user behavior, expected traffic, and historical baselines.

---

# ✅ Version 1.0

Version 1.0 establishes the foundation of the Enterprise SSH Threat Monitoring project.

### Completed

- AWS Infrastructure Deployment
- Splunk Enterprise Deployment
- Splunk Universal Forwarder Configuration
- Linux Authentication Log Collection
- SSH Security Monitoring
- Controlled Attack Simulation
- SPL Detection Engineering
- SOC Dashboard
- Scheduled Alerting
- Technical Documentation
- Architecture Documentation
- Version-Controlled Detection Queries

---

# 🛣️ Future Roadmap

Future versions may expand the monitoring environment with additional detection and response capabilities.

## Version 2.0 — Advanced Linux Detection Engineering

Planned areas include:

- Password spraying detection
- Privilege escalation monitoring
- Suspicious `sudo` activity
- New user account monitoring
- SSH configuration change monitoring
- Advanced authentication correlation

## Version 3.0 — Threat Intelligence

Potential capabilities:

- IP reputation enrichment
- Threat intelligence feeds
- Suspicious source prioritization
- Automated enrichment workflows

## Version 4.0 — Threat Hunting

Potential additions:

- Dedicated threat hunting queries
- Authentication anomaly hunting
- Historical attacker analysis
- Behavioral baselining

## Version 5.0 — Expanded SOC Environment

Potential expansion:

- Windows endpoint monitoring
- Sysmon telemetry
- Additional endpoint log sources
- Cross-platform detection engineering
- SOAR integration
- Incident response automation

---

# 🔐 Security Considerations

This repository is intended for cybersecurity education, defensive security research, and authorized lab testing.

All attack simulations documented in this project were conducted within systems specifically configured and authorized for testing.

Do not use security testing techniques against systems without explicit authorization.

Sensitive information such as:

- AWS credentials
- Private keys
- Access tokens
- Passwords
- Account identifiers

should never be committed to a public repository.

---

# 🤝 Contributing

This project is primarily maintained as a cybersecurity portfolio and research lab.

Suggestions for improving detection logic, dashboard design, documentation, and defensive monitoring workflows are welcome.

---

# 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

# 👤 Author

## Ravi Kiran Kambhampati

**Cybersecurity | SOC Operations | Detection Engineering | Cloud Security**

This project was developed as part of a hands-on cybersecurity portfolio focused on building practical skills in SIEM engineering, security monitoring, detection development, cloud infrastructure, and Security Operations Center workflows.

---

<p align="center">
  <strong>Enterprise SSH Threat Monitoring using Splunk</strong>
</p>

<p align="center">
  From Authentication Telemetry → Detection → Alert → Investigation
</p>

<p align="center">
  Version 1.0
</p>