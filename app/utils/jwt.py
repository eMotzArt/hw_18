import datetime
import calendar

import jwt

from .constants import JWT_SECRET, JWT_ALGORITHM


def generate_access_token(**data):
    """Генерирует 30 минутый токен """
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    data["exp"] = calendar.timegm(min30.timetuple())

    return jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

def generate_refresh_token(**data):
    """Генерирует 30 дневный refresh-токен"""
    days30 = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    data["exp"] = calendar.timegm(days30.timetuple())

    return jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

def generate_tokens(**data):
    """Генерирует access и refresh токены и возращает словарем"""
    access_token = generate_access_token(**data)
    refresh_token = generate_refresh_token(**data)
    return {"access_token": access_token,
            "refresh_token": refresh_token}

def decode_token(token):
    """Декодирует токен"""
    return jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)


def check_token(token):
    """Возвращает True если токен декодирован и валиден"""
    try:
        jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return True
    except Exception as e:
        print(e)
        return False
