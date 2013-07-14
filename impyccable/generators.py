"""Data set generators."""
__author__ = 'Taylor "Nekroze" Lawson'
__email__ = 'nekroze@eturnilnetwork.com'
import random
import string
import sys


# Constants
MIN_INT = -sys.maxsize - 1
MAX_INT = sys.maxsize
MIN_FLOAT = -1e7
MAX_FLOAT = 1e7
LIST_LEN = 30


# Basic Types
def String(least=0, most=LIST_LEN, valid=None):
    """
    Returns a generator that will endlessly pump out random strings of a length
    >= least and <= most, constiting of strings/chars from the valid selection.

    The valid argument should be a list of string or a string of characters and
    defaults to all printable characters as defined in ``string.printable``.
    """
    if valid is None:
        valid = string.printable
    while True:
        length = random.randint(least, most)
        yield ''.join([random.choice(valid) for _ in range(length)])


def Integer(least=MIN_INT, most=MAX_INT):
    """
    Returns a generator that endlessly returns random integers >= lest and <=
    most.
    """
    while True:
        yield random.randint(least, most)


def Float(least=MIN_FLOAT, most=MAX_FLOAT):
    """
    Returns a generator that endlessly returns random floats >= lest and <=
    most.
    """
    while True:
        yield random.uniform(least, most)


def Boolean():
    """
    Returns a generator that endlessly returns random True or False.
    """
    while True:
        yield random.choice([True, False])


# Collections
