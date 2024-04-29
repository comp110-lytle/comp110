"""Tests for linkify."""

from __future__ import annotations
from graders.exercises.ex10_linked_lists.helpers import Node 
from pytest import mark
import pytest
pytestmark = pytest.mark.timeout(3)

__author__ = "Kaki Ryan <kakiryan@cs.unc.edu>"


@mark.weight(5)
def test_linkify_empty():
    """linkify - empty list returns None."""
    from exercises.ex10.linked_list import linkify 
    assert linkify([]) is None


@mark.weight(5)
def test_linkify_single_item():
    """linkify - single item input List."""
    from exercises.ex10.linked_list import linkify
    assert Node(1, None) == linkify([1])


@mark.weight(10)
def test_linkify_multiple_items():
    """linkify - multiple item input List."""
    from exercises.ex10.linked_list import linkify
    assert Node(1, Node(2, Node(3, None))) == linkify([1, 2, 3])
    assert Node(2, Node(3, Node(4, None))) == linkify([2, 3, 4])
