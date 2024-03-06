"""Tests for CQ on Unit Tests."""

__author__ = "Alyssa Lytle"

from graders.helpers import reimport_module, author_is_a_valid_pid, import_module
import inspect
from unittest import mock
from pytest import mark, fixture
import pytest
pytestmark = pytest.mark.timeout(3)

MODULE = "lessons.garden.garden_helpers_test"


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


def get_tests():
    """Get test fns from the test file."""
    tests = []
    try:
        module = import_module(MODULE)
        functions = inspect.getmembers(module, inspect.isfunction)
        for function in functions:
        # check if test is in the fn name to exclude imports
            if function[0].startswith("test"):
                tests.append(function)
    
    except:
        assert False, f"Unable to import {MODULE}. This could be due to incorrect import syntax."
        #raise Exception(f"Unable to import {MODULE}. This could be due to incorrect import syntax.")
    return tests


def get_call_count(tests, fn) -> int:
    call_count = 0
    try:
        unit_tests  = import_module(MODULE)
    except:
        raise Exception(f"Unable to import {MODULE}")
    
    if len(tests) == 0:
        raise Exception("Unable to find tests due to improper import")
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
def test_zip_unit_tests():
    """At least 2 unit tests for add_by_kind."""
    call_count: int = get_call_count(get_tests(), "add_by_kind")
    assert call_count >= 2, f"Need at least 3 tests for add_by_kind, detected {call_count}"


@mark.weight(5)
def test_zip_unit_tests2():
    """At least 2 unit tests for add_by_date."""
    call_count: int = get_call_count(get_tests(), "add_by_date")
    assert call_count >= 2, f"Need at least 2 tests for add_by_date, detected {call_count}"

@mark.weight(5)
def test_zip_unit_tests3():
    """At least 2 unit tests for lookup_by_kind_and_date."""
    call_count: int = get_call_count(get_tests(), "lookup_by_kind_and_date")
    assert call_count >= 2, f"Need at least 2 tests for lookup_by_kind_and_date, detected {call_count}"
