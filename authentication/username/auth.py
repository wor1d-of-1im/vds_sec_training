# auth.py

VALID_USERNAME = "antivirus"
VALID_PASSWORD = "password"

def login_check(username, password):
    if username != VALID_USERNAME:
        return "Invalid username"
    
    if password != VALID_PASSWORD:
        return "Incorrect password"
    
    return "SUCCESS"