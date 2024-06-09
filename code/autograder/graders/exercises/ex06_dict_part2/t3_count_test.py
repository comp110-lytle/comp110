"""Tests for Exercise 07: Dict Functions + Unit Tests."""

__author__ = "Kaki Ryan <kakiryan@cs.unc.edu>"

from pytest import mark
from graders.helpers import assert_parameter_list, import_module, reimport_module
from graders.helpers import assert_return_type
from random import randint


MODULE = "ex05.dictionary"


@mark.weight(4)
def test_count_1():
    """count - count returns the correct counts with a small list of values."""
    try:
        module = import_module(MODULE)
        values = ["Vrinda", "vrinda", "Kaleb", "Alyssa", "Kaleb", "Kaleb"]
        assert module.count(values) == {'Vrinda': 1, 'vrinda': 1, 'Kaleb': 3, 'Alyssa': 1}
    except:
        assert False, f"Unable to import {MODULE}"

@mark.weight(4)
def test_count_2():
    """count - count returns the correct counts with a large list of values."""
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
