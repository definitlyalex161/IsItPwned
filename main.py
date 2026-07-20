import hashlib
import getpass
import requests

def get_pwned_count(password):
    # Hash password using SHA-1
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]

    # Query API using k-Anonymity prefix
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"API Error: {response.status_code}")

    # Parse hashes returned by API
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

def main():
    print("--- IsItPwned ---")
    password = getpass.getpass("Enter password: ")

    if not password:
        print("No password entered.")
        return

    try:
        count = get_pwned_count(password)
        if count > 0:
            print(f"[!] Warning: Password leaked {count} times!")
        else:
            print("[+] Good news: Password not found in known leaks.")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == '__main__':
    main()

cat << 'EOF' > main.py 
import hashlib
import getpass
import requests

def get_pwned_count(password):
    # Hash password using SHA-1
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]

    # Query API using k-Anonymity prefix
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"API Error: {response.status_code}")

    # Parse hashes returned by API
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

def main():
    print("--- IsItPwned ---")
    password = getpass.getpass("Enter password: ")

    if not password:
        print("No password entered.")
        return

    try:
        count = get_pwned_count(password)
        if count > 0:
            print(f"[!] Warning: Password leaked {count} times!")
        else:
            print("[+] Good news: Password not found in known leaks.")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == '__main__':
    main()

