# B_format
Guide
Setup:

Install requests: pip install requests

Create combo.txt with credentials (format: username:password per line)

Modify LOGIN_URL, HEADERS, and PAYLOAD_TEMPLATE fields as needed

How it works:

Reads each line from combo.txt

Sends POST request with username/password

Checks if response has token field (change this based on API response)

Saves valid combos to valid.txt

Customization:

Change "user" and "pass" to match API field names (e.g., "email", "phone", "password")

Change "token" to whatever indicates success (e.g., "access_token", "success")

Add more headers like Authorization or User-Agent if needed

