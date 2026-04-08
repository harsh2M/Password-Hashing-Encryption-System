import bcrypt

class PasswordManager:
    def __init__(self, rounds=12):
        self.rounds = rounds

    def hash_password(self, password: str) -> str:
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(self.rounds))
        return hashed.decode('utf-8')

    def verify_password(self, password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed.encode('utf-8'))