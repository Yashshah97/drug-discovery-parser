"""
Core parsing logic for the drug discovery file format.

This module contains the main parser class and its associated methods.
"""

class Parser:
    """
    A streaming parser for the drug discovery file format.

    This parser is designed to be used in conjunction with a validating reader,
    which checks that the input data conforms to the expected structure.
    """

    def __init__(self):
        """Initialize the parser."""
        self.current_token = None

    def parse(self, tokens):
        """
        Parse the given list of tokens.

        :param tokens: A list of tokens representing the file format.
        :return: The parsed data.
        """
        self.tokens = tokens
        return self._parse()

    def _parse(self):
        """Recursively parse the tokens."""
        if not self.tokens:
            raise ValueError("Unexpected end of input")

        token = self.tokens.pop(0)
        if token == 'START':
            return self._parse_header()
        elif token == 'END':
            return self._parse_footer()
        else:
            raise ValueError(f"Unknown token: {token}")

    def _parse_header(self):
        """Parse the header section of the file format."""
        if not self.tokens:
            raise ValueError("Missing header data")

        token = self.tokens.pop(0)
        if token == 'HEADER':
            return {'header': self._parse_string()}
        else:
            raise ValueError(f"Expected HEADER, got {token}")

    def _parse_footer(self):
        """Parse the footer section of the file format."""
        if not self.tokens:
            raise ValueError("Missing footer data")

        token = self.tokens.pop(0)
        if token == 'FOOTER':
            return {'footer': self._parse_string()}
        else:
            raise ValueError(f"Expected FOOTER, got {token}")

    def _parse_string(self):
        """Parse a string section of the file format."""
        if not self.tokens:
            raise ValueError("Missing string data")

        token = self.tokens.pop(0)
        if token == 'STRING':
            return {'string': self._parse_value()}
        else:
            raise ValueError(f"Expected STRING, got {token}")

    def _parse_value(self):
        """Parse a value section of the file format."""
        if not self.tokens:
            raise ValueError("Missing value data")

        token = self.tokens.pop(0)
        if token == 'VALUE':
            return {'value': self._parse_number()}
        else:
            raise ValueError(f"Expected VALUE, got {token}")

    def _parse_number(self):
        """Parse a number section of the file format."""
        if not self.tokens:
            raise ValueError("Missing number data")

        token = self.tokens.pop(0)
        try:
            return {'number': float(token)}
        except ValueError:
            raise ValueError(f"Invalid number: {token}")
