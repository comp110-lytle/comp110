"""Tests for CQ05 - dicts Practice."""

__author__ = "Alyssa Lytle <abyrnes1@cs.unc.edu>"



from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module
from graders.helpers import assert_return_type

MODULE = "lessons.recursion"

def try_reimport(mod_name):
    try:
        module = reimport_module(mod_name)
    except:
        assert False, f"Unable to import {mod_name}. This could be due to incorrect import syntax."
    return True

@mark.weight(0)
def test_author():
    """__author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module)


@mark.weight(1)
def test_zip_params():
    """f should take two integers as parameters"""
    assert try_reimport(MODULE)
    module = reimport_module(MODULE)
    assert_parameter_list(module.f, [int, int])


@mark.weight(1)
def test_sum_return_type():
    """f should return an int"""
    assert try_reimport(MODULE)
    module = reimport_module(MODULE)
    assert_return_type(module.f, int)


@mark.weight(1)
def test_f_zero():
    """Base case: f(0, k) should be zero."""
    assert try_reimport(MODULE)
    module = reimport_module(MODULE)
    assert module.f(0, 8) == 0


@mark.weight(1)
def test_f_recursive():
    """Recursive Step: f(n, k) should be computed correctly for any n >= 0 and any k."""
    assert try_reimport(MODULE)
    module = reimport_module(MODULE)
    assert module.f(3, 8) == 24
