"""Tests for Exercise 05 - Unit Tests."""

__author__ = "Kaki Ryan <kakiryan@cs.unc.edu>"

from graders.helpers import reimport_module, author_is_a_valid_pid
import inspect
from unittest import mock
from pytest import mark, fixture
import pytest
pytestmark = pytest.mark.timeout(3)

MODULE = "lessons.zip_test"


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
    module = reimport_module(MODULE)
    functions = inspect.getmembers(module, inspect.isfunction)
    for function in functions:
        # check if test is in the fn name to exclude imports
        if function[0].startswith("test"):
            tests.append(function)
    return tests


def get_call_count(tests, fn) -> int:
    call_count = 0
    import lessons.zip_test as unit_tests
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


@mark.weight(5)
def test_zip_unit_tests(tests):
    """At least 3 unit tests for invert."""
    call_count: int = get_call_count(tests, "zip")
    assert call_count >= 3, f"Need at least 3 tests for zip, detected {call_count}"


