"""Tests for Dict Utils Part 1."""

__author__ = "Kaki Ryan <kakiryan@cs.unc.edu>"

from pytest import mark
from graders.helpers import assert_parameter_list, reimport_module
from graders.helpers import assert_return_type


MODULE = "exercises.ex05.dictionary"


@mark.weight(3)
def test_count_params():
    """count - count takes in a list[str]."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.count, [list[str]])


@mark.weight(3)
def test_count_return_type():
    """count - count returns a dict[str, int]."""
    module = reimport_module(MODULE)
    assert_return_type(module.count, dict[str, int])


@mark.weight(3)
def test_count_1():
    """count - count returns the correct counts with a small list of values."""
    module = reimport_module(MODULE)
    values = ["Kaki", "Kaki", "Lily", "Ada", "Nellie", "Krackle", "Lily"]
    assert module.count(values) == {'Kaki': 2, 'Lily': 2, 'Ada': 1, 'Nellie': 1, "Krackle": 1}
