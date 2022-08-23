import base64
import hashlib
import hmac

from .constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, PWD_ALGORITHM


def get_hash(password):
    x = hashlib.pbkdf2_hmac(
        PWD_ALGORITHM,
        password.encode('utf-8'),  # Convert the password to bytes
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    )
    return base64.b64encode(x)

def is_passwords_equals(first_password, second_password):
    first_password = base64.b64decode(first_password)
    second_password = base64.b64decode(second_password)
    return hmac.compare_digest(first_password, second_password)
