"""Unit tests for sub."""

__author__ = "730120710"


from pytest import mark


def _test_only_evens(list: list[int], expected: list[int]) -> None:
    """only_evens - Helper function for necessary checks."""
    from exercises.ex05.utils import only_evens

    original: list[int] = list[:]
    result: list[int] = only_evens(list)
    assert result == expected, "Returned list should match expected return value."
    assert list is not result, "only_evens must return a new list."
    assert original == list, "only_evens must not mutate its input list."


@mark.timeout(3)
@mark.weight(4)
def test_empty_list():
    """only_evens - empty input list (edge case)."""
    _test_only_evens([], [])


@mark.timeout(3)
@mark.weight(2)
def test_expect_empty():
    """only_evens - input list contains only odd numbers."""
    _test_only_evens([1], [])


@mark.timeout(3)
@mark.weight(2)
def test_expect_empty2():
    """only_evens - input list contains only odd numbers."""
    _test_only_evens([73, 5, 19], [])


@mark.timeout(3)
@mark.weight(2)
def test_use_case1():
    """only_evens - input list contains both even and odd numbers."""
    _test_only_evens([1, 2, 3, 4], [2, 4])


@mark.timeout(3)
@mark.weight(1)
def test_use_case2():
    """only_evens - input list contains both even and odd numbers."""
    _test_only_evens([4, 3, 2, 1], [4, 2])


@mark.timeout(3)
@mark.weight(1)
def test_use_case3():
    """only_evens - input list contains both even and odd numbers."""
    _test_only_evens([2, 4, 1, 3], [2, 4])


@mark.timeout(3)
@mark.weight(1)
def test_use_case4():
    """only_evens - input list contains both even and odd numbers."""
    _test_only_evens([1, 7, 4, 0], [4, 0])


@mark.timeout(3)
@mark.weight(1)
def test_zero_start1():
    """only_evens - one even number in input list."""
    _test_only_evens([1, 3, 6], [6])


@mark.timeout(3)
@mark.weight(1)
def test_zero_start2():
    """only_evens - one even number in input list."""
    _test_only_evens([8, 9, 5], [8])


@mark.timeout(3)
@mark.weight(1)
def test_zero_start3():
    """only_evens - one even number in input list."""
    _test_only_evens([1, 2, 3], [2])


@mark.timeout(3)
@mark.weight(4)
def test_neg_start():
    """only_evens - negative numbers in input list."""
    _test_only_evens([1, -10, -2], [-10, -2])


@mark.timeout(3)
@mark.weight(5)
def test_long():
    """only_evens - all even numbers in input list."""
    _test_only_evens([4, 2, 6, 12], [4, 2, 6, 12])
