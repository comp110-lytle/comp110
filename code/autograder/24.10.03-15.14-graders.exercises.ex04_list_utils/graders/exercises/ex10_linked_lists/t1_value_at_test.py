"""Linked list value_at tests."""
from graders.exercises.ex10_linked_lists.helpers import listify
from pytest import mark
import pytest
pytestmark = pytest.mark.timeout(3)


@mark.weight(2)
def test_value_at_empty():
    """value_at - empty"""
    from exercises.ex10.linked_list import value_at
    with pytest.raises(IndexError):
        value_at(None, 0)


@mark.weight(3)
def test_value_at_single_element():
    """value_at - single element"""
    from exercises.ex10.linked_list import value_at
    assert value_at(listify([0]), 0) == 0
    assert value_at(listify([1]), 0) == 1


@mark.weight(5)
def test_value_at_many_elements():
    """value_at - many elements"""
    from exercises.ex10.linked_list import value_at
    assert value_at(listify([10, 20, 30, 40]), 1) == 20
    assert value_at(listify([10, 20, 30, 40]), 2) == 30
    assert value_at(listify([10, 20, 30, 40]), 3) == 40


@mark.weight(5)
def test_value_at_index_oob():
    """value_at - index greater than last index is None"""
    from exercises.ex10.linked_list import value_at
    with pytest.raises(IndexError):
        value_at(listify([10, 20, 30, 40]), 4)