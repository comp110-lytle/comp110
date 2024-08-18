"""Tests for Exercise 00 - Getting Started."""

__author__ = "Kris Jordan <kris@cs.unc.edu>"

import runpy
from pytest import CaptureFixture, mark, MonkeyPatch
from graders.helpers import (
    author_is_a_valid_pid,
    mute_output,
    set_stdin,
    reimport_module,
    assert_parameter_list,
    assert_return_type,
)


MODULE = "exercises.ex00_hello_world"


@mark.weight(10)
def test_greet_defined():
    """Part 4. `greet` - function is declared."""
    module = reimport_module(MODULE)
    assert callable(module.greet)


@mark.weight(10)
def test_greet_parameter():
    """Part 4. `greet` - function has correct parameter type."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.greet, [str])


@mark.weight(10)
def test_greet_return_type():
    """Part 4. `greet` - function has correct return type."""
    module = reimport_module(MODULE)
    assert_return_type(module.greet, str)


@mark.weight(10)
def test_greet_returns_message():
    """Part 4. `greet` - function implementation must return a string containing original string, but longer."""
    module = reimport_module(MODULE)
    from random import random

    for i in range(100):
        arg: str = f"Name Argument ({random()})"
        rv: str = module.greet(arg)
        assert (
            rv != arg
        ), "Returned value from greet must not equal the argument exactly"
        assert len(rv) > len(
            arg
        ), "Returned value from greet must be longer than the argument given"
        assert arg in rv, "Argument given to greet must be contained in return value"
        assert_return_type(module.greet, str)


# @mark.weight(10)
# def test_run_as_module(capsys: CaptureFixture, monkeypatch: MonkeyPatch):
#     """Part 5. Program Structure should Ask User for Input and Call greet"""
#     arg = "110 Campers"
#     set_stdin(monkeypatch, [arg])

#     module = reimport_module(MODULE)

#     runpy.run_module(MODULE, run_name="__main__")
#     output = _get_output(capsys)
#     expected_output = module.greet(arg)

#     match_found = False
#     for line in output:
#         match_found = match_found or (expected_output in line)

#     assert (
#         match_found
#     ), f"Run as a program, input '{arg}', was expecting to produce message '{expected_output}'. Got: '{output}'."


@mark.weight(15)
def test_doc_string(capsys: CaptureFixture[str]):
    """Part 6. Doc String for module must be set and non-empty."""
    module = reimport_module(MODULE)
    assert getattr(module, "__doc__") is not None, "Module-level Doc String is required"
    assert len(getattr(module, "__doc__")) > 0, "Module-level Doc String is required"


@mark.weight(15)
def test_author(capsys: CaptureFixture[str]):
    """Part 6. __author__ global variable is present and correct format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module), "Valid 9-digit PID is required"


def _get_output(capsys):
    out, _err = capsys.readouterr()
    lines = out.split("\n")
    lines = list(filter(lambda s: s != "", lines))
    return lines
