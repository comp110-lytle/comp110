"""Tests for scale."""

from __future__ import annotations
from graders.exercises.ex10_linked_lists.helpers import Node 
from pytest import mark
import pytest
pytestmark = pytest.mark.timeout(3)

__author__ = "Kaki Ryan <kakiryan@cs.unc.edu>"


@mark.weight(5)
def test_scale_empty():
    """scale - empty list returns None."""
    from exercises.ex10.linked_list import scale
    assert scale(None, 2) is None


@mark.weight(5)
def test_scale_single_item():
    """scale - single Node input linked list."""
    from exercises.ex10.linked_list import scale
    assert Node(4, None) == scale(Node(2, None), 2)
    assert Node(6, None) == scale(Node(2, None), 3)
    assert Node(0, None) == scale(Node(0, None), 0)


@mark.weight(5)
def test_scale_multiple_items():
    """scale - multiple Node input linked list."""
    from exercises.ex10.linked_list import scale
    assert Node(2, Node(4, None)) == scale(Node(1, Node(2, None)), 2)
    assert Node(3, Node(6, Node(9, None))) == scale(Node(1, Node(2, Node(3, None))), 3)


@mark.weight(5)
def test_scale_pure():
    """scale - pure function does not modify input linked list."""
    from exercises.ex10.linked_list import scale
    original = Node(1, Node(2, None))
    assert Node(2, Node(4, None)) == scale(original, 2)
    assert Node(1, Node(2, None)) == original
