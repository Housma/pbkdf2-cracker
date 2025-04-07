#!/usr/bin/env python3

import hashlib
import binascii
import argparse
import os


def pbkdf2_hash(password, salt, iterations=50000, dklen=50):
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        iterations,
        dklen
    )


def find_matching_password(dictionary_file, target_hash, salt_hex, iterations=50000, dklen=50):
    try:
        salt = binascii.unhexlify(salt_hex)
        target_hash_bytes = binascii.unhexlify(target_hash)
    except binascii.Error:
        print("[!] Invalid hex value for hash or salt.")
        return

    if not os.path.exists(dictionary_file):
        print(f"[!] Wordlist not found: {dictionary_file}")
        return

    print("[+] Starting brute-force...")

    with open(dictionary_file, 'r', encoding='utf-8', errors='ignore') as file:
        for count, line in enumerate(file, 1):
            password = line.strip()
            hash_value = pbkdf2_hash(password, salt, iterations, dklen)
            if hash_value == target_hash_bytes:
                print(f"\n[+] Password found after {count} tries: {password}")
                return password
            if count % 1000 == 0:
                print(f"[-] Tried {count} passwords...", end='\r')

    print("\n[!] Password not found in the wordlist.")
    return None


def main():
    parser = argparse.ArgumentParser(description="Crack PBKDF2-HMAC-SHA256 password hashes")
    parser.add_argument("--hash", required=True, help="Target hash (hex string)")
    parser.add_argument("--salt", required=True, help="Salt used in hashing (hex string)")
    parser.add_argument("--wordlist", required=True, help="Path to dictionary file")
    parser.add_argument("--iterations", type=int, default=50000, help="Number of iterations (default: 50000)")
    parser.add_argument("--dklen", type=int, default=50, help="Output key length (default: 50 bytes)")
    args = parser.parse_args()

    find_matching_password(args.wordlist, args.hash, args.salt, args.iterations, args.dklen)


if __name__ == "__main__":
    main()
