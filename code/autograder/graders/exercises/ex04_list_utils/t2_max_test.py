"""Unit tests for max."""

__author__ = "730225231"

import pytest
from pytest import mark


def _test_max(list: list[int], expected: int) -> None:
    """Helper function for necessary checks"""
    from exercises.ex04_utils import max
    assert max(list) == expected


@mark.timeout(3)
@mark.weight(4)
def test_use_case1():
    """max - Ascending list of unique ints. (Use Case.)"""
    _test_max([1, 2, 3, 4, 5], 5)


@mark.timeout(3)
@mark.weight(4)
def test_use_case2():
    """max - Descending list of unique ints. (Use Case.)"""
    _test_max([5, 4, 3, 2, 1], 5)


@mark.timeout(3)
@mark.weight(4)
def test_use_case3():
    """max - Scrambled list of unique ints. (Use Case.)"""
    _test_max([3, 5, 3, 4, 1], 5)


@mark.timeout(3)
@mark.weight(2)
def test_repeats():
    """max - Max int appears more than once. (Edge Case.)"""
    _test_max([5, 1, 2, 3, 5, 4], 5)



@mark.timeout(3)
@mark.weight(2)
def test_zero():
    """max - Max int is a negative number. (Edge Case.)"""
    _test_max([-5, -2, -3, -1], -1)


@mark.timeout(3)
@mark.weight(4)
def test_empty():
    """max - List is empty. (Edge case.)"""
    with pytest.raises(ValueError):
        max([])
