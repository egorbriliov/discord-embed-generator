"""Содержит все переменные .env в классе Env."""

from dotenv import dotenv_values


class Env:
    """Содержит все переменные .env."""

    TOKEN = dotenv_values(".env")['TOKEN']
