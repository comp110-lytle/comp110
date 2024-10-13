"""Tests for Exercise 05 - Unit Tests."""

__author__ = "730120710"

from graders.helpers import author_is_a_valid_pid, reimport_module
import inspect
from unittest import mock
from pytest import mark, fixture
import pytest

pytestmark = pytest.mark.timeout(6)

MODULE = "exercises.ex05.utils_test"

tests = []

# NOTE:
# FOR THIS TO WORK W THE TYPE CHECKER, have to add this line to typecheck.py:
# lines = [line for line in lines if "Source file found" not in line]
# Just want to ignore an error dealing with duplicate module names


@mark.weight(0)
def test_author():
    """list_utils_test.py - __author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module)


@fixture
def tests():
    """Get test fns from the test file."""
    tests = []
    module = reimport_module(MODULE)
    functions = inspect.getmembers(module, inspect.isfunction)
    for function in functions:
        # check if test is in the fn name to exclude imports
        if function[0].startswith("test"):
            tests.append(function)
    return tests


def get_call_count(tests, fn) -> int:
    call_count = 0
    import exercises.ex05.utils_test as unit_tests

    for test in tests:
        try:
            with mock.patch.object(
                unit_tests, fn, wraps=getattr(unit_tests, fn)
            ) as student_fn:
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
            raise Exception("No tests for " + fn + " defined yet, or one of your tests is incorrect.")
    return call_count


@mark.weight(5)
def test_only_evens_unit_tests(tests):
    """At least 3 unit tests for only_evens."""
    call_count: int = get_call_count(tests, "only_evens")
    assert (
        call_count >= 3
    ), f"Need at least 3 tests for only_evens, detected {call_count}"


@mark.weight(5)
def test_sub_unit_tests(tests):
    """At least 3 unit tests for sub."""
    call_count: int = get_call_count(tests, "sub")
    assert call_count >= 3, f"Need at least 3 tests for sub, detected {call_count}"


@mark.weight(5)
def test_add_at_index_unit_tests(tests):
    """At least 3 unit tests for add_at_index."""
    call_count: int = get_call_count(tests, "add_at_index")
    assert (
        call_count >= 3
    ), f"Need at least 3 tests for add_at_index, detected {call_count}"
