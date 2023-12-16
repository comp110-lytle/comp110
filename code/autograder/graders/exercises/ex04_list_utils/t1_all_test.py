"""Unit tests for all."""

__author__ = "730225231"

from pytest import mark


def _test_all(list: list[int], num: int, expected: int) -> None:
    """Helper function for necessary checks"""
    from exercises.ex04_utils import all
    assert all(list, num) == expected


@mark.timeout(3)
@mark.weight(4)
def test_use_case_true():
    """all - List is all 1's, testing with 1."""
    _test_all([1, 1, 1], 1, True)


@mark.timeout(3)
@mark.weight(4)
def test_use_case_false():
    """all - List is all 1's, testing with 2."""
    _test_all([1, 1, 1], 2, False)


@mark.timeout(3)
@mark.weight(4)
def test_use_case_false1():
    """all - List is 1's and 2's, testing with 2."""
    _test_all([1, 2, 2], 2, False)


@mark.timeout(3)
@mark.weight(4)
def test_use_case_false2():
    """all - List is 1's and 2's, testing with 1."""
    _test_all([1, 2, 2], 1, False)


@mark.timeout(3)
@mark.weight(4)
def test_empty():
    """all - List is empty."""
    _test_all([], 1, False)


@mark.timeout(3)
@mark.weight(5)
def test_long_list_true():
    """all - List is all 2's."""
    _test_all([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 2, True)


@mark.timeout(3)
@mark.weight(5)
def test_long_list_false():
    """all - List is all 2's."""
    _test_all([2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2], 2, False)