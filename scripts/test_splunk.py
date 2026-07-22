from splunk_client import get_unique_failed_ips

ips = get_unique_failed_ips()

print("\nUnique attacker IPs\n")

for ip in ips:
    print(ip)
