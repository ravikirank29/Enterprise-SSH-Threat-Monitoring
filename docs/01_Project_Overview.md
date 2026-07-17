# Project Overview

## Executive Summary

Enterprise SSH Threat Monitoring using Splunk is a Security Operations Center (SOC) lab designed to simulate, detect, and monitor SSH brute-force attacks against Linux servers. The project demonstrates the complete lifecycle of security monitoring, beginning with infrastructure deployment and ending with automated detection and alerting.

The lab was built using Amazon Web Services (AWS), Ubuntu Linux, Kali Linux, Splunk Enterprise, and the Splunk Universal Forwarder. SSH authentication events are collected from the Linux authentication log (`/var/log/auth.log`), forwarded to Splunk Enterprise, and analyzed using custom SPL (Search Processing Language) queries. The project also includes interactive dashboards and scheduled alerts to provide visibility into authentication activity.

Rather than focusing only on log ingestion, this project demonstrates practical detection engineering concepts commonly performed by SOC Analysts, Detection Engineers, and Blue Team professionals.

---

# Project Objectives

The primary objectives of this project are:

- Deploy a centralized SIEM platform using Splunk Enterprise.
- Configure centralized log collection from Linux servers.
- Monitor SSH authentication events.
- Simulate real-world SSH brute-force attacks using Hydra.
- Develop SPL detection rules for suspicious authentication behavior.
- Visualize security events using dashboards.
- Configure automated alerts for brute-force detection.
- Demonstrate an enterprise-style SOC monitoring workflow.

---

# Project Scope

The project includes the following components.

## Infrastructure

- Amazon EC2
- Ubuntu Linux
- AWS Security Groups
- AWS VPC Networking

## Security Monitoring

- Splunk Enterprise
- Splunk Universal Forwarder
- Linux Authentication Logs

## Attack Simulation

- Hydra
- Nmap
- SSH

## Detection Engineering

- SPL Queries
- Dashboard Development
- Alert Configuration

---

# Business Problem

Credential-based attacks continue to be one of the most common techniques used by attackers to gain unauthorized access to Linux servers. Security Operations Centers (SOCs) require centralized visibility into authentication activity to quickly identify brute-force attempts and investigate suspicious login behavior.

Without centralized monitoring, failed authentication attempts often remain unnoticed until an attacker successfully compromises an account.

This project demonstrates how a SIEM platform such as Splunk can be used to collect authentication logs, identify attack patterns, and provide actionable alerts to security analysts.

---

# Project Architecture

The monitoring workflow implemented in this project is illustrated below.

Internet

↓

Kali Linux (Attacker)

↓

SSH Brute Force Attack

↓

Ubuntu Linux Server

↓

/var/log/auth.log

↓

Splunk Universal Forwarder

↓

TCP Port 9997

↓

Splunk Enterprise

↓

Detection Rules

↓

SOC Dashboard

↓

Security Alerts

---

# Key Features

The project currently provides the following capabilities.

- SSH authentication monitoring
- Failed login detection
- Successful login monitoring
- Brute-force attack detection
- Top attacking IP identification
- Most targeted user identification
- Correlation of successful logins after repeated failures
- Interactive Splunk dashboard
- Automated scheduled alerts

---

# Expected Outcome

Upon completion, the project provides an enterprise-style monitoring environment capable of:

- Detecting SSH brute-force attacks.
- Providing visibility into Linux authentication activity.
- Supporting SOC investigations.
- Demonstrating practical SIEM engineering skills.
- Serving as a portfolio project for SOC Analyst and Detection Engineering roles.

---

# Skills Demonstrated

This project demonstrates practical experience with:

- AWS Cloud Infrastructure
- Linux Administration
- Splunk Enterprise
- Splunk Universal Forwarder
- SIEM Engineering
- Detection Engineering
- Search Processing Language (SPL)
- Security Monitoring
- Dashboard Development
- Alert Engineering
- SSH Security
- Hydra
- Nmap
- Blue Team Operations

---

# Version

Current Release

**Version 1.0**

Future releases will include:

- Threat Intelligence Integration
- Password Spraying Detection
- Linux Detection Engineering
- MITRE ATT&CK Mapping
- Threat Hunting
- Incident Response Workflow
