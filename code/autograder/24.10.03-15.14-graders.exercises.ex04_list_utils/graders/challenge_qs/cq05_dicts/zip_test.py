"""Tests for CQ05 - dicts Practice."""

__author__ = "Alyssa Lytle <abyrnes1@cs.unc.edu>"


import pytest
from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module
from graders.helpers import assert_return_type

MODULE = "lessons.zip"


@mark.weight(0)
def test_author():
    """invert - __author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module)


@mark.weight(1)
def test_zip_params():
    """Part 1. zip should take a list of strings and a list of ints as parameters"""
    module = reimport_module(MODULE)
    assert_parameter_list(module.zip, [list[str], list[int]])


@mark.weight(1)
def test_sum_return_type():
    """Part 1. zip should return a dict[str,int]"""
    module = reimport_module(MODULE)
    assert_return_type(module.zip, dict[str,int])


@mark.weight(1)
def test_zip_empty():
    """Part 1. zip of empty lists should be {}"""
    from lessons.zip import zip
    assert zip([],[]) == {}


@mark.weight(1)
def test_sum_positive():
    """Part 1. zip two lists of length 3"""
    from lessons.zip import zip
    l1: list[str] = ["Happy", "Tuesday","y'all"]
    l2: list[int] = [1,2,3]
    assert zip(l1,l2) == {"Happy": 1, "Tuesday":2, "y'all": 3}

@mark.weight(1)
def test_sum_negative():
    """Part 1. zip of two lists of different lengths should return {}"""
    from lessons.zip import zip
    l1: list[str] = ["Happy", "Tuesday","y'all"]
    l2: list[int] = [1,2,3,4]
    assert zip(l1,l2) == {}
    
