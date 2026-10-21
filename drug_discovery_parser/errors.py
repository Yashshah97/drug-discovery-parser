"""
Friendly error messages for common parsing errors.
"""

class ParsingError(Exception):
    """Base class for all parsing-related exceptions."""
    pass


class InvalidFileFormat(ParsingError):
    """
    Raised when the file format is not recognized or supported.

    :param msg: A message describing the error, including the expected file format.
    """
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)


class InvalidData(ParsingError):
    """
    Raised when data in the file is invalid or malformed.

    :param msg: A message describing the error, including any relevant details about the invalid data.
    """
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)


class UnexpectedToken(ParsingError):
    """
    Raised when an unexpected token is encountered while parsing.

    :param expected_token: The token that was expected at this point in the file.
    :param actual_token: The token that was actually encountered.
    """
    def __init__(self, expected_token, actual_token):
        self.expected_token = expected_token
        self.actual_token = actual_token
        msg = f"Unexpected token '{actual_token}' (expected '{expected_token}')"
        super().__init__(msg)


class MissingRequiredField(ParsingError):
    """
    Raised when a required field is missing from the file.

    :param field_name: The name of the missing field.
    """
    def __init__(self, field_name):
        self.field_name = field_name
        msg = f"Missing required field '{field_name}'"
        super().__init__(msg)
