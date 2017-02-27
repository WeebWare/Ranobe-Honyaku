from passlib.hash import scrypt

from RanobeHonyaku.errors import InvalidCredentials


def encrypt_password(password) -> str:
    return scrypt(password)


def validate_password(unhashed_password, hashed_password) -> bool:
    if not scrypt.verify(unhashed_password, hashed_password):
        raise InvalidCredentials
    return True
