"""Unit tests for add_at_index."""

__author__ = "730120170"

import pytest
from pytest import mark


def _test_add_at_index(
    list1: list[int], to_be_added: int, idx_to_add: int, expected: list[int]
) -> None:
    """add_at_index - Helper function for necessary checks."""
    from exercises.ex05.utils import add_at_index

    original: list[int] = list1[:]
    add_at_index(list1, to_be_added, idx_to_add)
    assert (
        list1 == expected
    ), "The list argument should be mutated by adding the specified integer at the indicated index."


@mark.timeout(3)
@mark.weight(2)
def test_out_of_range_neg1():
    """add_at_index - Trying to add an element at an index that is out of range (edge case)."""
    with pytest.raises(IndexError):
        _test_add_at_index([], 5, -1, None)


@mark.timeout(3)
@mark.weight(2)
def test_out_of_range_neg2():
    """add_at_index - Trying to add an element at an index that is out of range (edge case)."""
    with pytest.raises(IndexError):
        _test_add_at_index([5, 6], 8, -1, None)


@mark.timeout(3)
@mark.weight(1)
def test_out_of_range_neg3():
    """add_at_index - Trying to add an element at an index that is out of range (edge case)."""
    with pytest.raises(IndexError):
        _test_add_at_index([5, 6], 8, -18, None)


@mark.timeout(3)
@mark.weight(3)
def test_out_of_range_pos1():
    """add_at_index - Trying to add an element at an index that is out of range (edge case)."""
    with pytest.raises(IndexError):
        _test_add_at_index([], 1, 5, None)


@mark.timeout(3)
@mark.weight(2)
def test_out_of_range_pos2():
    """add_at_index - Trying to add an element at an index that is out of range (edge case)."""
    with pytest.raises(IndexError):
        _test_add_at_index([5, 6], 8, 3, None)


@mark.timeout(3)
@mark.weight(5)
def test_empty_list():
    """add_at_index - Adding an element at an index 0 to an empty list."""
    _test_add_at_index([], 1, 0, [1])


@mark.timeout(3)
@mark.weight(3)
def test_one_element_list1():
    """add_at_index - Adding an element to a list with one element."""
    _test_add_at_index([3], 5, 1, [3, 5])


@mark.timeout(3)
@mark.weight(2)
def test_one_element_list2():
    """add_at_index - Adding an element to a list with one element."""
    _test_add_at_index([-10], 5, 0, [5, -10])


@mark.timeout(3)
@mark.weight(2)
def test_use_case1():
    """add_at_index - Adding an element to a list with multiple elements (use case)."""
    _test_add_at_index([3, 5, 9], 7, 2, [3, 5, 7, 9])


@mark.timeout(3)
@mark.weight(1)
def test_use_case2():
    """add_at_index - Adding an element to a list with multiple elements (use case)."""
    _test_add_at_index([3, 5, 9], 11, 3, [3, 5, 9, 11])


@mark.timeout(3)
@mark.weight(1)
def test_use_case3():
    """add_at_index - Adding an element to a list with multiple elements (use case)."""
    _test_add_at_index([3, 5, 9], 1, 0, [1, 3, 5, 9])


@mark.timeout(3)
@mark.weight(1)
def test_use_case4():
    """add_at_index - Adding an element to a list with multiple elements (use case)."""
    _test_add_at_index([-9, -8, -7, -6], 0, 2, [-9, -8, 0, -7, -6])
