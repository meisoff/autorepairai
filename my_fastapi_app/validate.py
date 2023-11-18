import re
from db import database as db

def validate_email(email: str):
    # Паттерн для валидации почты
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Проверка соответствия почты паттерну
    if re.match(pattern, email):
        email = db.Account.select().where(
            db.Account.login == email)
        if not email:
            return True, "Можно регистрировать"
        else:
            return False, "Пользователь с таким email зарегистрирован"
    else:
        return False, "Некорректный формат для логина. Введите свою почту."


def validate_password(password):
    reasons = []

    # Пароль должен содержать минимум 8 символов
    if len(password) < 8:
        reasons.append("Пароль должен содержать минимум 8 символов")

    # Пароль должен содержать как минимум одну цифру
    if not any(char.isdigit() for char in password):
        reasons.append("Пароль должен содержать как минимум одну цифру")

    # Пароль должен содержать как минимум одну букву в верхнем регистре
    if not any(char.isupper() for char in password):
        reasons.append("Пароль должен содержать как минимум одну букву в верхнем регистре")

    # Пароль должен содержать как минимум одну букву в нижнем регистре
    if not any(char.islower() for char in password):
        reasons.append("Пароль должен содержать как минимум одну букву в нижнем регистре")

    # Пароль должен содержать как минимум один специальный символ
    if not any(char in '!@#$%^&*()_+-={}[]|\:;"<>,.?/~`' for char in password):
        reasons.append("Пароль должен содержать как минимум один специальный символ")

    if reasons:
        return False, reasons
    else:
        return True, reasons

