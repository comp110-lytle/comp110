"""Tests for CQ - functions Practice."""

__author__ = "Alyssa Lytle <abyrnes1@cs.unc.edu>"


import pytest
import re
from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module
from graders.helpers import set_stdin, assert_return_type
from re import Pattern
from typing import Any
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture

MODULE = "CQs.cq00_functions"
module: Any

def _regex_test_stdout(lines: list[str], monkeypatch: MonkeyPatch, regex: Pattern[Any]):
    match = False
    for line in lines:
        if regex.search(line) is not None:
            match = True
    assert match
  

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
def test_mimic_params():
    """mimic should take a str as input."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.mimic, [str])


@mark.weight(1)
def test_mimic_type():
    """mimic should return a string."""
    module = reimport_module(MODULE)
    assert_return_type(module.mimic, str)
    
@mark.weight(1)
def test_main_params():
    """main should take no inputs."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.main, [])


@mark.weight(1)
def test_main_type(capsys, monkeypatch):
    """main should not return anything"""
    module = reimport_module(MODULE)
    words: list[str] = ["secret"]
    set_stdin(monkeypatch, words)
    assert module.main() == None
    out: str
    out, _ = capsys.readouterr()
    

@mark.weight(1)
def test_mimic():
    """Testing that mimic returns the same string that is given as input."""
    module = reimport_module(MODULE)
    assert module.mimic("Comp110") == "Comp110"

@mark.weight(1)
def test_part_4_main_correctly_implemented_parameter(capsys, monkeypatch):
    """main() function properly prompts for user input and prints it back."""
    module = reimport_module(MODULE)

    words: list[str] = ["secret"]
    set_stdin(monkeypatch, words)
    module.main()
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)secret")
    _regex_test_stdout(lines, monkeypatch, regex)


    
    
