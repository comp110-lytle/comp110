"""Unit tests for all."""

__author__ = "730225231"

from pytest import mark


def _test_all(list: list[int], num: int, expected: int) -> None:
    """Helper function for necessary checks"""
    from exercises.ex04_utils import all
    assert all(list, num) == expected


@mark.timeout(3)
@mark.weight(5)
def test_use_case_true():
    """all - Should return True when all numbers in the list are the same as the number in the argument."""
    _test_all([1, 1, 1, 1, 1, 1], 1, True)


@mark.timeout(3)
@mark.weight(5)
def test_use_case_false():
    """all - Should return False when all numbers in the list are NOT the same as the argument. (Use case 1.)"""
    _test_all([1, 1, 1], 2, False)


@mark.timeout(3)
@mark.weight(5)
def test_use_case_false1():
    """all - Should return False when all numbers in the list are NOT the same as the argument. (Use case 2.)"""
    _test_all([1, 2, 2], 2, False)


@mark.timeout(3)
@mark.weight(5)
def test_empty():
    """all - Should return False when list is empty. (Edge Case.)"""
    _test_all([], 1, False)


