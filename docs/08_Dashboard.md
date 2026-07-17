# Enterprise SSH Threat Monitoring Dashboard

## Overview

The Enterprise SSH Threat Monitoring dashboard provides a centralized view of Linux SSH authentication activity collected by Splunk Enterprise. It enables Security Operations Center (SOC) analysts to quickly identify suspicious authentication behavior, monitor attack trends, and investigate potential brute-force attacks from a single interface.

Rather than manually searching through thousands of authentication events, the dashboard presents key metrics and visualizations that support rapid detection and incident response.

---

# Objectives

The dashboard was designed to achieve the following objectives:

- Visualize Linux authentication activity
- Identify brute-force attacks
- Monitor successful and failed logins
- Identify attacking IP addresses
- Identify targeted user accounts
- Support incident investigations
- Reduce investigation time

---

# Dashboard Architecture

```text
Ubuntu Server
        │
Authentication Logs
        │
        ▼
Splunk Universal Forwarder
        │
        ▼
Splunk Enterprise
        │
        ▼
linux_auth Index
        │
        ▼
SPL Searches
        │
        ▼
Dashboard Panels
        │
        ▼
SOC Analyst
```

---

# Dashboard Panels

The Enterprise SSH Threat Monitoring dashboard consists of several visualization panels that provide different perspectives of authentication activity.

---

# Panel 1 – Failed SSH Login Trend

## Purpose

Displays the number of failed SSH login attempts over time.

## Visualization

Time Chart

## Benefits

- Detect brute-force attacks
- Identify authentication spikes
- Monitor attack frequency
- Support trend analysis

---

# Panel 2 – Successful SSH Login Trend

## Purpose

Displays successful SSH authentication events over time.

## Visualization

Time Chart

## Benefits

- Monitor legitimate user activity
- Compare successful and failed logins
- Identify unusual authentication behavior

---

# Panel 3 – Top Attacking IP Addresses

## Purpose

Displays the IP addresses responsible for the highest number of failed login attempts.

## Visualization

Bar Chart or Table

## Benefits

- Identify the most active attacking hosts
- Prioritize investigations
- Support threat hunting

---

# Panel 4 – Most Targeted User Accounts

## Purpose

Displays which usernames are targeted most frequently.

## Visualization

Bar Chart

## Benefits

- Identify high-value targets
- Detect username enumeration attempts
- Understand attacker behavior

---

# Panel 5 – SSH Brute Force Detection

## Purpose

Displays source IP addresses that exceeded the configured authentication failure threshold.

## Visualization

Statistics Table

## Benefits

- Immediate visibility into brute-force attacks
- Supports automated alerting
- Reduces analyst investigation time

---

# Panel 6 – Successful Login After Multiple Failures

## Purpose

Highlights successful SSH authentications that occur after multiple failed login attempts.

## Visualization

Event Table

## Benefits

- Identify possible account compromise
- Detect successful brute-force attacks
- Prioritize incident response

---

# Dashboard Workflow

```text
SSH Activity
      │
      ▼
Authentication Logs
      │
      ▼
Universal Forwarder
      │
      ▼
Splunk Enterprise
      │
      ▼
SPL Queries
      │
      ▼
Dashboard Panels
      │
      ▼
SOC Investigation
```

---

# Investigation Workflow

A SOC analyst can use the dashboard to investigate authentication activity using the following process:

### Step 1

Review the Failed Login Trend panel.

Look for sudden spikes in authentication failures.

---

### Step 2

Review the Top Attacking IPs panel.

Identify the source responsible for the highest number of failed logins.

---

### Step 3

Review the Most Targeted Users panel.

Determine which user accounts are under attack.

---

### Step 4

Review the Successful Login panel.

Determine whether the attacker eventually authenticated successfully.

---

### Step 5

Review the Successful Login After Multiple Failures panel.

If present, immediately begin an incident investigation.

---

# Operational Benefits

The dashboard provides several operational advantages.

- Real-time visibility
- Centralized monitoring
- Faster investigations
- Improved situational awareness
- Reduced analyst workload
- Simplified authentication monitoring

---

# Future Dashboard Enhancements

Future versions of the dashboard will include:

- Geographic attack map
- MITRE ATT&CK mapping
- Password spraying visualization
- Privilege escalation monitoring
- Threat Intelligence enrichment
- Risk score dashboard
- Executive SOC overview
- Linux security posture dashboard

---

# Validation

The dashboard was validated using authentication events generated during controlled attack simulations.

Validation confirmed that:

- Failed logins appeared correctly
- Successful logins were displayed
- Attacking IPs were identified
- Targeted usernames were visualized
- Brute-force detection functioned correctly
- Dashboard updated in near real time

---

# Conclusion

The Enterprise SSH Threat Monitoring dashboard transforms raw Linux authentication logs into actionable security insights. By combining multiple SPL detections into a centralized monitoring interface, the dashboard enables SOC analysts to rapidly identify suspicious authentication behavior, investigate potential brute-force attacks, and respond to security incidents more efficiently.

The dashboard serves as the primary operational interface for this project and demonstrates practical SIEM dashboard development using Splunk Enterprise.