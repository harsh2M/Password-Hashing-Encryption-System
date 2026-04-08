import json
from password_manager import PasswordManager
from encryption import EncryptionManager

DB_FILE = "database.json"

pm = PasswordManager()
em = EncryptionManager()

def load_db():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def register():
    db = load_db()

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in db:
        print("User already exists!")
        return

    hashed_password = pm.hash_password(password)

    db[username] = {
        "password": hashed_password,
        "secret": ""
    }

    save_db(db)
    print("User registered successfully!")

def login():
    db = load_db()

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username not in db:
        print("User not found!")
        return None

    stored_hash = db[username]["password"]

    if pm.verify_password(password, stored_hash):
        print("Login successful!")
        return username
    else:
        print("Invalid password!")
        return None

def store_secret(username):
    db = load_db()

    secret = input("Enter secret to store: ")
    encrypted = em.encrypt(secret)

    db[username]["secret"] = encrypted
    save_db(db)

    print("Secret stored securely!")

def view_secret(username):
    db = load_db()

    encrypted = db[username]["secret"]

    if not encrypted:
        print("No secret stored.")
        return

    decrypted = em.decrypt(encrypted)
    print("Your secret:", decrypted)

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            register()

        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\n1. Store Secret")
                    print("2. View Secret")
                    print("3. Logout")

                    sub_choice = input("Choose: ")

                    if sub_choice == "1":
                        store_secret(user)
                    elif sub_choice == "2":
                        view_secret(user)
                    elif sub_choice == "3":
                        break

        elif choice == "3":
            break

if __name__ == "__main__":
    main()