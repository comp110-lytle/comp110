"""Tests for Execise 03 - Wordle."""

__author__ = "Kris Jordan <kris@cs.unc.edu>"


import re
from re import Pattern
import unittest.mock as mock
from pytest import mark, raises
from typing import Any
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture
from graders.helpers import author_is_a_valid_pid, mute_output, set_stdin, import_module, reimport_module, assert_parameter_list, assert_return_type


MODULE = "exercises.ex03_wordle"
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


@mark.weight(3)
def test_part_1_contains_char_correctly_declared():
    """Part 1. `contains_char` - function is correctly declared (name, parameter types, return type)."""
    module = reimport_module(MODULE)
    assert callable(module.contains_char)
    assert_parameter_list(module.contains_char, [str, str])
    assert_return_type(module.contains_char, bool)


@mark.weight(5)
def test_part_1_contains_char_correctly_implemented():
    """Part 1. `contains_char` - function is correctly implemented."""
    module = reimport_module(MODULE)
    contains_char = module.contains_char
    assert contains_char("abc", "a")
    assert contains_char("abc", "b")
    assert contains_char("abc", "c")
    assert not contains_char("abc", "d")
    assert not contains_char("abcdefghijklmnopqrstuvwxy", "z")
    

@mark.weight(2)
def test_part_1_contains_char_throws():
    """Part 1. `contains_char` - throws assertion error with wrong second argument length."""
    module = reimport_module(MODULE)
    contains_char = module.contains_char
    with raises(AssertionError):
        contains_char("abc", "abc")


@mark.weight(3)
def test_part_2_emojified_correctly_declared():
    """Part 2. `emojified` - function is correctly declared (name, parameter types, return type)."""
    module = reimport_module(MODULE)
    assert callable(module.emojified)
    assert_parameter_list(module.emojified, [str, str])
    assert_return_type(module.emojified, str)


@mark.weight(7)
def test_part_2_emojified_correctly_implemented():
    """Part 2. `emojified` - function is correctly implemented."""
    module = reimport_module(MODULE)
    emojified = module.emojified
    assert emojified("aaaaa", "abcde") == "🟩🟨🟨🟨🟨"
    assert emojified("bbbbb", "abcde") == "🟨🟩🟨🟨🟨"
    assert emojified("ccccc", "abcde") == "🟨🟨🟩🟨🟨"
    assert emojified("ddddd", "abcde") == "🟨🟨🟨🟩🟨"
    assert emojified("eeeee", "abcde") == "🟨🟨🟨🟨🟩"
    assert emojified("abcde", "abcde") == "🟩🟩🟩🟩🟩"
    assert emojified("abcde", "zzzzz") == "⬜⬜⬜⬜⬜"
    assert emojified("abcde", "azbce") == "🟩🟨🟨⬜🟩"
    assert emojified("abcdefg", "azbcefg") == "🟩🟨🟨⬜🟩🟩🟩"


@mark.weight(5)
def test_part_2_emojified_calls_contains_char():
    """Part 2. `emojified` - function must call contains_char."""
    module = reimport_module(MODULE)
    try:
        with mock.patch.object(module, "contains_char", wraps=module.contains_char) as student_contains_char:
            module.emojified("hello", "world")
            student_contains_char.assert_called()
    except AssertionError as e:
        e.args = ("Must call `contains_char` from `emojified`.",)
        raise e


@mark.weight(5)
def test_part_2_emojified_throws():
    """Part 2. `emojified` - throws assertion error with non-equal lengths of parameters."""
    module = reimport_module(MODULE)
    contains_char = module.contains_char
    with raises(AssertionError):
        contains_char("abcd", "abc")
        contains_char("abc", "abcd")


@mark.weight(3)
def test_part_3_input_guess_correctly_declared(capsys, monkeypatch):
    """Part 3. `input_guess` - function is correctly declared (name, parameter types, return type)."""
    module = reimport_module(MODULE)
    assert callable(module.input_guess)
    assert_parameter_list(module.input_guess, [int])
    assert_return_type(module.input_guess, str)


@mark.weight(4)
def test_part_3_input_guess_correct_implementation_correct_length(capsys, monkeypatch):
    """Part 3. `input_guess` - function is correctly implemented (correct lengths)"""
    module = reimport_module(MODULE)

    words: list[str] = ["python"]
    set_stdin(monkeypatch, words)
    module.input_guess(6)
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Enter a 6 character word")
    _regex_test_stdout(lines, monkeypatch, regex)

    words: list[str] = ["pythons"]
    set_stdin(monkeypatch, words)
    module.input_guess(7)
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Enter a 7 character word")
    _regex_test_stdout(lines, monkeypatch, regex)


@mark.weight(3)
def test_part_3_input_guess_correct_implementation_incorrect_length(capsys, monkeypatch):
    """Part 3. `input_guess` - function is correctly implemented (incorrect lengths)"""
    module = reimport_module(MODULE)
    words: list[str] = ["pythons", "python"]
    set_stdin(monkeypatch, words)
    module.input_guess(6)
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Enter a 6 character word")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)That wasn't 6 chars")
    _regex_test_stdout(lines, monkeypatch, regex)


@mark.weight(3)
def test_part_4_main_correctly_declared():
    """Part 4. `main` - function is correctly declared (name, parameter types, return type)."""
    module = reimport_module(MODULE)
    assert callable(module.main)
    assert_parameter_list(module.main, [])
    assert_return_type(module.main, None)


@mark.weight(7)
def test_part_4_main_correctly_implemented(capsys, monkeypatch):
    """Part 4. `main` - game is winnable with secret "codes"."""
    module = reimport_module(MODULE)
    words: list[str] = ["codes"]
    set_stdin(monkeypatch, words)
    module.main()
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Turn 1/6")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)You won in 1/6")
    _regex_test_stdout(lines, monkeypatch, regex)


@mark.weight(5)
def test_part_4_main_correctly_implemented_multiple_guesses(capsys, monkeypatch):
    """Part 4. `main` - game is winnable after multiple guesses."""
    module = reimport_module(MODULE)
    words: list[str] = ["modes", "dodes", "codes"]
    set_stdin(monkeypatch, words)
    module.main()
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    for i in range(1, 4):
        regex = re.compile(f"(?i)Turn {i}/6")
        _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)You won in 3/6")
    _regex_test_stdout(lines, monkeypatch, regex)


@mark.weight(5)
def test_part_4_main_correctly_implemented_loses(capsys, monkeypatch):
    """Part 4. `main` - game is lost after 6 guesses."""
    module = reimport_module(MODULE)
    words: list[str] = ["modes", "dodes", "lodes", "godes", "wodes", "bodes"]
    set_stdin(monkeypatch, words)
    module.main()
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    for i in range(1, 7):
        regex = re.compile(f"(?i)Turn {i}/6")
        _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)X/6")
    _regex_test_stdout(lines, monkeypatch, regex)


@mark.weight(5)
def test_part_4_main_correctly_calls_functions_with_input_guess(capsys, monkeypatch):
    """Part 4. `main` - makes use of the `input_guess` function."""
    module = reimport_module(MODULE)
    try:
        with mock.patch.object(module, "input_guess", wraps=module.input_guess) as student_input_guess:
            words: list[str] = ["modes", "dodes", "lodes", "godes", "wodes", "bodes"]
            set_stdin(monkeypatch, words)
            module.main()
            student_input_guess.assert_called()
    except AssertionError as e:
        e.args = ("Must call `input_guess` from `main`.",)
        raise e

    
@mark.weight(6)
def test_part_4_main_correctly_calls_functions(capsys, monkeypatch):
    """Part 4. `main` - makes use of the `emojified` function."""
    module = reimport_module(MODULE)
    try:
        with mock.patch.object(module, "emojified", wraps=module.emojified) as student_emojified:
            words: list[str] = ["modes", "dodes", "lodes", "godes", "wodes", "bodes"]
            set_stdin(monkeypatch, words)
            module.main()
            student_emojified.assert_called()
    except AssertionError as e:
        e.args = ("Must call `emojified` from `main`.",)
        raise e