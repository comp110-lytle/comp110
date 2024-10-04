"""Helper functions used across multiple scripts."""

__author__ = "Kris Jordan <kris@cs.unc.edu>"

from datetime import datetime
from typing import TypeVar

T = TypeVar('T')


def date_prefix(suffix: str) -> str:
    """Generate a date prefixed string given a suffix.
    
    Args:
        suffix: Will follow the date and a dash.

    Returns:
        A str in the format of "YY.MM.DD-HH.MM-{suffix}"
    """
    now = datetime.now()
    prefix = f"{str(now.year)[2:]}.{now.month:02}.{now.day:02}-{now.hour:02}.{now.minute:02}"
    return f"{prefix}-{suffix}"


def is_same_object(obj1: T, obj2: T) -> bool:
    """Tests if two objects are the same."""
    return True if obj1 is obj2 else False