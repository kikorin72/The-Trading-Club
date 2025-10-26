from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    # Truncate to 72 bytes for bcrypt
    max_bytes = 72
    safe_password = password.encode("utf-8")[:max_bytes].decode("utf-8", "ignore")
    return pwd_context.hash(safe_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    max_bytes = 72
    safe_password = plain_password.encode("utf-8")[:max_bytes].decode("utf-8", "ignore")
    return pwd_context.verify(safe_password, hashed_password)
