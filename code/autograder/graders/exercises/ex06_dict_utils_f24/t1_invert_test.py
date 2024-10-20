"""Unit tests for dict_01"""

__author__ = "Kaki Ryan <kakiryan@live.unc.edu>"
__author__ = "Viktorya Hunanyan <vhunany@unc.edu>"


import pytest
from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module
from graders.helpers import assert_return_type

MODULE = "exercises.ex06.dictionary"

# GOAL: To check for signatures, and very basic functionality. 
# Edge cases must be checked and fulfilled in Part 2 using Unit Testing.


@mark.weight(0)
def test_author():
    """dictionary.py - __author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module)


@mark.weight(2)
def test_invert_params():
    """invert - invert has 1 parameter of type dict[str, str]."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.invert, [dict[str, str]])


@mark.weight(2)
def test_invert_return_type():
    """invert - invert returns a dict[str, str]."""
    module = reimport_module(MODULE)
    assert_return_type(module.invert, dict[str, str])


@mark.weight(2)
def test_invert_1():
    """invert - inverts correctly switches key-value pairs."""
    module = reimport_module(MODULE)
    all_same: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert module.invert(all_same) == {'z': 'a', 'y': 'b', 'x': 'c'}

@mark.weight(2)
def test_invert_key_error():
    """invert - raises KeyError when duplicate values exist."""
    module = reimport_module(MODULE)
    with pytest.raises(KeyError):
        module.invert({'kris': 'jordan', 'michael': 'jordan'})


@mark.weight(2)
def test_invert_empty():
    """invert - handles empty dictionary."""
    module = reimport_module(MODULE)
    assert module.invert({}) == {}

@mark.weight(2)
def test_invert_1():
    """invert - invert is correct when given an empty dictionary."""
    module = reimport_module(MODULE)
    empty: dict[str, str] = {}
    assert module.invert(empty) == {}


@mark.weight(2)
def test_invert_2():
    """invert - invert is correct for a large input dictionary."""
    module = reimport_module(MODULE)
    low: dict[str, str] = {'apple': 'bottom', 'jeans': 'boots', 'with': 'the', 'fur': 'apple'}
    assert module.invert(low) == {'bottom': 'apple', 'boots': 'jeans', 'the': 'with', 'apple': 'fur'}


@mark.weight(2)
def test_invert_error():
    """invert - invert correctly raises error."""
    module = reimport_module(MODULE)
    bad_dict: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
    with pytest.raises(KeyError):
        module.invert(bad_dict)

@mark.weight(2)
def test_invert_key_error():
    """invert - raises KeyError when duplicate values exist."""
    module = reimport_module(MODULE)
    with pytest.raises(KeyError):
        module.invert({'kris': 'jordan', 'michael': 'jordan'})


@mark.weight(2)
def test_invert_empty():
    """invert - handles empty dictionary."""
    module = reimport_module(MODULE)
    assert module.invert({}) == {}