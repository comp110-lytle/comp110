"""Tests for Execise 02 - Wordle."""

__author__ = "Kris Jordan <kris@cs.unc.edu>, Alyssa Lytle <abyrnes1@cs.unc.edu>"


import re
from re import Pattern
import unittest.mock as mock
from pytest import mark, raises
from typing import Any
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture
from graders.helpers import author_is_a_valid_pid, mute_output, set_stdin, import_module, reimport_module, assert_parameter_list, assert_return_type
import pytest
import runpy



CONCAT_MODULE = "CQs.cq04.concatenation"
COORD_MODULE = "CQs.cq04.coordinates"
VIS_MODULE = "CQs.cq04.visualize"

module: Any  # Global variable will hold the module object which can be reloaded


def _regex_test_stdout(lines: list[str], monkeypatch: MonkeyPatch, regex: Pattern[Any]):
    match = False
    for line in lines:
        if regex.search(line) is not None:
            match = True
    assert match


@mark.weight(1)
def test_author(capsys: CaptureFixture, monkeypatch: MonkeyPatch):
    """Part 0 - __author__ str variable is correct PID format in all three files. Note that order should be: imports, docstring, __author__ variable."""
    set_stdin(monkeypatch, ["python"])
    mute_output(capsys)
    global module
    module = import_module(CONCAT_MODULE)
    mute_output(capsys)
    assert author_is_a_valid_pid(module)
    module = import_module(COORD_MODULE)
    mute_output(capsys)
    assert author_is_a_valid_pid(module)
    module = import_module(VIS_MODULE)
    mute_output(capsys)
    assert author_is_a_valid_pid(module)


def _get_output(capsys):
    out, _err = capsys.readouterr()
    lines = out.split("\n")
    lines = list(filter(lambda s: s != "", lines))
    return lines

@mark.weight(1)
def test_concat_correctly_declared():
    """Part 1.1 `concat` - function is correctly declared (name, parameter types, return type)."""
    module = reimport_module(CONCAT_MODULE)
    assert callable(module.concat)
    assert_parameter_list(module.concat, [str, str])
    assert_return_type(module.concat, str)

@mark.weight(1)
def test_concat_correct_functionality():
    """Part 1.1 - checking `concat` for correct behavior."""
    module = reimport_module(CONCAT_MODULE)
    assert module.concat("321","howdy") == "321howdy"

@mark.weight(1)
def test_concat_main_global_vars():
    """Part 1.2 `concat` - concatenation.py should have global variables word1 and word2 with values "happy" and "tuesday", respectively."""
    #module = import_module(CONCAT_MODULE)
    assert runpy.run_module(CONCAT_MODULE, run_name='__main__')["word1"] == "happy"
    assert runpy.run_module(CONCAT_MODULE, run_name='__main__')["word2"] == "tuesday"


@mark.weight(1)
def test_concat_main(capsys, monkeypatch):
    """Part 1.2 `concat` - concatenation.py should call concat."""
    #module = import_module(CONCAT_MODULE)
    
    runpy.run_module(CONCAT_MODULE, run_name='__main__')
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)happytuesday")
    _regex_test_stdout(lines, monkeypatch, regex)
    

@mark.weight(1)
def test_concat_correctly_imported():
    """Part 2.0 `visualize.py` - concat function is correctly imported."""
    module = reimport_module(VIS_MODULE)
    assert callable(module.concat)
    

@mark.weight(1)
def test_concat_suppression(capsys):
    """Part 2.1 `visualize.py` - concat function call suppressed."""
    #module = import_module(CONCAT_MODULE)
    runpy.run_module(CONCAT_MODULE)
    out: str
    out, _ = capsys.readouterr()
    assert len(out) == 0
  

@mark.weight(1)
def test_visualize_main_global_vars():
    """Part 2.2 `visualize.py` - visualize.py should have global variables x and y with values "123" and "abc", respectively."""
    #module = import_module(CONCAT_MODULE)
    assert runpy.run_module(VIS_MODULE, run_name='__main__')["x"] == "123"
    assert runpy.run_module(VIS_MODULE, run_name='__main__')["y"] == "abc"


    
@mark.weight(1)
def test_vis_function_call(capsys, monkeypatch):
    """Part 2.2 `visualize.py` - concat function called with global variables x and y."""
    #module = import_module(CONCAT_MODULE)
    runpy.run_module(VIS_MODULE, run_name='__main__')
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)123abc")
    _regex_test_stdout(lines, monkeypatch, regex)
    
@mark.weight(1)
def test_coords_output(capsys,monkeypatch):
    """Part 3.0 `coordinates.py` - Checking `get_coords` for correct functionality."""
    # words: list[str] = ["games"]
    # set_stdin(monkeypatch, words)
    module = reimport_module(COORD_MODULE)
    module.get_coords("21", "23")
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    test_out = ['(2,2)', '(2,3)', '(1,2)', '(1,3)']
    for output in test_out:
        regex = re.compile(f"(?i){output}")
        _regex_test_stdout(lines, monkeypatch, regex)
        
@mark.weight(1)
def test_get_coords_correctly_imported():
    """Part 3.1 `visualize.py` - get_coords function is correctly imported."""
    module = reimport_module(VIS_MODULE)
    assert callable(module.get_coords)
    
@mark.weight(1)
def test_coords_output_in_vis(capsys,monkeypatch):
    """Part 3.1 `visualize.py` - get_coords called for global variables x and y."""
    # words: list[str] = ["games"]
    # set_stdin(monkeypatch, words)
    runpy.run_module(VIS_MODULE, run_name='__main__')
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    test_out = ['(1,a)','(1,b)','(1,c)','(2,a)','(2,b)','(2,c)','(3,a)','(3,b)','(3,c)']
    for output in test_out:
        regex = re.compile(f"(?i){output}")
        _regex_test_stdout(lines, monkeypatch, regex)
    
