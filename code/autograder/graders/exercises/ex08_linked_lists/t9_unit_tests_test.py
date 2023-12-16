"""Tests for existence of unit tests."""

from __future__ import annotations
from unittest import mock
import inspect
from graders.helpers import reimport_module
from pytest import mark, fixture
import pytest
pytestmark = pytest.mark.timeout(3)

__author__ = "Kaki Ryan <kakiryan@cs.unc.edu>"

MODULE = "exercises.ex08.linked_list_test"


tests = []


@fixture
def tests() -> None:
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
    import exercises.ex08.linked_list_test as unit_tests
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
        except Exception as e:
            raise Exception(f"Possibly no tests for {fn} defined yet? Otherwise, exception encountered when running tests: {e}")
    return call_count


@mark.weight(2)
def test_last_unit_tests(tests):
    """At least 2 unit tests for last."""
    call_count: int = get_call_count(tests, "last")
    assert call_count >= 2, "Need at least 2 tests for last"


@mark.weight(2)
def test_value_at_unit_tests(tests):
    """At least 2 unit tests for value_at."""
    call_count: int = get_call_count(tests, "value_at")
    assert call_count >= 2, "Need at least 2 tests for value_at"


@mark.weight(2)
def test_max_unit_tests(tests):
    """At least 2 unit tests for max."""
    call_count: int = get_call_count(tests, "max")
    assert call_count >= 2, "Need at least 2 tests for max"


@mark.weight(2)
def test_linkify_unit_tests(tests):
    """At least 2 unit tests for linkify."""
    call_count: int = get_call_count(tests, "linkify")
    assert call_count >= 2, "Need at least 2 tests for linkify"


@mark.weight(2)
def test_scale_unit_tests(tests):
    """At least 2 unit tests for scale."""
    call_count: int = get_call_count(tests, "scale")
    assert call_count >= 2, "Need at least 2 tests for scale"
