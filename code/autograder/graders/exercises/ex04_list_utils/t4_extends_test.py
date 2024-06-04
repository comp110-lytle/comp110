"""Unit tests for extend."""

__author__ = "720310785"

from pytest import mark
from graders.helpers import import_module, reimport_module, assert_return_type
MODULE = "ex04_utils"

def _test_extend(list1: list[int], list2: list[int], expected: bool) -> None:
    """extend - Helper function for necessary checks"""
    module = import_module(MODULE)
    module.extend(list1, list2)
    assert list1 == expected


@mark.timeout(3)
@mark.weight(2)
def test_both_empty():
    """extend - Both lists are empty. (Edge case.)"""
    _test_extend([], [], [])


@mark.timeout(3)
@mark.weight(2)
def test_use_case1():
    """extend - Extend populated list with empty list. (Edge case.)"""
    _test_extend([1,2], [], [1,2])


@mark.timeout(3)
@mark.weight(2)
def test_use_case2():
    """extend - Extend empty list with populated list. (Edge case.)"""
    _test_extend([], [1, 2, 3], [1,2,3])


@mark.timeout(3)
@mark.weight(5)
def test_diff_elements():
    """extend - Extend populated list with populated list. (Use case 1.)"""
    _test_extend([1, 2, 3], [4, 5, 1], [1,2,3,4,5,1])


@mark.timeout(3)
@mark.weight(5)
def test_diff_elements2():
    """extend - Extend populated list with populated list. (Use case 2.)"""
    _test_extend([1, 2, 3, 4], [1, 1], [1,2,3,4,1,1])


@mark.weight(2)
def test_extend_return_type():
    """extend should not return anything"""
    module = reimport_module(MODULE)
    assert_return_type(module.extend, None)


@mark.weight(2)
def test_extend_mutation():
    """extend should not modify the second parameter"""
    module = reimport_module(MODULE)
    a: list[int] = [1,2,3]
    b: list[int] = [4,5]
    module.extend(a,b)
    assert b == [4,5]