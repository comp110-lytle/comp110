"""Unit tests for remove_repeats."""

__author__ = "Viktorya Hunanyan <vhunany@unc.edu>"


import pytest
from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module
from graders.helpers import assert_return_type

MODULE = "lessons.list_repeats"


@mark.weight(0)
def test_author():
    """invert - __author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module)


@mark.weight(1)
def test_zip_params():
    """Part 1. remove_repeats should take a list of ints."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.remove_repeats, [list[int]])


@mark.weight(1)
def test_sum_return_type():
    """Part 1. remove_repeats should return None"""
    module = reimport_module(MODULE)
    assert_return_type(module.remove_repeats, None)


@mark.weight(1)
def test_one_check_for_return_value():
    """Part 1. Empty input list to check that the function has expected return value None."""
    from lessons.list_repeats import remove_repeats
    assert remove_repeats([]) == None


@mark.weight(2) 
def test_two_check_for_correct_mutation_for_list_with_repeats():
    """Part 1. Test for correct mutation of an input that has both sequentional repeated values and non-sequential repeated values."""
    from lessons.list_repeats import remove_repeats
    a: list[int] = [4, 8, 9, 4, 2, 2, 0, 9, 7, 10]
    remove_repeats(a)
    assert a == [4, 8, 9, 2, 0, 7, 10]


@mark.weight(2)
def test_two_check_for_correct_mutation_for_list_with_no_repeats():
    """Test for correct mutation of an input that has no repeated values."""
    from lessons.list_repeats import remove_repeats
    a: list[int] = [4, 8, 9, -1, 2, -2, 0, 19, 7, 10]
    remove_repeats(a)
    assert a == [4, 8, 9, -1, 2, -2, 0, 19, 7, 10]


