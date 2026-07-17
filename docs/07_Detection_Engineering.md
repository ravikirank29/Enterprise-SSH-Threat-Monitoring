# Detection Engineering

## Overview

Detection engineering is the process of designing, implementing, and validating security detections that identify malicious or suspicious activity within an environment. In this project, custom Splunk Search Processing Language (SPL) queries were developed to detect SSH authentication anomalies and support Security Operations Center (SOC) investigations.

The detections were built using Linux authentication events collected from `/var/log/auth.log` and indexed within the `linux_auth` index.

---

# Objectives

The primary objectives of the detection engineering phase were:

- Detect SSH brute-force attacks.
- Identify repeated authentication failures.
- Monitor successful SSH logins.
- Identify the most targeted user accounts.
- Identify the most active source IP addresses.
- Detect successful logins following multiple failed attempts.
- Support SOC investigations with actionable security telemetry.

---

# Detection Workflow

```text
Authentication Event
        │
        ▼
linux_auth Index
        │
        ▼
SPL Search
        │
        ▼
Detection Rule
        │
        ▼
Dashboard
        │
        ▼
Alert
        │
        ▼
SOC Investigation
```

---

# Detection 1 – Failed SSH Login Trend

## Purpose

Monitor the number of failed SSH authentication attempts over time.

## Detection Logic

This detection identifies authentication failures recorded by the SSH daemon and visualizes their frequency over time.

### SPL Query

```spl
index=linux_auth "Failed password"
| timechart count
```

### SOC Value

- Detect brute-force activity.
- Identify authentication spikes.
- Support trend analysis.

---

# Detection 2 – Successful SSH Login Trend

## Purpose

Monitor successful SSH authentication events.

### SPL Query

```spl
index=linux_auth "Accepted password"
| timechart count
```

### SOC Value

- Track legitimate authentication activity.
- Compare successful and failed login patterns.

---

# Detection 3 – Top Attacking IP Addresses

## Purpose

Identify the IP addresses responsible for the highest number of failed authentication attempts.

### SPL Query

```spl
index=linux_auth "Failed password"
| rex "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by src_ip
| sort -count
```

### SOC Value

- Identify the most active attacking hosts.
- Prioritize investigations.

---

# Detection 4 – Most Targeted User Accounts

## Purpose

Identify which usernames attackers attempted to authenticate against.

### SPL Query

```spl
index=linux_auth "Failed password"
| rex "for (invalid user )?(?<user>\w+)"
| stats count by user
| sort -count
```

### SOC Value

- Identify high-value targets.
- Understand attacker behavior.

---

# Detection 5 – SSH Brute-Force Detection

## Purpose

Detect excessive authentication failures originating from the same source IP.

### SPL Query

```spl
index=linux_auth "Failed password"
| rex "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by src_ip
| where count >= 5
```

### Detection Threshold

```
5 Failed Login Attempts
```

### SOC Value

- Detect brute-force attacks.
- Trigger automated alerts.
- Reduce analyst response time.

---

# Detection 6 – Successful Login After Multiple Failures

## Purpose

Identify successful authentication events that occur after multiple failed login attempts.

### Detection Logic

This detection helps identify scenarios where an attacker may have successfully guessed valid credentials after repeated failures.

### SPL Query

```spl
index=linux_auth ("Failed password" OR "Accepted password")
```

### SOC Value

- Detect possible account compromise.
- Support incident investigations.

---

# Dashboard Integration

Each detection was integrated into the Enterprise SSH Threat Monitoring dashboard.

Dashboard panels include:

- Failed Login Trend
- Successful Login Trend
- Top Attacking IPs
- Most Targeted Users
- Brute Force Detection
- Successful Login After Multiple Failures

---

# Detection Validation

Each detection was validated using authentication events generated during controlled attack simulations.

Validation included:

- Failed SSH login attempts
- Successful logins
- Invalid usernames
- Multiple authentication failures
- Repeated login attempts from the same IP

All detections returned expected results and accurately reflected the generated authentication activity.

---

# Benefits

The implemented detection rules provide several operational benefits:

- Continuous authentication monitoring.
- Rapid identification of suspicious login behavior.
- Improved SOC visibility.
- Automated brute-force detection.
- Support for incident response.
- Foundation for future threat hunting.

---

# Future Enhancements

Future versions of this project will expand the detection library to include:

- Password spraying detection.
- SSH key abuse detection.
- Privilege escalation detection.
- New user account creation.
- SSH configuration changes.
- Suspicious sudo activity.
- Threat intelligence enrichment.
- MITRE ATT&CK mapping.
- Risk-based alerting.

---

# Conclusion

The detection engineering phase demonstrates how raw authentication logs can be transformed into actionable security detections using Splunk SPL. These detections enable SOC analysts to rapidly identify suspicious authentication activity, investigate potential credential attacks, and respond to security incidents using centralized visibility provided by Splunk Enterprise.

The detection library developed in this project forms the foundation for future enhancements involving advanced threat hunting, behavioral analytics, and enterprise-scale security monitoring.