# AWS Deployment

## Overview

The Enterprise SSH Threat Monitoring lab is deployed entirely within Amazon Web Services (AWS). The cloud infrastructure provides a realistic enterprise environment for hosting the SIEM platform and monitored Linux systems while allowing attack simulations from an external attacker machine.

The deployment consists of two Ubuntu EC2 instances:

- Splunk Enterprise Server
- Ubuntu Target Server

A separate Kali Linux virtual machine is used as the attacker system to simulate reconnaissance and SSH brute-force attacks.

---

# Deployment Architecture

```text
                    Internet
                        │
                        │
            ┌───────────┴───────────┐
            │                       │
            ▼                       ▼
     Kali Linux VM            Analyst Browser
     (Hydra / Nmap)           (Splunk Web UI)
            │                       │
            │ SSH (22)              │ HTTPS (8000)
            ▼                       ▼
    Ubuntu Target EC2  ───────► Splunk Enterprise EC2
         │                         ▲
         │ auth.log                │
         │                         │
         └──── Universal Forwarder ┘
                 TCP 9997
```

---

# EC2 Instances

## Splunk Enterprise Server

The Splunk server functions as the centralized Security Information and Event Management (SIEM) platform.

### Responsibilities

- Receive forwarded logs
- Index incoming events
- Execute SPL searches
- Host dashboards
- Generate alerts
- Support investigations

### Operating System

Ubuntu Server

### Services

- Splunk Enterprise
- Splunk Web
- Splunk Indexer
- Splunk Search Head

---

## Ubuntu Target Server

The Ubuntu server acts as the monitored endpoint.

### Responsibilities

- Host the OpenSSH service
- Generate authentication logs
- Forward logs using the Splunk Universal Forwarder
- Receive simulated attacks

### Operating System

Ubuntu Server

### Installed Components

- OpenSSH Server
- Splunk Universal Forwarder

---

# Network Configuration

Both EC2 instances are deployed within the same AWS Virtual Private Cloud (VPC), allowing secure communication between the monitored endpoint and the Splunk server.

This design minimizes latency for log forwarding and reflects common enterprise network architectures.

---

# Security Groups

The security groups were configured to allow only the required network communication.

## Splunk Enterprise Server

| Port | Protocol | Purpose |
|------|----------|---------|
| 22 | TCP | SSH Administration |
| 8000 | TCP | Splunk Web Interface |
| 9997 | TCP | Universal Forwarder Data Reception |

---

## Ubuntu Target Server

| Port | Protocol | Purpose |
|------|----------|---------|
| 22 | TCP | SSH Access |

---

# Splunk Data Reception

The Splunk Enterprise server was configured to receive data from Universal Forwarders on TCP port **9997**.

The Ubuntu target server forwards Linux authentication logs to this receiving port in near real time.

---

# Log Source

The primary monitored log file is:

```text
/var/log/auth.log
```

This log contains:

- Failed SSH logins
- Successful SSH logins
- Invalid usernames
- Authentication failures
- Session creation
- SSH daemon activity

---

# Deployment Workflow

The AWS deployment followed these high-level steps:

1. Launch the Splunk Enterprise EC2 instance.
2. Launch the Ubuntu target EC2 instance.
3. Configure AWS security groups.
4. Install Splunk Enterprise.
5. Enable data receiving on port 9997.
6. Install the Splunk Universal Forwarder on the Ubuntu server.
7. Configure the forwarder to monitor `/var/log/auth.log`.
8. Verify successful log ingestion into Splunk.

---

# Validation

The deployment was validated using the following checks:

- Successful SSH connectivity to both EC2 instances.
- Splunk Web accessible on port 8000.
- Splunk receiving data on TCP port 9997.
- Universal Forwarder connected to the Splunk server.
- Authentication logs successfully indexed.
- Search results displaying real-time SSH events.

---

# Security Considerations

Several security practices were implemented during deployment:

- Only required ports were exposed.
- Log forwarding was isolated to the Splunk receiver.
- Centralized log collection reduced reliance on local log analysis.
- Authentication events were monitored continuously.

---

# Scalability

The current deployment supports a single monitored Linux server but is designed for future expansion.

Potential enhancements include:

- Additional Linux servers
- Windows endpoints
- Sysmon integration
- Multiple Universal Forwarders
- Dedicated indexers
- Search Head clustering
- Threat Intelligence integration
- Endpoint Detection and Response (EDR)

---

# Conclusion

Deploying the infrastructure in AWS provides a flexible and scalable environment for enterprise security monitoring. The combination of EC2 instances, centralized logging, and Splunk Enterprise creates a practical SOC lab that closely resembles real-world production deployments while remaining suitable for learning, experimentation, and portfolio development.