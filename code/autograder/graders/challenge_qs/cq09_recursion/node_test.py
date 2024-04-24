import re
import importlib
from pytest import mark
from graders.helpers import author_is_a_valid_pid, mute_output, set_stdin, import_module, reimport_module
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture
from typing import Any
import inspect
import types
from exercises.ex10.linked_list import Node

MODULE = "exercises.ex10.linked_list"

@mark.weight(0)
def test_author(capsys: CaptureFixture, monkeypatch: MonkeyPatch):
    """0. __author__ str variable is correct PID format."""
    set_stdin(monkeypatch, ["hello", "z"])  # 
    mute_output(capsys)
    module = import_module(MODULE)
    mute_output(capsys)
    assert author_is_a_valid_pid(module)


def _equal(ll1: Node, ll2: Node):
    """Checks if two linked lists are equal"""
    if (ll1.next == None) and (ll2.next == None):
        return True
    elif (ll1.next == None) or (ll2.next == None):
        # different lengths
        return False
    else:
        return (ll1.data == ll2.data) and _equal(ll1.next, ll2.next)




@mark.weight(1)
def test_head_params():
    """Part 0: head() should have one parameter: self and return int"""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Node.head)
    assert len(sig.parameters) == 1
    assert sig.return_annotation == "int"  

@mark.weight(1)
def test_head_functionality():
    """Part 0: head() should return an int with the 'data' of the head"""
    node_c = Node(5, None)
    node_b = Node(4, node_c)
    node_a = Node(3, node_b)
    assert node_a.head() == 3
    assert node_b.head() == 4
    
@mark.weight(1)
def test_tail_params():
    """Part 1: tail() should have one parameter: self and return Node or None"""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Node.tail)
    assert len(sig.parameters) == 1
    assert sig.return_annotation == "Node | None"

@mark.weight(1)
def test_tail_functionality():
    """Part 1: tail() should return a linked list for a list of length > 1"""
    node_c = Node(5, None)
    node_b = Node(4, node_c)
    node_a = Node(3, node_b)
    assert _equal(node_a.tail(), node_b)

@mark.weight(1)
def test_tail_functionality():
    """Part 1: tail() should return None for a list of length 1"""
    node_c = Node(5, None)
    assert node_c.tail() == None
    
    
@mark.weight(1)
def test_last_params():
    """Part 2: last() should have one parameter: self and return int"""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Node.head)
    assert len(sig.parameters) == 1
    assert sig.return_annotation == "int"

    

@mark.weight(1)
def test_last_functionality():
    """Part 2: last() should return an int with the 'data' of the last node in the linked list"""
    node_c = Node(5, None)
    node_b = Node(4, node_c)
    node_a = Node(3, node_b)
    assert node_a.last() == 5
    assert node_b.last() == 5
    
    
