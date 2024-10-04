"""Tests for Exercise 04 - Data Wrangling."""

__author__ = "Kaki Ryan <kakiryan@cs.unc.edu>"

from pytest import mark
from graders.helpers import assert_parameter_list, reimport_module
from graders.helpers import assert_return_type
from random import randint


MODULE = "exercises.ex05.dictionary"


@mark.weight(7.5)
def test_count_params():
    """data_utils.py - count takes in a list[str]."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.count, [list[str]])


@mark.weight(7.5)
def test_count_return_type():
    """data_utils.py - count returns a dict[str, int]."""
    module = reimport_module(MODULE)
    assert_return_type(module.count, dict[str, int])


@mark.weight(7.5)
def test_count_1():
    """data_utils.py - count returns the correct counts with a small list of values."""
    module = reimport_module(MODULE)
    values = ["Kaki", "Kaki", "Lily", "Ada", "Nellie", "Krackle", "Lily"]
    assert module.count(values) == {'Kaki': 2, 'Lily': 2, 'Ada': 1, 'Nellie': 1, "Krackle": 1}


@mark.weight(7.5)
def test_count_2():
    """data_utils.py - count returns the correct counts with a large list of values."""
    module = reimport_module(MODULE)
    values = ["Kaki", "Kaki", "Lily", "Ada", "Nellie", "Krackle", "Lily"] 
    for i in range(0, 100):
        choice = randint(0, 6)
        values.append(values[choice])
    expected: dict[str, int] = {}
    for value in values:
        if value in expected:
            expected[value] += 1
        else:
            expected[value] = 1
    assert module.count(values) == expected