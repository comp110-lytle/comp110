"""Tests for CQ - functions Practice."""

__author__ = "Alyssa Lytle <abyrnes1@cs.unc.edu>"


import pytest
from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module
from graders.helpers import assert_return_type
import re

MODULE = "lessons.evens_function"


def _regex_test_stdout(capsys, regex):
    out, _err = capsys.readouterr()
    lines = out.split("\n")
    match = False
    print(lines)
    for line in lines:
        if line.trim() == "":
            continue
        if regex.search(line) is not None:
            match = True
    assert match, "Output must match exactly. Check your spelling and spacing."     


def _get_output(capsys):
    out, _err = capsys.readouterr()
    lines = out.split("\n")
    lines = list(filter(lambda s: s != "", lines))
    return lines


@mark.weight(0)
def test_author():
    """__author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module)


@mark.weight(1)
def test_evens_params():
    """display_evens should take an integer as input."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.display_evens, [int])


@mark.weight(1)
def test_evens_return_type():
    """display_evens should return an integer."""
    module = reimport_module(MODULE)
    assert_return_type(module.display_evens, int)


@mark.weight(1)
def test_evens_ret_1():
    """Testing return value of display_evens with odd input."""
    module = reimport_module(MODULE)
    assert module.display_evens(1) == 1


@mark.weight(1)
def test_evens_print_1(capsys):
    """Testing printed output of display_evens with odd input."""
    module = reimport_module(MODULE)
    module.display_evens(1)
    output = _get_output(capsys)
    regex = re.compile(f"(?i){0}")
    match = regex.search(output[0]) is not None
    assert match, "Output must match expectation exactly. Check your spelling and spacing."


@mark.weight(1)
def test_evens_ret_8():
    """Testing return value of display_evens with odd input."""
    module = reimport_module(MODULE)
    assert module.display_evens(8) == 8


@mark.weight(1)
def test_evens_print_8(capsys):
    """Testing printed output of display_evens with odd input."""
    module = reimport_module(MODULE)
    module.display_evens(8)
    output = _get_output(capsys)
    regex = re.compile(f"(?i){8}")
    match = regex.search(output[0]) is not None
    assert match, "Output must match expectation exactly. Check your spelling and spacing."
    regex = re.compile(f"(?i){0}")
    match = regex.search(output[-1]) is not None
    assert match, "Output must match expectation exactly. Check your spelling and spacing."

