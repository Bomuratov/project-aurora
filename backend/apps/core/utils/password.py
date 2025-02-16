import bcrypt

def hashing_password(password: str) -> str:
    salt = bcrypt.gensalt()
    password_bytes: bytes = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password.decode("utf-8")


def validate_password(password: str, hashed_password: bytes)-> bool:
    return bcrypt.checkpw(password=password.encode("utf-8"), hashed_password=hashed_password.encode("utf-8"),)


