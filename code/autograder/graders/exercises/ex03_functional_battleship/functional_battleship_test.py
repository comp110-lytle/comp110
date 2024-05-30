"""Tests for Execise 03 - Structured Battleship."""

__author__ = "Vrinda Desai <vrinda@email.unc.edu>"


import re
from re import Pattern
import unittest.mock as mock
from pytest import mark, raises
from typing import Any
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture
from graders.helpers import author_is_a_valid_pid, mute_output, set_stdin, import_module, reimport_module, assert_parameter_list, assert_return_type


MODULE = "ex03_functional_battleship"
module: Any  # Global variable will hold the module object which can be reloaded


def _regex_test_stdout(lines: list[str], monkeypatch: MonkeyPatch, regex: Pattern[Any]):
    match = False
    for line in lines:
        if regex.search(line) is not None:
            match = True
    assert match


@mark.weight(5)
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


### PART 1
@mark.weight(5)
def test_part_1_input_guess_correctly_declared(capsys, monkeypatch):
    """Part 1. `input_guess` - function is correctly declared (name, parameter types, return type)."""
    module = reimport_module(MODULE)
    assert callable(module.input_guess)
    assert_parameter_list(module.input_guess, [int, str])
    assert_return_type(module.input_guess, int)


@mark.weight(5)
def test_part_1_input_guess_correct_column_implementation(capsys, monkeypatch):
    """Part 1. `input_guess` - function is correctly implemented for row."""
    module = reimport_module(MODULE)

    nums: list[str] = ["12"]
    set_stdin(monkeypatch, nums)
    module.input_guess(12, "row")
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Guess a row: ")
    _regex_test_stdout(lines, monkeypatch, regex)

    nums: list[str] = ["8", "3"]
    set_stdin(monkeypatch, nums)
    module.input_guess(7, "row")
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)The grid is only 7 by 7. Try again: ")
    _regex_test_stdout(lines, monkeypatch, regex)


@mark.weight(5)
def test_part_1_input_guess_correct_row_implementation(capsys, monkeypatch):
    """Part 1. `input_guess` - function is correctly implemented for column."""
    module = reimport_module(MODULE)

    nums: list[str] = ["5"]
    set_stdin(monkeypatch, nums)
    module.input_guess(5, "column")
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Guess a column: ")
    _regex_test_stdout(lines, monkeypatch, regex)

    nums: list[str] = ["0", "2"]
    set_stdin(monkeypatch, nums)
    module.input_guess(16, "column")
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)The grid is only 16 by 16. Try again: ")
    _regex_test_stdout(lines, monkeypatch, regex)


@mark.weight(5)
def test_part_1_input_guess_throws():
    """Part 1. `input_guess` - throws assertion error with wrong second argument string."""
    module = reimport_module(MODULE)
    input_guess = module.input_guess
    with raises(AssertionError):
        input_guess(3, "abc")


### PART 2
@mark.weight(5)
def test_part_2_checking_grid_miss_1(capsys, monkeypatch):
    """Part 2. print_grid` - correct grid is outputted for incorrectly guessed inputs."""
    expected: list[str] = ["🟦🟦🟦🟦", "🟦🟦🟦🟦", "🟦🟦🟦🟦", "🟦🟦⬜🟦"]
    for idx in range(0, len(expected)):
        reimport_module(MODULE)
        module.print_grid(4, 4, 3, False)
        output = _get_output(capsys)
        regex = re.compile(f"(?i){expected[idx]}")
        match_found = False
        match = regex.search(output[idx]) is not None
        match_found = match_found or match
        assert match_found, f"Output must match expectation exactly."


@mark.weight(5)
def test_part_2_checking_grid_miss_2(capsys, monkeypatch):
    """Part 2. print_grid` - correct grid is outputted for incorrectly guessed inputs."""
    expected: list[str] = ["🟦⬜🟦🟦🟦🟦", "🟦🟦🟦🟦🟦🟦", "🟦🟦🟦🟦🟦🟦", "🟦🟦🟦🟦🟦🟦","🟦🟦🟦🟦🟦🟦", "🟦🟦🟦🟦🟦🟦"]
    for idx in range(0, len(expected)):
        reimport_module(MODULE)
        module.print_grid(6, 1, 2, False)
        output = _get_output(capsys)
        regex = re.compile(f"(?i){expected[idx]}")
        match_found = False
        match = regex.search(output[idx]) is not None
        match_found = match_found or match
        assert match_found, f"Output must match expectation exactly."


@mark.weight(5)
def test_part_2_checking_grid_hit_1(capsys, monkeypatch):
    """Part 2. print_grid` - correct grid is outputted for correctly guessed inputs."""
    expected: list[str] = ["🟦🟦🟦", "🟦🟥🟦", "🟦🟦🟦"]
    for idx in range(0, len(expected)):
        reimport_module(MODULE)
        module.print_grid(3, 2, 2, True)
        output = _get_output(capsys)
        regex = re.compile(f"(?i){expected[idx]}")
        match_found = False
        match = regex.search(output[idx]) is not None
        match_found = match_found or match
        assert match_found, f"Output must match expectation exactly."


@mark.weight(5)
def test_part_2_checking_grid_hit_2(capsys, monkeypatch):
    """Part 2. print_grid` - correct grid is outputted for correctly guessed inputs."""
    expected: list[str] = ["🟦🟦🟦🟦🟦", "🟦🟦🟦🟦🟦", "🟦🟦🟦🟦🟦", "🟦🟦🟦🟦🟦", "🟦🟦🟦🟦🟥"]
    for idx in range(0, len(expected)):
        reimport_module(MODULE)
        module.print_grid(5, 5, 5, True)
        output = _get_output(capsys)
        regex = re.compile(f"(?i){expected[idx]}")
        match_found = False
        match = regex.search(output[idx]) is not None
        match_found = match_found or match
        assert match_found, f"Output must match expectation exactly."


### PART 3
@mark.weight(5)
def test_part_3_correct_guess_correctly_declared():
    """Part 3. `correct_guess` - function is correctly declared (name, parameter types, return type)."""
    module = reimport_module(MODULE)
    assert callable(module.correct_guess)
    assert_parameter_list(module.correct_guess, [int, int, int, int])
    assert_return_type(module.correct_guess, bool)


@mark.weight(5)
def test_part_3_correct_guess_correctly_implemented():
    """Part 3. `correct_guess` - function is correctly implemented."""
    module = reimport_module(MODULE)
    correct_guess = module.correct_guess
    assert correct_guess(2, 2, 2, 2)
    assert correct_guess(1, 3, 1, 3)
    assert correct_guess(4, 2, 4, 2)
    assert correct_guess(2, 4, 4, 2) is False
    assert correct_guess(1, 1, 3, 3) is False
    assert correct_guess(1, 2, 3, 4) is False
    
    
### PART 4
@mark.weight(5)
def test_part_4_main_correctly_declared():
    """Part 4. `main` - function is correctly declared (name, parameter types, return type)."""
    module = reimport_module(MODULE)
    assert callable(module.main)
    assert_parameter_list(module.main, [int, int, int])
    assert_return_type(module.main, None)


@mark.weight(5)
def test_part_4_main_correctly_implemented(capsys, monkeypatch):
    """Part 4. `main` - game is winnable after correct guess."""
    module = reimport_module(MODULE)
    nums: list[str] = ["1", "4"]
    set_stdin(monkeypatch, nums)
    module.main(5, 1, 4)
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    regex = re.compile("(?i)Turn 1/5")
    _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)You won in 1/5")
    _regex_test_stdout(lines, monkeypatch, regex)


@mark.weight(5)
def test_part_4_main_correctly_implemented_multiple_guesses(capsys, monkeypatch):
    """Part 4. `main` - game is winnable after multiple guesses."""
    module = reimport_module(MODULE)
    nums: list[str] = ["1", "1", "2", "2", "3", "3", "4", "4"]
    set_stdin(monkeypatch, nums)
    module.main(4, 4, 4)
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    for i in range(1, 4):
        regex = re.compile(f"(?i)Turn {i}/5")
        _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)You won in 4/5")
    _regex_test_stdout(lines, monkeypatch, regex)


@mark.weight(5)
def test_part_4_main_correctly_implemented_loses(capsys, monkeypatch):
    """Part 4. `main` - game is lost after five guesses."""
    module = reimport_module(MODULE)
    words: list[str] = ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
    set_stdin(monkeypatch, words)
    module.main(6, 1, 1)
    out: str
    out, _ = capsys.readouterr()
    lines: list[str] = out.split("\n")
    for i in range(1, 6):
        regex = re.compile(f"(?i)Turn {i}/5")
        _regex_test_stdout(lines, monkeypatch, regex)
    regex = re.compile("(?i)X/5")
    _regex_test_stdout(lines, monkeypatch, regex)


@mark.weight(5)
def test_part_4_main_correctly_calls_functions_with_input_guess(capsys, monkeypatch):
    """Part 4. `main` - makes use of the `input_guess` function."""
    module = reimport_module(MODULE)
    try:
        with mock.patch.object(module, "input_guess", wraps=module.input_guess) as student_input_guess:
            words: list[str] = ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
            set_stdin(monkeypatch, words)
            module.main(6, 1, 1)
            student_input_guess.assert_called()
    except AssertionError as e:
        e.args = ("Must call `input_guess` from `main`.",)
        raise e
    
@mark.weight(5)
def test_part_4_main_correctly_calls_functions_with_correct_guess(capsys, monkeypatch):
    """Part 4. `main` - makes use of the `correct_guess` function."""
    module = reimport_module(MODULE)
    try:
        with mock.patch.object(module, "correct_guess", wraps=module.correct_guess) as student_correct_guess:
            words: list[str] = ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
            set_stdin(monkeypatch, words)
            module.main(6, 1, 1)
            student_correct_guess.assert_called()
    except AssertionError as e:
        e.args = ("Must call `correct_guess` from `main`.",)
        raise e

@mark.weight(5)
def test_part_4_main_correctly_calls_functions_with_print_grid(capsys, monkeypatch):
    """Part 4. `main` - makes use of the `print_grid` function."""
    module = reimport_module(MODULE)
    try:
        with mock.patch.object(module, "print_grid", wraps=module.print_grid) as student_print_grid:
            words: list[str] = ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
            set_stdin(monkeypatch, words)
            module.main(6, 1, 1)
            student_print_grid.assert_called()
    except AssertionError as e:
        e.args = ("Must call `print_grid` from `main`.",)
        raise e