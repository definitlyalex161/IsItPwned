import hashlib
import getpass
# import requests  # Brauchen wir später für die API-Abfrage

def generate_sha1_hash(password):
    """
    Nimmt ein Passwort als Text, wandelt es in einen SHA-1-Hash um
    und gibt diesen als großen Text (Uppercase) zurück.
    """
    # TODO: Nutze hashlib.sha1(), um das Passwort zu hashen
    pass

def fetch_api_data(hash_prefix):
    """
    Sendet die ersten 5 Zeichen des Hashes an die 'Have I Been Pwned'-API
    und gibt die Antwort (alle passenden Suffixe) zurück.
    """
    # TODO: Sende einen GET-Request an https://api.pwnedpasswords.com/range/{hash_prefix}
    pass

def check_pwned_count(api_response, hash_suffix):
    """
    Durchsucht die API-Antwort nach unserem restlichen Hash (Suffix).
    Gibt zurück, wie oft das Passwort geleakt wurde (oder 0, wenn es sicher ist).
    """
    # TODO: Zeile für Zeile prüfen, ob unser hash_suffix in der Antwort steht
    pass

def main():
    print("========================================")
    print("       🔒 Willkommen bei IsItPwned 🔒")
    print("========================================\n")

    # getpass sorgt dafür, dass das Passwort beim Tippen unsichtbar bleibt (wie bei sudo)
    password = getpass.getpass("Zu prüfendes Passwort eingeben: ")

    if not password:
        print("Kein Passwort eingegeben. Abbruch.")
        return

    print("\n[+] Generiere Hash...")
    # hash_full = generate_sha1_hash(password)
    
    print("[+] Kontaktiere Have I Been Pwned API (k-Anonymity)...")
    # prefix = hash_full[:5]
    # suffix = hash_full[5:]
    # response = fetch_api_data(prefix)
    
    print("[+] Werte Ergebnisse aus...")
    # leaks = check_pwned_count(response, suffix)
    
    # print(f"\nErgebnis: Das Passwort wurde {leaks} mal in Datenlecks gefunden.")
    print("\nSkelett läuft! Jetzt müssen wir nur noch die TODOs mit Code füllen.")

# Dieser Block sorgt dafür, dass main() nur ausgeführt wird, 
# wenn du die Datei direkt startest (python main.py)
if __name__ == '__main__':
    main()
