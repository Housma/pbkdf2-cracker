# 🔐 PBKDF2 Cracker

A simple Python script to crack `PBKDF2-HMAC-SHA256` password hashes using a wordlist.  
Used by platforms like **Gitea**, **GitLab**, and other secure applications.

I used this tool to successfully crack a password during the HTB CTF **Titanic** challenge.  

---

## 🚀 Features

- Supports:
  - Custom salt (hex)
  - Iteration count (default: 50000)
  - Output key length (`dkLen`, default: 50 bytes)
- Brute-force password recovery via wordlists
- Includes test mode for verifying known hashes
- Works with Gitea / GitLab exports

---

## 📦 Installation

```bash
git clone https://github.com/Housma/pbkdf2-cracker.git
cd pbkdf2-cracker
python3 pbkdf2_cracker.py --help
```

> 💡 No external libraries needed — just Python 3.6+

---

## 🧪 Hash Type

This tool cracks:

```
PBKDF2-HMAC-SHA256
```

Format:
```
pbkdf2$<iterations>$<dklen>$<salt>$<hash>
```

---

## 🛠️ Usage

### 🔹 Basic Syntax

```bash
python3 pbkdf2_cracker.py \
  --hash <hex_encoded_hash> \
  --salt <hex_encoded_salt> \
  --wordlist /path/to/wordlist.txt
```

### 🔹 Optional Arguments

| Option         | Description                        | Default     |
|----------------|------------------------------------|-------------|
| `--iterations` | PBKDF2 iteration count              | `50000`     |
| `--dklen`      | Derived key output length in bytes | `50`        |

---

### ✅ Example
Passwd: e531d398946137baea70ed6a680a54385ecff131309c0bd8f225f284406b7cbc8efc5dbef30bf1682619263444ea594cfb56

Salt: 8bf3e3452b78544f8bee9400d6936d34

```bash
python3 pbkdf2_cracker.py \
  --hash e531d398946137baea70ed6a680a54385ecff131309c0bd8f225f284406b7cbc8efc5dbef30bf1682619263444ea594cfb56 \
  --salt 8bf3e3452b78544f8bee9400d6936d34 \
  --wordlist /usr/share/wordlists/rockyou.txt
```

---

## 🔍 Test Mode

Use test mode to verify known hash-password pairs built into the script:

```bash
python3 pbkdf2_cracker.py --test
```

---

## ✅ Example Output

```
[+] Starting brute-force...
[-] Tried 1000 passwords...
[-] Tried 2000 passwords...
[+] Password found after 3467 tries: 25282528
```


---

## ⚠️ Disclaimer

This tool is intended for **educational purposes** and **authorized penetration testing** only.  
Do not use against systems without permission.

---
