from abuseipdb import check_ip
import json

# Google's public DNS (usually has a very low abuse score)
ip = "8.8.8.8"

result = check_ip(ip)

print(json.dumps(result, indent=4))
