"""Tests for CQ - Mutating Lists Practice."""


__author__ = "Alyssa Lytle <abyrnes1@cs.unc.edu>"


import pytest
from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module, import_module
from graders.helpers import assert_return_type

MODULE = "lessons.mutate"


@mark.weight(1)
def test_author():
    """Part 0. __author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module)


@mark.weight(1)
def test_append_params():
    """Part 1. manual_append should take a list[int] and an int as parameters"""
    module = import_module(MODULE)
    assert_parameter_list(module.manual_append, [list[int], int])


@mark.weight(1)
def test_append_return_type():
    """Part 1. manual_append should not return anything"""
    module = reimport_module(MODULE)
    assert_return_type(module.manual_append, None)


@mark.weight(1)
def test_append_empty():
    """Part 1. manual_append should work when appending an int to an empty list"""
    module = reimport_module(MODULE)
    a: list[int] = []
    module.manual_append(a, 0)
    assert a == [0]


@mark.weight(1)
def test_append_nonempty():
    """Part 1. manual_append should work when appending an int to a non-empty list"""
    module = reimport_module(MODULE)
    a: list[int] = [1,2]
    module.manual_append(a, 4)
    assert a == [1,2,4]


@mark.weight(1)
def test_double_params():
    """Part 2. double should take a list[int] as a parameter"""
    module = reimport_module(MODULE)
    assert_parameter_list(module.double, [list[int]])


@mark.weight(1)
def test_double_return_type():
    """Part 2. double should not return anything"""
    module = reimport_module(MODULE)
    assert_return_type(module.double, None)


@mark.weight(2)
def test_double_nonempty():
    """Part 2. double should multiply every element in the input list by 2"""
    module = reimport_module(MODULE)
    a: list[int] = [2,1,3]
    module.double(a)
    assert a == [4,2,6]