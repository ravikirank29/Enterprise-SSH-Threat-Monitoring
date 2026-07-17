# Lessons Learned

## Overview

Building the Enterprise SSH Threat Monitoring lab provided practical experience in designing, deploying, monitoring, and securing a centralized Security Information and Event Management (SIEM) environment using Splunk Enterprise.

Unlike theoretical cybersecurity exercises, this project required troubleshooting real infrastructure issues, validating data collection pipelines, developing detection logic, and confirming that alerts accurately reflected simulated attack activity.

The project reinforced the importance of reliable log collection, effective detection engineering, and continuous monitoring in modern Security Operations Centers (SOCs).

---

# Technical Skills Gained

Throughout this project, practical experience was gained in several key cybersecurity domains.

## Cloud Infrastructure

- Deploying Linux servers in AWS EC2
- Configuring Security Groups
- Managing cloud networking
- Remote administration using SSH

---

## Linux Administration

- Managing Ubuntu servers
- Configuring OpenSSH
- Monitoring authentication logs
- Managing Linux services
- Basic system troubleshooting

---

## Splunk Enterprise

- Installing Splunk Enterprise
- Creating custom indexes
- Configuring data receivers
- Searching authentication events
- Writing SPL queries
- Creating dashboards
- Building scheduled alerts

---

## Detection Engineering

The project demonstrated how raw authentication logs can be transformed into meaningful security detections.

Detection use cases implemented included:

- Failed login monitoring
- Successful login monitoring
- Brute-force detection
- Top attacking IPs
- Most targeted users
- Successful logins following repeated failures

These detections represent common use cases performed by Security Operations Center analysts.

---

# Challenges Encountered

Several technical challenges were encountered during implementation.

## SSH Password Authentication

By default, Ubuntu cloud images disabled password-based SSH authentication.

This prevented authentication testing until the SSH configuration was modified and the SSH service restarted.

Understanding the interaction between cloud image defaults and OpenSSH configuration highlighted the importance of validating system configurations before beginning security testing.

---

## Universal Forwarder Configuration

Ensuring reliable log forwarding required validating multiple components, including:

- Data receiver configuration
- Forwarder connectivity
- Network communication
- Monitored log files
- Indexed events

This process emphasized that successful log collection depends on the correct configuration of both the forwarder and the receiving Splunk instance.

---

## Detection Validation

Developing effective detection rules required generating representative authentication events and verifying that each SPL query returned accurate results.

This reinforced the importance of validating detection logic using realistic telemetry rather than assuming searches function correctly.

---

# Key Takeaways

Several important lessons emerged during this project.

## Centralized Logging

Reliable centralized log collection is the foundation of any effective monitoring environment.

Without complete and accurate telemetry, even well-designed detection rules cannot identify malicious activity.

---

## Detection Engineering

Writing SPL queries is only one aspect of detection engineering.

Effective detections must also be validated, documented, and continuously improved based on observed attack behavior.

---

## Dashboard Design

Dashboards should present meaningful operational information rather than simply displaying raw data.

Well-designed visualizations enable analysts to identify suspicious activity quickly and reduce investigation time.

---

## Alert Tuning

Alerts should balance sensitivity with practicality.

Thresholds that are too low may generate excessive false positives, while thresholds that are too high may delay detection of legitimate attacks.

---

# Professional Skills Developed

Beyond technical implementation, this project strengthened several professional skills.

- Problem solving
- Troubleshooting
- Documentation
- System validation
- Security analysis
- Detection design
- Project planning
- Technical communication

---

# Future Improvements

Version 1.0 provides a solid foundation for future development.

Planned enhancements include:

- Threat Intelligence integration
- Password spraying detection
- Linux privilege escalation monitoring
- SSH key abuse detection
- MITRE ATT&CK mapping
- Threat hunting dashboards
- Risk-based alerting
- Executive SOC dashboard
- SOAR integration
- Windows endpoint monitoring
- Sysmon event collection
- Endpoint Detection and Response (EDR)

---

# Project Outcome

The Enterprise SSH Threat Monitoring lab successfully demonstrated an end-to-end Security Operations Center workflow.

The completed solution includes:

- AWS infrastructure
- Linux endpoint monitoring
- Centralized log collection
- Splunk Enterprise deployment
- Universal Forwarder configuration
- Authentication monitoring
- Attack simulation
- Detection engineering
- Dashboard development
- Automated alerting

Together, these components form a practical SOC monitoring environment that closely reflects enterprise security operations and provides a strong foundation for continued learning and future enhancements.

---

# Final Thoughts

This project demonstrates that effective cybersecurity is not limited to deploying security tools. Successful security monitoring requires a combination of reliable infrastructure, continuous log collection, thoughtful detection engineering, meaningful visualization, and ongoing validation.

Building this lab provided hands-on experience with technologies and workflows commonly used by Security Operations Center teams and established a scalable platform for future security research, threat hunting, and detection engineering projects.