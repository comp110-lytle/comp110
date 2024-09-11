"""Tests for Execise 02 - Wordle."""

__author__ = "Kris Jordan <kris@cs.unc.edu>"


import re
from re import Pattern
import unittest.mock as mock
from pytest import mark, raises
from typing import Any
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture
from graders.helpers import author_is_a_valid_pid, mute_output, set_stdin, import_module, reimport_module, assert_parameter_list, assert_return_type
import pytest

MODULE = "exercises.ex02_chardle"
module: Any  # Global variable will hold the module object which can be reloaded


def _regex_test_stdout(lines: list[str], monkeypatch: MonkeyPatch, regex: Pattern[Any]):
    match = False
    for line in lines:
        if regex.search(line) is not None:
            match = True
    assert match


@mark.weight(1)
def test_author(capsys: CaptureFixture, monkeypatch: MonkeyPatch):
    """Part 0 - __author__ str variable is correct PID format."""
    set_stdin(monkeypatch, ["python"])
    mute_output(capsys)
    global module
    module = import_module(MODULE)
    mute_output(capsys)
    assert author_is_a_valid_pid(module)


def _get_output(capsys):
    out, _err = capsys.readouterr()
    lines = out.split("\n")
    lines = list(filter(lambda s: s != "", lines))
    return lines

@mark.weight(1)
def test_inp_word_correctly_declared():
    """Part 1. `input_word` - function is correctly declared (name, parameter types, return type)."""
    module = reimport_module(MODULE)
    assert callable(module.input_word)
    assert_parameter_list(module.input_word, [])
    assert_return_type(module.input_word, str)

@mark.weight(2)
def test_input_word(capsys,monkeypatch):
    """Part 1. `input_word` - Should prompt user with: Enter a 5-character word"""
    words: list[str] = ["games"]
    set_stdin(monkeypatch, words)
    module = reimport_module(MODULE)
    module.input_word()
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Enter a 5-character word")
    _regex_test_stdout(lines, monkeypatch, regex)
    
@mark.weight(1)
def test_input_word_correct(capsys,monkeypatch):
    """Part 1. `input_word` - If the input word has a length of 5, it should return that input word."""
    words: list[str] = ["games"]
    set_stdin(monkeypatch, words)
    module = reimport_module(MODULE)
    assert module.input_word() == "games"
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Enter a 5-character word")
    _regex_test_stdout(lines, monkeypatch, regex)
    


@mark.weight(1)
def test_inp_letter_correctly_declared():
    """Part 2. `input_letter` - function is correctly declared (name, parameter types, return type)."""
    module = reimport_module(MODULE)
    assert callable(module.input_letter)
    assert_parameter_list(module.input_letter, [])
    assert_return_type(module.input_letter, str)

@mark.weight(1)
def test_input_letter(capsys,monkeypatch):
    """Part 2. `input_letter` - Should prompt user with: Enter a single character"""
    words: list[str] = ["a"]
    set_stdin(monkeypatch, words)
    module = reimport_module(MODULE)
    module.input_letter()
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Enter a single character")
    _regex_test_stdout(lines, monkeypatch, regex)
    
@mark.weight(1)
def test_input_letter_correct(capsys,monkeypatch):
    """Part 2. `input_letter` - If the input letter has a length of 1, it should return that input letter."""
    words: list[str] = ["a"]
    set_stdin(monkeypatch, words)
    module = reimport_module(MODULE)
    assert module.input_letter() == "a"

    


@mark.weight(1)
def test_part_1_contains_char_correctly_declared():
    """Part 3. `contains_char` - function is correctly declared (name, parameter types, return type)."""
    module = reimport_module(MODULE)
    assert callable(module.contains_char)
    assert_parameter_list(module.contains_char, [str, str])
    assert_return_type(module.contains_char, None)


@mark.weight(2)
def test_part_1_contains_char_correctly_implemented(capsys,monkeypatch):
    """Part 3. `contains_char` - function correctly states if a character is found at a certain index. (Check output wording exactly!)"""
    module = reimport_module(MODULE)
    ## Test 1
    module.contains_char("abcde", "a")
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Searching for a in abcde")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)a found at index 0")
    _regex_test_stdout(lines, monkeypatch, regex)
    ## Test 2
    module.contains_char("abcde", "e")
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Searching for e in abcde")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)e found at index 4")
    _regex_test_stdout(lines, monkeypatch, regex)
    ## Test 3
    module.contains_char("abcde", "q")
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Searching for q in abcde")
    _regex_test_stdout(lines, monkeypatch, regex)

    
@mark.weight(2)
def test_contains_char_count(capsys,monkeypatch):
    """Part 4. `contains_char` - function correctly counts number of occurences of a character in a word. (Check output wording exactly!)"""
    module = reimport_module(MODULE)
    ## Test 1
    module.contains_char("abcde", "a")
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Searching for a in abcde")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)a found at index 0")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)1 instance of a found in abcde")
    _regex_test_stdout(lines, monkeypatch, regex)
    ## Test 2
    module.contains_char("abcda", "a")
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Searching for a in abcda")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)a found at index 0")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)a found at index 4")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)2 instances of a found in abcda")
    _regex_test_stdout(lines, monkeypatch, regex)
    # ## Test 3
    module.contains_char("abcde", "q")
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Searching for q in abcde")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)No instances of q found in abcde")
    _regex_test_stdout(lines, monkeypatch, regex)


    
@mark.weight(1)
def test_input_letter_incorrect(capsys,monkeypatch):
    """Part 5. `input_letter` - If the input word doesn't have a length of 1, it should exit the program early and print: Error: Character must be a single character."""
    inputs: list[str] = ["gamers"]
    did_not_exit = True
    with pytest.raises(SystemExit):
            set_stdin(monkeypatch, inputs)
            reimport_module(MODULE)
            module.input_letter()
            did_not_exit = False
    assert did_not_exit, "Must call exit() with invalid input."
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Enter a single character")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)Error: Character must be a single character")
    _regex_test_stdout(lines, monkeypatch, regex)


@mark.weight(1)
def test_input_word_incorrect(capsys,monkeypatch):
    """Part 5. `input_word` - If the input word doesn't have a length of 5, it should exit the program early and print: Error: Word must contain 5 characters."""
    inputs: list[str] = ["gamers"]
    did_not_exit = True
    with pytest.raises(SystemExit):
            set_stdin(monkeypatch, inputs)
            reimport_module(MODULE)
            module.input_word()
            did_not_exit = False
    assert did_not_exit, "Must call exit() with invalid input."
    # assert module.input_word() == "gamers"
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Enter a 5-character word")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)Error: Word must contain 5 characters.")
    _regex_test_stdout(lines, monkeypatch, regex)





@mark.weight(1)
def test_main_correctly_declared():
    """Part 6. `main` - function is correctly declared (name, parameter types, return type)."""
    module = reimport_module(MODULE)
    assert callable(module.main)
    assert_parameter_list(module.main, [])
    assert_return_type(module.main, None)


@mark.weight(1)
def test_main_word(capsys,monkeypatch):
    """Part 6. `main` - Should prompt user first with: Enter a 5-character word"""
    word = "games"
    char = "a"
    set_stdin(monkeypatch, [word, char])
    module = reimport_module(MODULE)
    module.main()
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Enter a 5-character word")
    _regex_test_stdout(lines, monkeypatch, regex)
    
@mark.weight(1)
def test_main_char(capsys,monkeypatch):
    """Part 6. `main` - Should prompt user second with: Enter a single character"""
    word = "games"
    char = "a"
    set_stdin(monkeypatch, [word, char])
    module = reimport_module(MODULE)
    module.main()
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Enter a 5-character word")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)Enter a single character")
    _regex_test_stdout(lines, monkeypatch, regex)
    
    
@mark.weight(1)
def test_main_char(capsys,monkeypatch):
    """Part 6. `main` - Should take results from function calls and use them as input to """
    word = "abcde"
    char = "q"
    set_stdin(monkeypatch, [word, char])
    module = reimport_module(MODULE)
    module.main()
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Enter a 5-character word")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)Enter a single character")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)Searching for q in abcde")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)No instances of q found in abcde")
    _regex_test_stdout(lines, monkeypatch, regex)