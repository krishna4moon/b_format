# B_format
```
# ===== CONFIGURATION =====
LOGIN_URL = "https://example.com/api/login"
COMBO_FILE = "combo.txt"
OUTPUT_FILE = "valid.txt"

```

## 📘 Usage Guide

### Installation
```bash
pip install requests
```

### Input Format (`combo.txt`)
```
username1:password1
username2:password2
email@example.com:pass123
```

### Output (`valid.txt`)
- Automatically created with working credentials

### Customization

| Variable | Purpose |
|----------|---------|
| `LOGIN_URL` | Target API endpoint |
| `"user"` / `"pass"` | Field names expected by API |
| `"token"` | Success indicator in response |

### Example Modifications

**For email + password:**
```python
PAYLOAD_TEMPLATE = {
    "email": "",
    "password": ""
}
# Then check: resp.json().get("access_token")
```

**With additional headers:**
```python
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "YourApp/1.0",
    "Authorization": "Bearer token_here"
}
```

### Notes
- Remove/rename `combo.txt` and `valid.txt` as needed
- Adjust success condition (`resp.json().get("token")`) based on actual API response
- Add delays (`time.sleep()`) to avoid rate limiting
