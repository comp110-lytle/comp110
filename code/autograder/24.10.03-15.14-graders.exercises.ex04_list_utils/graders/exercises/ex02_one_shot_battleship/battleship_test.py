"""Tests for Execise 02 - One Shot Battleship."""

__author__ = "Vrinda Desai <vrinda@email.unc.edu>"


import re
from pytest import mark
from typing import Any
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture
from graders.helpers import author_is_a_valid_pid, mute_output, set_stdin, import_module, reimport_module


MODULE = "ex02_one_shot_battleship"
module: Any  # Global variable will hold the module object which can be reloaded


@mark.weight(5)
def test_author(capsys: CaptureFixture, monkeypatch: MonkeyPatch):
    """Part 0 - __author__ str variable is correct PID format."""
    set_stdin(monkeypatch, ["1", "2"])  
    mute_output(capsys)
    global module
    module = import_module(MODULE)
    mute_output(capsys)
    assert author_is_a_valid_pid(module)


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

# Part 1: Prompting for a Guess (30 pts)
@mark.weight(5)
def test_part_1_guess_row_prompt_correct(capsys, monkeypatch):
    """Part 1. Inputting a row guess is prompted correctly."""
    set_stdin(monkeypatch, ["1", "2"])
    reimport_module(MODULE)
    output = _get_output(capsys)
    regex = re.compile("(?i)Guess a row: ")
    match_found = False
    for line in output:
        match = regex.search(line) is not None
        match_found = match_found or match
    assert match_found, "Output must match expectation exactly. Check your spelling and spacing."

@mark.weight(5)
def test_part_1_guess_column_prompt_correct(capsys, monkeypatch):
    """Part 1. Inputting a column guess is prompted correctly.."""
    set_stdin(monkeypatch, ["1", "2"])
    reimport_module(MODULE)
    output = _get_output(capsys)
    regex = re.compile("(?i)Guess a column: ")
    match_found = False
    for line in output:
        match = regex.search(line) is not None
        match_found = match_found or match
    assert match_found, "Output must match expectation exactly. Check your spelling and spacing."


@mark.weight(5)
def test_part_1_row_guess_too_low(capsys, monkeypatch):
    """Part 1. A low row guess is caught correctly."""
    set_stdin(monkeypatch, ["-1", "1", "2"])
    reimport_module(MODULE)
    output = _get_output(capsys)
    regex = re.compile("(?i)The grid is only 4 by 4. Try again: ")
    match_found = False
    for line in output:
        match = regex.search(line) is not None
        match_found = match_found or match
    assert match_found, "Output must match expectation exactly. Check your spelling and spacing."


@mark.weight(5)
def test_part_1_row_guess_too_high(capsys, monkeypatch):
    """Part 1. A high row guess is caught correctly."""
    set_stdin(monkeypatch, ["8", "2", "2"])
    reimport_module(MODULE)
    output = _get_output(capsys)
    regex = re.compile("(?i)The grid is only 4 by 4. Try again: ")
    match_found = False
    for line in output:
        match = regex.search(line) is not None
        match_found = match_found or match
    assert match_found, "Output must match expectation exactly. Check your spelling and spacing."

@mark.weight(5)
def test_part_1_column_guess_too_low(capsys, monkeypatch):
    """Part 1. A low column guess is caught correctly."""
    set_stdin(monkeypatch, ["3", "-7", "1"])
    reimport_module(MODULE)
    output = _get_output(capsys)
    regex = re.compile("(?i)The grid is only 4 by 4. Try again: ")
    match_found = False
    for line in output:
        match = regex.search(line) is not None
        match_found = match_found or match
    assert match_found, "Output must match expectation exactly. Check your spelling and spacing."

@mark.weight(5)
def test_part_1_column_guess_too_high(capsys, monkeypatch):
    """Part 1. A high column guess is caught correctly."""
    set_stdin(monkeypatch, ["3", "5", "7", "1"])
    reimport_module(MODULE)
    output = _get_output(capsys)
    regex = re.compile("(?i)The grid is only 4 by 4. Try again: ")
    match_found = False
    for line in output:
        match = regex.search(line) is not None
        match_found = match_found or match
    assert match_found, "Output must match expectation exactly. Check your spelling and spacing."

# Part 2: Print a Grid
@mark.weight(5)
def test_part_2_checking_grid_miss_1(capsys, monkeypatch):
    """Part 2. Correct grid is outputted for incorrectly guessed inputs."""
    expected: list[str] = ["⬜🟦🟦🟦", "🟦🟦🟦🟦", "🟦🟦🟦🟦", "🟦🟦🟦🟦"]
    for idx in range(0, len(expected)):
        set_stdin(monkeypatch, ["1", "1"])
        reimport_module(MODULE)
        output = _get_output(capsys)
        regex = re.compile(f"(?i){expected[idx]}")
        match_found = False
        match = regex.search(output[idx]) is not None
        match_found = match_found or match
        assert match_found, f"Output must match expectation exactly."


@mark.weight(5)
def test_part_2_checking_grid_miss_2(capsys, monkeypatch):
    """Part 2. Correct grid is outputted for incorrectly guessed inputs."""
    expected: list[str] = ["🟦🟦🟦🟦", "🟦⬜🟦🟦", "🟦🟦🟦🟦", "🟦🟦🟦🟦"]
    for idx in range(0, len(expected)):
        set_stdin(monkeypatch, ["2", "2"])
        reimport_module(MODULE)
        output = _get_output(capsys)
        regex = re.compile(f"(?i){expected[idx]}")
        match_found = False
        match = regex.search(output[idx]) is not None
        match_found = match_found or match
        assert match_found, f"Output must match expectation exactly."

@mark.weight(5)
def test_part_2_checking_grid_miss_3(capsys, monkeypatch):
    """Part 2. Correct grid is outputted for incorrectly guessed inputs."""
    expected: list[str] = ["🟦🟦🟦🟦", "🟦🟦🟦🟦", "🟦🟦⬜🟦", "🟦🟦🟦🟦"]
    for idx in range(0, len(expected)):
        set_stdin(monkeypatch, ["3", "3"])
        reimport_module(MODULE)
        output = _get_output(capsys)
        regex = re.compile(f"(?i){expected[idx]}")
        match_found = False
        match = regex.search(output[idx]) is not None
        match_found = match_found or match
        assert match_found, f"Output must match expectation exactly."

@mark.weight(5)
def test_part_2_checking_grid_miss_4(capsys, monkeypatch):
    """Part 2. Correct grid is outputted for incorrectly guessed inputs."""
    expected: list[str] = ["🟦🟦🟦🟦", "🟦🟦🟦🟦", "🟦🟦🟦🟦", "🟦🟦🟦⬜"]
    for idx in range(0, len(expected)):
        set_stdin(monkeypatch, ["4", "4"])
        reimport_module(MODULE)
        output = _get_output(capsys)
        regex = re.compile(f"(?i){expected[idx]}")
        match_found = False
        match = regex.search(output[idx]) is not None
        match_found = match_found or match
        assert match_found, f"Output must match expectation exactly."

@mark.weight(5)
def test_part_2_checking_grid_miss_5(capsys, monkeypatch):
    """Part 2. Correct grid is outputted for incorrectly guessed inputs."""
    expected: list[str] = ["🟦🟦🟦🟦", "🟦🟦⬜🟦", "🟦🟦🟦🟦", "🟦🟦🟦🟦"]
    for idx in range(0, len(expected)):
        set_stdin(monkeypatch, ["2", "3"])
        reimport_module(MODULE)
        output = _get_output(capsys)
        regex = re.compile(f"(?i){expected[idx]}")
        match_found = False
        match = regex.search(output[idx]) is not None
        match_found = match_found or match
        assert match_found, f"Output must match expectation exactly."

@mark.weight(5)
def test_part_2_checking_grid_hit(capsys, monkeypatch):
    """Part 2. Correct grid is outputted for correctly guessed inputs."""
    expected: list[str] = ["🟦🟦🟦🟦", "🟦🟦🟦🟦", "🟦🟥🟦🟦", "🟦🟦🟦🟦"]
    for idx in range(0, len(expected)):
        set_stdin(monkeypatch, ["3", "2"])
        reimport_module(MODULE)
        output = _get_output(capsys)
        regex = re.compile(f"(?i){expected[idx]}")
        match_found = False
        match = regex.search(output[idx]) is not None
        match_found = match_found or match
        assert match_found, f"Output must match expectation exactly."

# Part 3: Giving A Hint to Your User
@mark.weight(2.5)
def test_part_3_ship_hit(capsys, monkeypatch):
    """Part 3. Correct output when correct guess is made."""
    set_stdin(monkeypatch, ["3", "2"])
    reimport_module(MODULE)
    output = _get_output(capsys)
    regex = re.compile("(?i)Hit!")
    match_found = False
    for line in output:
        match = regex.search(line) is not None
        match_found = match_found or match
    assert match_found, "Output must match expectation exactly. Check your spelling and spacing."

@mark.weight(2.5)
def test_part_3_ship_missed(capsys, monkeypatch):
    """Part 3. Correct output when incorrect guess is made."""
    set_stdin(monkeypatch, ["1", "1"])
    reimport_module(MODULE)
    output = _get_output(capsys)
    regex = re.compile("(?i)Miss!")
    match_found = False
    for line in output:
        match = regex.search(line) is not None
        match_found = match_found or match
    assert match_found, "Output must match expectation exactly. Check your spelling and spacing."

@mark.weight(2.5)
def test_part_3_correct_row(capsys, monkeypatch):
    """Part 3. Correct output when only row guess is correct."""
    set_stdin(monkeypatch, ["3", "1"])
    reimport_module(MODULE)
    output = _get_output(capsys)
    regex = re.compile("(?i)Close! Correct row, wrong column.")
    match_found = False
    for line in output:
        match = regex.search(line) is not None
        match_found = match_found or match
    assert match_found, "Output must match expectation exactly. Check your spelling and spacing."

@mark.weight(2.5)
def test_part_3_correct_column(capsys, monkeypatch):
    """Part 3. Correct output when only column guess is correct."""
    set_stdin(monkeypatch, ["1", "2"])
    reimport_module(MODULE)
    output = _get_output(capsys)
    regex = re.compile("(?i)Close! Correct column, wrong row.")
    match_found = False
    for line in output:
        match = regex.search(line) is not None
        match_found = match_found or match
    assert match_found, "Output must match expectation exactly. Check your spelling and spacing."


