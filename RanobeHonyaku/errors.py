class RanobeHonyakuException(Exception):
    pass


class InvalidCredentials(RanobeHonyakuException):
    pass


class NoPassedData(RanobeHonyakuException):
    pass


error_messages = {
    "ACCOUNT_NON_EXISTANT": "Account doesn't exist.",
    "ACCOUNT_REGISTERED": "Account already registered.",
    "INCORRECT_PASSWORD": "Incorrect password."
}
