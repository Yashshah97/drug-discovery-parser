"""
A validating reader for the Drug Discovery File-Format Parser.

This module provides a validating reader that checks the correctness of parsed data.
"""

class Reader:
    """
    A validating reader for the Drug Discovery File-Format Parser.

    This class ensures that parsed data is correct by checking against a set of predefined rules.
    """

    def __init__(self, lines):
        """
        Initialize the reader with a list of lines to parse.

        :param lines: A list of strings representing the file contents
        """
        self.lines = lines

    def _parse_line(self, line):
        """
        Parse a single line and return its parsed value.

        :param line: A string representing a single line in the file
        :return: The parsed value for the given line
        """
        # For demonstration purposes only. Replace with actual parsing logic.
        return line.strip()

    def _validate_line(self, line):
        """
        Validate a single line against predefined rules.

        :param line: A string representing a single line in the file
        :return: Whether the line is valid or not
        """
        # For demonstration purposes only. Replace with actual validation logic.
        return True

    def read(self):
        """
        Read and parse all lines, validating each one along the way.

        :return: A list of parsed values for each line in the file
        """
        parsed_values = []
        for line in self.lines:
            if not self._validate_line(line):
                raise ValueError(f"Invalid line: {line}")
            parsed_value = self._parse_line(line)
            parsed_values.append(parsed_value)
        return parsed_values

def main():
    # For demonstration purposes only. Replace with actual usage.
    lines = ["Line 1", "Line 2", "Line 3"]
    reader = Reader(lines)
    try:
        parsed_values = reader.read()
        print(parsed_values)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
