"""Tests for CQ04 - loops Practice."""

__author__ = "Alyssa Lytle <abyrnes1@cs.unc.edu>"


import pytest
from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module
from graders.helpers import assert_return_type

MODULE = "lessons.sum"


@mark.weight(0)
def test_author():
    """invert - __author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module)


@mark.weight(1)
def test_w_sum_params():
    """Part 1. w_sum should take a list of floats as a parameter"""
    module = reimport_module(MODULE)
    assert_parameter_list(module.w_sum, [list[float]])


@mark.weight(1)
def test_sum_return_type():
    """Part 1. w_sum should return a float"""
    module = reimport_module(MODULE)
    assert_return_type(module.w_sum, float)


@mark.weight(1)
def test_sum_empty():
    """Part 1. w_sum of empty list should be 0.0"""
    from lessons.sum import w_sum
    assert w_sum([]) == 0.0


@mark.weight(1)
def test_sum_positive():
    """Part 1. w_sum of positive floats should be correct"""
    from lessons.sum import w_sum
    test_list: list[float] = [2.0, 2.0, 3.0]
    assert w_sum(test_list) == 7.0

@mark.weight(1)
def test_sum_negative():
    """Part 1. w_sum of positive and negative floats should be correct"""
    from lessons.sum import w_sum
    test_list: list[float] = [1.0, -3.0, 4.0]
    assert w_sum(test_list) == 2.0
    
@mark.weight(1)
def test_f_sum_params():
    """Part 2. f_sum should take a list of floats as a parameter"""
    module = reimport_module(MODULE)
    assert_parameter_list(module.f_sum, [list[float]])


@mark.weight(1)
def test_fsum_return_type():
    """Part 2. f_sum should return a float"""
    module = reimport_module(MODULE)
    assert_return_type(module.f_sum, float)


@mark.weight(1)
def test_fsum_empty():
    """Part 2. f_sum of empty list should be 0.0"""
    from lessons.sum import f_sum
    assert f_sum([]) == 0.0
    
@mark.weight(1)
def test_fsum_positive():
    """Part 2. f_sum of positive floats should be correct"""
    from lessons.sum import f_sum
    test_list: list[float] = [2.0, 2.0, 3.0]
    assert f_sum(test_list) == 7.0

@mark.weight(1)
def test_fsum_negative():
    """Part 2. f_sum of positive and negative floats should be correct"""
    from lessons.sum import f_sum
    test_list: list[float] = [1.0, -3.0, 4.0]
    assert f_sum(test_list) == 2.0
    
@mark.weight(1)
def test_f_range_sum_params():
    """Part 3. f_range_sum should take a list of floats as a parameter"""
    module = reimport_module(MODULE)
    assert_parameter_list(module.f_range_sum, [list[float]])


@mark.weight(1)
def test_f_range_sum_return_type():
    """Part 3. f_range_sum should return a float"""
    module = reimport_module(MODULE)
    assert_return_type(module.f_range_sum, float)


@mark.weight(1)
def test_f_range_sum_empty():
    """Part 3. f_range_sum of empty list should be 0.0"""
    from lessons.sum import f_range_sum
    assert f_range_sum([]) == 0.0
    
@mark.weight(1)
def test_f_range_sum_positive():
    """Part 3. f_range_sum of positive floats should be correct"""
    from lessons.sum import f_range_sum
    test_list: list[float] = [2.0, 2.0, 3.0]
    assert f_range_sum(test_list) == 7.0

@mark.weight(1)
def test_f_range_sum_negative():
    """Part 3. f_range_sum of positive and negative floats should be correct"""
    from lessons.sum import f_range_sum
    test_list: list[float] = [1.0, -3.0, 4.0]
    assert f_range_sum(test_list) == 2.0