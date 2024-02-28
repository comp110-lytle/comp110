"""Tests for CQ - Unzip Dicts Practice."""


__author__ = "Alyssa Lytle <abyrnes1@cs.unc.edu>"


import pytest
from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module, import_module
from graders.helpers import assert_return_type

MODULE = "lessons.unzip"


@mark.weight(1)
def test_author():
    """Part 0. __author__ str variable is correct PID format."""
    module = import_module(MODULE)
    assert author_is_a_valid_pid(module)


@mark.weight(1)
def test_gk_params():
    """Part 1. get_keys should take a dict[str, int] as a parameter"""
    module = import_module(MODULE) 
    assert_parameter_list(module.get_keys, [dict[str, int]])


@mark.weight(1)
def test_gk_return_type():
    """Part 1. get_keys should return a list[str]"""
    module = reimport_module(MODULE)
    assert_return_type(module.get_keys, list[str])


@mark.weight(1)
def test_gk_empty():
    """Part 1. get_keys called with an empty dict should return an empty list."""
    module = reimport_module(MODULE)
    a: dict[str,int] = {}
    check = module.get_keys(a)
    assert check == []


@mark.weight(1)
def test_gk_nonempty():
    """Part 1. get_keys basic functionality."""
    module = reimport_module(MODULE)
    a: dict[str,int] = {"Math": 110, "Comp": 210, "Chem": 100}
    check = module.get_keys(a)
    assert check == ["Math", "Comp", "Chem"]


@mark.weight(1)
def test_gv_params():
    """Part 2. get_values should take a dict[str, int] as a parameter"""
    module = import_module(MODULE) 
    assert_parameter_list(module.get_values, [dict[str, int]])


@mark.weight(1)
def test_gv_return_type():
    """Part 2. get_values should return a list[int]"""
    module = reimport_module(MODULE)
    assert_return_type(module.get_values, list[int])


@mark.weight(1)
def test_gv_empty():
    """Part 2. get_values called with an empty dict should return an empty list."""
    module = reimport_module(MODULE)
    a: dict[str,int] = {}
    check = module.get_values(a)
    assert check == []


@mark.weight(1)
def test_gv_nonempty():
    """Part 2. get_values basic functionality."""
    module = reimport_module(MODULE)
    a: dict[str,int] = {"Math": 110, "Comp": 210, "Chem": 100}
    check = module.get_values(a)
    assert check == [110, 210, 100]

