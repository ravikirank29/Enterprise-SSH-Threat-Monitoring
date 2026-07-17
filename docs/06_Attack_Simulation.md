# Attack Simulation

## Overview

To validate the effectiveness of the monitoring environment, controlled attack simulations were performed against the Ubuntu target server. These simulations generated realistic authentication events that were collected, indexed, and analyzed within Splunk Enterprise.

The objective was not to compromise the system, but to produce representative security telemetry for developing and validating detection rules.

---

# Objectives

The attack simulation phase was designed to:

- Generate realistic SSH authentication events.
- Validate the end-to-end log collection pipeline.
- Produce telemetry for detection engineering.
- Test Splunk dashboards and scheduled alerts.
- Demonstrate a complete attack-to-detection workflow.

---

# Lab Environment

The attack simulation involved three systems.

| System | Purpose |
|----------|---------|
| Kali Linux | Attack simulation |
| Ubuntu Server | Target system |
| Splunk Enterprise | Monitoring and detection |

---

# Attack Scenario

The simulated attack followed the sequence below.

```text
Reconnaissance
        │
        ▼
Identify SSH Service
        │
        ▼
Attempt Multiple SSH Logins
        │
        ▼
Authentication Events Generated
        │
        ▼
Events Logged to auth.log
        │
        ▼
Forwarded to Splunk
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

---

# Reconnaissance

The first phase of the simulation consisted of identifying services exposed by the Ubuntu server.

The reconnaissance confirmed that:

- The server was reachable.
- SSH was available.
- Port 22 was accepting connections.

This information established the target for the authentication testing that followed.

---

# SSH Authentication Testing

Controlled SSH authentication attempts were performed against the Ubuntu server using valid and invalid credentials.

These activities generated a variety of authentication events, including:

- Successful logins
- Failed logins
- Invalid username attempts
- Incorrect password attempts

These events formed the basis for the detection rules created later in the project.

---

# Authentication Events Generated

The Ubuntu server recorded authentication activity within:

```text
/var/log/auth.log
```

Examples of recorded event types included:

- Failed password
- Accepted password
- Invalid user
- Session opened
- Session closed

Each event contained valuable information such as:

- Timestamp
- Source IP
- Username
- Hostname
- Authentication result

---

# Log Collection Validation

The Splunk Universal Forwarder continuously monitored the authentication log and forwarded newly generated events to Splunk Enterprise.

Validation confirmed that:

- Events were forwarded successfully.
- Data was indexed correctly.
- Searches returned expected results.
- Dashboards updated automatically.

---

# Detection Validation

The simulated authentication activity was used to validate multiple detection rules.

Examples included:

- Multiple failed authentication attempts.
- Successful authentication after repeated failures.
- Top attacking IP addresses.
- Most frequently targeted usernames.
- Authentication activity trends.

These detections demonstrated the ability of Splunk to identify suspicious authentication behavior in near real time.

---

# Dashboard Verification

Following the attack simulation, the dashboard reflected the generated activity.

Key visualizations included:

- Failed login trend
- Successful login trend
- Top attacking IPs
- Most targeted users
- SSH brute-force detection
- Authentication event timeline

This confirmed that the data pipeline from event generation through visualization was functioning correctly.

---

# Alert Validation

A scheduled alert was configured to detect excessive failed SSH authentication attempts.

During testing, the alert successfully triggered when the defined threshold was exceeded.

This validated the complete monitoring workflow from event generation to automated notification.

---

# End-to-End Workflow

The complete monitoring lifecycle is summarized below.

```text
Attack Simulation
        │
        ▼
Ubuntu SSH Service
        │
        ▼
Authentication Log
        │
        ▼
Universal Forwarder
        │
        ▼
Splunk Enterprise
        │
        ▼
Detection Rules
        │
        ▼
Dashboard
        │
        ▼
Alert
```

---

# Results

The attack simulation successfully demonstrated:

- Reliable log generation.
- Successful log forwarding.
- Centralized event collection.
- Accurate indexing.
- Effective SPL detections.
- Real-time dashboard updates.
- Automated alert generation.

---

# Lessons Learned

The simulation highlighted the importance of centralized authentication monitoring in identifying suspicious login behavior.

By combining continuous log collection with detection engineering, security analysts can rapidly identify credential-based attacks and investigate authentication anomalies before they lead to unauthorized access.

This phase also validated that the overall SOC monitoring environment was functioning as designed and ready for further enhancements such as threat intelligence integration, MITRE ATT&CK mapping, and advanced detection use cases.