# Alerting

## Overview

A Security Information and Event Management (SIEM) platform is most effective when it can automatically notify analysts of suspicious activity. In this project, Splunk Enterprise was configured to generate alerts when authentication events matched predefined detection criteria.

The primary alert implemented detects SSH brute-force attacks by identifying source IP addresses that exceed a specified threshold of failed login attempts within a defined period.

This automated alerting capability enables faster detection and response to credential-based attacks without requiring continuous manual monitoring.

---

# Objectives

The alerting configuration was designed to:

- Detect SSH brute-force attacks automatically.
- Notify analysts of suspicious authentication activity.
- Reduce manual log monitoring.
- Improve incident response time.
- Validate the end-to-end monitoring workflow.

---

# Alert Workflow

```text
SSH Authentication Activity
            │
            ▼
Linux Authentication Logs
            │
            ▼
Splunk Universal Forwarder
            │
            ▼
Splunk Enterprise
            │
            ▼
Scheduled SPL Search
            │
            ▼
Alert Condition Evaluated
            │
            ▼
Alert Triggered
            │
            ▼
SOC Analyst Investigation
```

---

# Alert Scenario

The implemented alert monitors authentication failures recorded in the `linux_auth` index.

When the number of failed SSH login attempts from a single source IP exceeds the configured threshold, Splunk generates an alert for analyst review.

---

# Detection Logic

The alert identifies repeated authentication failures originating from the same source IP address.

### Detection Criteria

- Multiple failed SSH authentication attempts
- Same source IP
- Threshold exceeded
- Configured search schedule

---

# Example SPL Search

```spl
index=linux_auth "Failed password"
| rex "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by src_ip
| where count >= 5
```

---

# Alert Configuration

The alert was configured with the following settings.

| Setting | Value |
|----------|-------|
| Alert Type | Scheduled |
| Search Interval | Every Minute |
| Trigger Condition | Number of Results > 0 |
| Severity | High |
| Data Source | linux_auth |

---

# Alert Lifecycle

The following sequence describes how an alert is generated.

1. Authentication attempts occur.
2. Authentication events are written to `/var/log/auth.log`.
3. The Universal Forwarder sends events to Splunk Enterprise.
4. Events are indexed within `linux_auth`.
5. The scheduled SPL search executes.
6. Splunk evaluates the detection threshold.
7. An alert is generated if the threshold is exceeded.
8. The SOC analyst begins an investigation.

---

# Alert Validation

The alert was validated during controlled attack simulations.

Validation activities included:

- Failed SSH login attempts
- Multiple authentication failures
- Repeated login attempts from the same source IP

The scheduled search successfully identified the generated activity and triggered an alert when the configured threshold was reached.

---

# Investigation Process

When an alert is generated, a SOC analyst can investigate using the following workflow.

### Step 1

Review the source IP address responsible for the failed authentication attempts.

---

### Step 2

Determine which usernames were targeted.

---

### Step 3

Review the authentication timeline.

---

### Step 4

Determine whether a successful login occurred after repeated failures.

---

### Step 5

Assess whether additional response actions are required.

---

# Benefits

Automated alerting provides several operational advantages.

- Reduced manual monitoring
- Faster attack detection
- Improved analyst efficiency
- Consistent detection logic
- Support for incident response
- Continuous monitoring

---

# Future Enhancements

Future releases of this project will expand alerting capabilities by including:

- Password spraying alerts
- Privilege escalation alerts
- SSH configuration change alerts
- New user account creation alerts
- Threat intelligence enrichment
- Risk-based alerting
- MITRE ATT&CK mapping
- Multi-stage attack correlation

---

# Conclusion

The alerting component completes the end-to-end monitoring workflow by automatically identifying suspicious authentication activity and notifying security analysts when predefined detection thresholds are exceeded.

Combined with centralized log collection, detection engineering, and dashboard visualization, automated alerting enables faster identification of potential SSH brute-force attacks and strengthens the overall effectiveness of the monitoring environment.