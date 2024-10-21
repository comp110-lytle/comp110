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


@mark.weight(4)
def test_invert_params():
    """invert - invert has 1 parameter of type dict[str, str]."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.invert, [dict[str, str]])

@mark.weight(4)
def test_invert_return_type():
    """invert - invert returns a dict[str, str]."""
    module = reimport_module(MODULE)
    assert_return_type(module.invert, dict[str, str])

@mark.weight(5)
def test_invert_correct():
    """invert - inverts correctly switches key-value pairs."""
    module = reimport_module(MODULE)
    all_same: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert module.invert(all_same) == {'z': 'a', 'y': 'b', 'x': 'c'}

@mark.weight(4)
def test_invert_key_error():
    """invert - raises KeyError when duplicate values exist."""
    module = reimport_module(MODULE)
    with pytest.raises(KeyError):
        module.invert({'kris': 'jordan', 'michael': 'jordan'})

@mark.weight(5)
def test_invert_empty():
    """invert - handles empty dictionary."""
    module = reimport_module(MODULE)
    assert module.invert({}) == {}