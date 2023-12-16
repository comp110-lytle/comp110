"""Linked list last tests."""
from graders.exercises.ex08_linked_lists.helpers import listify
from pytest import CaptureFixture, MonkeyPatch, mark
import pytest
from graders.helpers import author_is_a_valid_pid, import_module
pytestmark = pytest.mark.timeout(3)


@mark.weight(1)
def test_author():
    """__author__ str variable is correct PID format."""
    module = import_module("exercises.ex08.linked_list")
    assert author_is_a_valid_pid(module)


@mark.weight(4)
def test_last_empty():
    """last - empty"""
    from exercises.ex08.linked_list import last
    with pytest.raises(ValueError):
        assert last(None)


@mark.weight(5)
def test_last_single_element():
    """last - single element"""
    from exercises.ex08.linked_list import last
    assert last(listify([0])) == 0
    assert last(listify([1])) == 1


@mark.weight(5)
def test_last_many_elements():
    """last - many elements"""
    from exercises.ex08.linked_list import last
    assert last(listify([0, 1])) == 1
    assert last(listify([0, 1, 2])) == 2
    assert last(listify([0, 1, 2, 3])) == 3