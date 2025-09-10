import http.client
import ssl
import json

# Disable SSL certificate verification for testing
context = ssl._create_unverified_context()

conn = http.client.HTTPSConnection("advertisement-management-api-91xh.onrender.com", context=context)

print("Sending request to /api/jobs/")
conn.request("GET", "/api/jobs/")

res = conn.getresponse()
data = res.read()

print(f"Status: {res.status} {res.reason}")
print("Headers:")
for header, value in res.getheaders():
    print(f"  {header}: {value}")

print("\nResponse:")
try:
    # Try to parse as JSON
    json_data = json.loads(data.decode("utf-8"))
    print(json.dumps(json_data, indent=2))
except json.JSONDecodeError:
    # If not JSON, print raw response
    print(data.decode("utf-8"))
