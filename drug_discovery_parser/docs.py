"""
Module for documentation generation and metadata management.
"""

__version__ = '1.0'
__author__ = 'Your Name'

def get_description():
    """
    Returns a short description of the project.

    :return: str
    """
    return "Drug Discovery File-Format Parser"

def get_long_description():
    """
    Returns a long description of the project.

    :return: str
    """
    return """\
A file-format parser for molecular screening and cheminformatics:
a streaming parser with a validating reader and friendly error messages,
built in pure Python with tests and documentation.
"""

def get_metadata():
    """
    Returns metadata about the project.

    :return: dict
    """
    return {
        'name': 'drug-discovery-parser',
        'version': __version__,
        'author': __author__,
        'description': get_description(),
        'long_description': get_long_description()
    }
