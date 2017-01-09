# This might be used at some point but as of now isn't needed

"""
from flask import jsonify

from RanobeHonyaku.api.v1 import api_v1


class APIError(Exception):

    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code

    def format_to_dict(self):
        return {
            "message": self.message,
            "error": self.status_code
        }


# Handles all errors that involve the API; Will return an error message and the response code
@api_v1.errorhandler(Exception)
def api_error_handler(error):
    return jsonify({"error": str(error)})
"""
