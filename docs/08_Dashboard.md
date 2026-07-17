# Installation Guide

## AWS Infrastructure

- Created two Ubuntu EC2 instances
- Splunk Enterprise Server
- Ubuntu SSH Victim

## Kali Linux

- Installed on VirtualBox
- Used as attacker

## Splunk

- Installed Splunk Enterprise
- Enabled receiving on TCP 9997

## Universal Forwarder

Installed on Ubuntu victim.

Forwarded:

- /var/log/auth.log

Index:

linux_auth