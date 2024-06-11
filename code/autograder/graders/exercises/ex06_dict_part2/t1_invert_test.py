"""Tests for Exercise 07: Dict Functions + Unit Tests."""

__author__ = "Kaki Ryan <kakiryan@live.unc.edu>"

import pytest
from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module
from graders.helpers import assert_return_type

MODULE = "ex05.dictionary"


@mark.weight(2)
def test_invert_1():
    """invert - invert is correct when given an empty dictionary."""
    from ex05.dictionary import invert
    empty: dict[str, str] = {}
    assert invert(empty) == {}


@mark.weight(3)
def test_invert_2():
    """invert - invert is correct for a large input dictionary."""
    from ex05.dictionary import invert
    low: dict[str, str] = {'apple': 'bottom', 'jeans': 'boots', 'with': 'the', 'fur': 'apple'}
    assert invert(low) == {'bottom': 'apple', 'boots': 'jeans', 'the': 'with', 'apple': 'fur'}


@mark.weight(3)
def test_invert_error():
    """invert - invert correctly raises error."""
    from ex05.dictionary import invert
    bad_dict: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
    with pytest.raises(KeyError):
        invert(bad_dict)
