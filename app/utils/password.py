import base64
import hashlib
from .constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, PWD_ALGORITHM


def get_hash(password):
    x = hashlib.pbkdf2_hmac(
        PWD_ALGORITHM,
        password.encode('utf-8'),  # Convert the password to bytes
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    )
    return base64.b64encode(x)
