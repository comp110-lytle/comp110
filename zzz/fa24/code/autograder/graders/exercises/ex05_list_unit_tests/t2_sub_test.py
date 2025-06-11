"""Unit tests for sub."""

__author__ = "730120710"


from pytest import mark


def _test_sub(list: list[int], start: int, end: int, expected: list[int]) -> None:
    """sub - Helper function for necessary checks"""
    from exercises.ex05.utils import sub

    original: list[int] = list[:]
    result: list[int] = sub(list, start, end)
    assert result == expected, "Returned list should match expected return value."
    assert list is not result, "sub must return a new list."
    assert original == list, "sub must not mutate its list parameter."


@mark.timeout(3)
@mark.weight(5)
def test_use_case():
    """sub - Start and end indices both fall within range of list, returns true subset."""
    _test_sub([1, 2, 3, 4], 1, 3, [2, 3])


@mark.timeout(3)
@mark.weight(4)
def test_zero_start():
    """sub - Start index is 0."""
    _test_sub([1, 2, 3], 0, 2, [1, 2])


@mark.timeout(3)
@mark.weight(4)
def test_neg_start():
    """sub - Start index is negative (edge case)."""
    _test_sub([1, 2, 3], -10, 2, [1, 2])


@mark.timeout(3)
@mark.weight(4)
def test_long_end():
    """sub - End index is greater than the length of the list (edge case)."""
    _test_sub([1, 2, 3], 1, 5, [2, 3])


@mark.timeout(3)
@mark.weight(4)
def test_empty_list():
    """sub - List is empty (edge case)."""
    _test_sub([], 0, 1, [])


@mark.timeout(3)
@mark.weight(4)
def test_expect_empty():
    """sub - start index is equal to length of list; expect an empty list (edge case)."""
    _test_sub([1], 1, 2, [])
