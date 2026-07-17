# Detection Rules

## SSH Brute Force Detection

Description

Detects five or more failed SSH logins from the same IP within two minutes.

Detection Logic

- Extract source IP
- Count failed attempts
- Trigger when count >= 5

Purpose

Detect brute-force attacks.

---

## Successful Login After Multiple Failures

Description

Detects successful authentication after multiple failed attempts.

Purpose

Identify compromised accounts following brute-force attacks.