"""Содержит все переменные .env в классе Env."""

from dotenv import dotenv_values


class Enviroment:
    """Contains all .env values."""

    VALUES = dotenv_values(".env")

    @classmethod
    def get(cls, name: str):
        """Return value by name if exists."""
        try:
            return cls.VALUES[name]
        except KeyError:
            raise KeyError(f'Name {name} not exists in .env') from None
