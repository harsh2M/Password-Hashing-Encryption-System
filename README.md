# Password-Hashing-Encryption-System
A beginner-to-intermediate Python project demonstrating secure password handling and data encryption, designed to mirror real-world authentication systems.

📌 Features
🔐 Password Hashing (bcrypt)
Secure, salted hashing
Industry-standard approach
Passwords are never stored in plain text

🔁 Encryption & Decryption (Fernet)
Store sensitive user data securely
Reversible encryption using a secret key

👤 User Authentication
Register new users
Login with password verification

🗄️ Local Storage
JSON-based database (database.json)

🔒 Secret Storage
Users can store and retrieve encrypted secrets

🧠 Concepts Covered

This project is built for learning core security concepts:

Hashing vs Encryption
Salt and why it matters
Secure password verification
Key-based encryption
Key management basics

🏗️ Project Structure

auth_project/
│
├── password_manager.py   # Handles password hashing (bcrypt)
├── encryption.py         # Handles encryption/decryption (Fernet)
├── database.json         # Simple JSON database
├── app.py                # Main CLI application

⚙️ Installation
Clone or download the project
Install dependencies:
pip install bcrypt cryptography
▶️ Usage

Run the application:

python app.py
Available Options:
Register a new user
Login with existing credentials
Store a secret (encrypted)
View stored secret (decrypted)

🔑 How It Works
Password Security
Passwords are hashed using bcrypt
Each password is salted automatically
Stored hashes cannot be reversed
Encryption
User secrets are encrypted using Fernet
Requires a secret key for decryption

⚠️ Important Notes
Passwords are not recoverable (by design)
If the encryption key is lost → encrypted data is unrecoverable
If the key is leaked → all encrypted data is exposed

🚧 Limitations (Learning Project)
Uses JSON instead of a real database
No password strength validation
No rate limiting or brute-force protection
Encryption key handling is basic

