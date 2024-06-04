"""Linked list max tests."""
from graders.exercises.ex10_linked_lists.helpers import listify
from pytest import mark
import pytest
pytestmark = pytest.mark.timeout(3)


@mark.weight(5)
def test_max_empty():
    """max - empty"""
    from exercises.ex10.linked_list import max
    with pytest.raises(ValueError):
        max(None)


@mark.weight(5)
def test_max_single_element():
    """max - single element"""
    from exercises.ex10.linked_list import max
    assert max(listify([0])) == 0
    assert max(listify([1])) == 1
    assert max(listify([2])) == 2


@mark.weight(5)
def test_max_many_elements():
    """max - many elements"""
    from exercises.ex10.linked_list import max
    assert max(listify([10, 20, 30, 40])) == 40
    assert max(listify([10, 20, 40, 30])) == 40
    assert max(listify([10, 40, 20, 30])) == 40
    assert max(listify([40, 10, 20, 30])) == 40