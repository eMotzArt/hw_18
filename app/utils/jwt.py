import datetime
import calendar

import jwt

from .constants import JWT_SECRET, JWT_ALGORITHM


def generate_token(data):
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    data["exp"] = calendar.timegm(min30.timetuple())

    return jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)


def check_token(token):
    try:
        jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return True
    except Exception:
        return False
