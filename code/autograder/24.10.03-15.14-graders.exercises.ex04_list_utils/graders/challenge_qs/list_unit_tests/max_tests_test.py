"""Tests for Exercise 05 - Unit Tests."""

__author__ = "Kaki Ryan <kakiryan@cs.unc.edu>"

from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module, assert_return_type
import inspect
from unittest import mock
from pytest import mark, fixture
import pytest
pytestmark = pytest.mark.timeout(3)

MODULE = "lessons.CQ05.find_max"
TESTMODULE = "lessons.CQ05.max_test"

@mark.weight(0)
def test_author():
    """__author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module)


tests = []

# NOTE:
# FOR THIS TO WORK W THE TYPE CHECKER, have to add this line to typecheck.py:
# lines = [line for line in lines if "Source file found" not in line]
# Just want to ignore an error dealing with duplicate module names


@fixture
def tests():
    """Get test fns from the test file."""
    tests = []
    module = reimport_module(TESTMODULE)
    functions = inspect.getmembers(module, inspect.isfunction)
    for function in functions:
        # check if test is in the fn name to exclude imports
        if function[0].startswith("test"):
            tests.append(function)
    return tests


def get_call_count(tests, fn) -> int:
    call_count = 0
    import lessons.CQ05.max_test as unit_tests
    for test in tests:
        try:
            with mock.patch.object(unit_tests, fn, wraps=getattr(unit_tests, fn)) as student_fn: 
                # add this first try/except to ignore if a student's test fails
                try:
                    test[1]()
                except AssertionError:
                    ...
                try:
                    student_fn.assert_called()
                    call_count += 1
                except Exception:
                    ...
        except Exception:
            raise Exception("No tests for " + fn + " defined yet.")
    return call_count



@mark.weight(1)
def test_max_param():
    """Part 1. find_and_remove_max should have list[int] parameter."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.find_and_remove_max, [list[int]])
    
@mark.weight(1)
def test_max_return_val():
    """Part 1. find_and_remove_max should return int."""
    module = reimport_module(MODULE)
    assert_return_type(module.find_and_remove_max, int)

@mark.weight(1)
def test_max_ret_edge():
    """Part 1. find_and_remove_max with empty input should not modify input and return -1."""
    module = reimport_module(MODULE)
    a: list[int] = []
    assert module.find_and_remove_max(a) == -1
    assert a == []
    
@mark.weight(1)
def test_max_ret():
    """Part 1. find_and_remove_max should return correct value given list of ints."""
    module = reimport_module(MODULE)
    a: list[int] = [1,8,2,3,8,3]
    assert module.find_and_remove_max(a) == 8
    
@mark.weight(1)
def test_max_mutate():
    """Part 1. find_and_remove_max should remove all instances of max value from list of ints."""
    module = reimport_module(MODULE)
    a: list[int] = [1,8,8,2,3,8,3]
    module.find_and_remove_max(a)
    assert a == [1,2,3,3]

@mark.weight(5)
def test_zip_unit_tests(tests):
    """At least 3 unit tests for find_and_remove_max."""
    call_count: int = get_call_count(tests, "find_and_remove_max")
    assert call_count >= 3, f"Need at least 3 tests for find_and_remove_max, detected {call_count}"


