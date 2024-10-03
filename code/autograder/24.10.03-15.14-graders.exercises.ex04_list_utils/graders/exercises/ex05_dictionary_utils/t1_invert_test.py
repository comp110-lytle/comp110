"""Unit tests for dict_01"""

__author__ = "Kaki Ryan <kakiryan@live.unc.edu>"

import pytest
from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module
from graders.helpers import assert_return_type

MODULE = "exercises.ex05.dictionary"


@mark.weight(0)
def test_author():
    """invert - __author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module)


@mark.weight(4)
def test_invert_params():
    """invert - invert has 1 parameter of type dict[str,str]."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.invert, [dict[str, str]])


@mark.weight(4)
def test_invert_return_type():
    """invert - invert returns a dict[str,str]."""
    module = reimport_module(MODULE)
    assert_return_type(module.invert, dict[str, str])


@mark.weight(4)
def test_invert_1():
    """Invert test case 1."""
    from exercises.ex05.dictionary import invert
    all_same: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(all_same) == {'z': 'a', 'y': 'b', 'x': 'c'}


@mark.weight(4)
def test_invert_2():
    """Invert test case 2."""
    from exercises.ex05.dictionary import invert
    tied: dict[str, str] = {'apple': 'cat'}
    assert invert(tied) == {'cat': 'apple'}


@mark.weight(4)
def test_invert_error():
    """Correctly raises error"""
    from exercises.ex05.dictionary import invert
    yellow_wins: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
    with pytest.raises(KeyError):
        invert(yellow_wins)
