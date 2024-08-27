"""Tests for Execise 01 - Hype Machine."""

__author__ = "Kris Jordan <kris@cs.unc.edu>"


import re
import pytest
from pytest import mark
from typing import Any
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture
from graders.helpers import author_is_a_valid_pid, mute_output, set_stdin, import_module, reimport_module

MODULE = "exercises.ex01_chardle"
module: Any  # Global variable will hold the module object which can be reloaded


def test_author(capsys: CaptureFixture, monkeypatch: MonkeyPatch):
    """Part 0 - __author__ str variable is correct PID format."""
    set_stdin(monkeypatch, ["hello", "z"])  # 
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


@mark.weight(20)
def test_part_1_word_prompt(capsys, monkeypatch):
    """Part 1. Prompting for Inputs"""
    for inputs in [["hello", "e"], ["world", "p"], ["zzzzz", "y"]]:
        word, char = inputs
        set_stdin(monkeypatch, [word, char])
        reimport_module(MODULE)
        output = _get_output(capsys)
        regex = re.compile("(?i)Searching for " + char + " in " + word)
        match = regex.search(output[0]) is not None
        assert match, "Output must match expectation exactly. Check your spelling and spacing."


@mark.weight(20)
def test_part_2_checking_indices(capsys, monkeypatch):
    """Part 2. Checking Indices for Matches"""
    for inputs in [["hello", "e", [1]], ["heels", "e", [1, 2]], ["heels", "s", [4]], ["zzzzz", "z", [0, 1, 2, 3, 4]]]:
        word, char, indices = inputs
        set_stdin(monkeypatch, [word, char])
        reimport_module(MODULE)
        output = _get_output(capsys)
        for index in indices:
            regex = re.compile("(?i)" + char + " found at index " + str(index))
            match_found = False
            for line in output:
                match = regex.search(line) is not None
                match_found = match_found or match
            assert match_found, f"Given word {word}, we expected the output: {char} found at index {index}. Your code output was {output}"


@mark.weight(10)
def test_part_3_counting_matching_indices_many(capsys, monkeypatch):
    """Part 3. Counting Matching Indices (Many matching indices)."""
    for inputs in [["hello", "l", 2], ["aabbb", "b", 3], ["abbbb", "b", 4], ["zzzzz", "z", 5]]:
        word, char, count = inputs
        set_stdin(monkeypatch, [word, char])
        reimport_module(MODULE)
        output = _get_output(capsys)
        
        expected = f"{count} instances of {char} found in {word}"
        regex = re.compile(f"(?i){expected}")
        match_found = False
        for line in output:
            match = regex.search(line) is not None
            match_found = match_found or match
        assert match_found, f"Given word {word} and char {char}, we expected the output (notice pluralization of \"instances\"): {expected}"


@mark.weight(10)
def test_part_3_counting_matching_indices_one(capsys, monkeypatch):
    """Part 3. Counting Matching Indices (Singular matching index)."""
    for inputs in [["abcde", "a", 1], ["abcde", "b", 1], ["abcde", "c", 1]]:
        word, char, count = inputs
        set_stdin(monkeypatch, [word, char])
        reimport_module(MODULE)
        output = _get_output(capsys)
        
        expected = f"{count} instance of {char} found in {word}"
        regex = re.compile(f"(?i){expected}")
        match_found = False
        for line in output:
            match = regex.search(line) is not None
            match_found = match_found or match
        assert match_found, f"Given word {word} and char {char}, we expected the output (notice nonplural of \"instance\"): {expected}"


@mark.weight(10)
def test_part_3_counting_matching_indices_none(capsys, monkeypatch):
    """Part 3. Counting Matching Indices (No matching indices)."""
    for inputs in [["zzzzz", "y", 0]]:
        word, char, _count = inputs
        set_stdin(monkeypatch, [word, char])
        reimport_module(MODULE)
        output = _get_output(capsys)
        
        expected = f"No instances of {char} found in {word}"
        regex = re.compile(f"(?i){expected}")
        match_found = False
        for line in output:
            match = regex.search(line) is not None
            match_found = match_found or match
        assert match_found, f"Given word {word} and char {char}, we expected the output: {expected}"


@mark.weight(5)
def test_part_4_early_exit_invalid_word(capsys, monkeypatch):
    """Part 4. Exiting Early for Invalid Inputs (Word too short or too long)."""
    for inputs in [["", ""], ["a", ""], ["bb", ""], ["ccc", ""], ["dddd", ""], ["ffffff", ""], ["ggggggg", ""]]:
        did_not_exit = True
        with pytest.raises(SystemExit):
            set_stdin(monkeypatch, inputs)
            reimport_module(MODULE)
            did_not_exit = False
        assert did_not_exit, "Must call exit() with invalid input."
        (word, char) = inputs
        output = _get_output(capsys)
        correct_lines_of_output = len(output) == 1
        assert correct_lines_of_output, "Expected exactly one line of output in the error case."
        regex = re.compile("(?i)error")
        match = regex.search(output[0]) is not None
        assert match, "Output must match exercise specification exactly. Check your spelling and spacing of the error message."


@mark.weight(5)
def test_part_4_early_exit_invalid_char(capsys, monkeypatch):
    """Part 4. Exiting Early for Invalid Inputs (Char too short or too long)."""
    for inputs in [["abcde", ""], ["abcde", "aa"], ["abcde", "aaa"], ["abcde", "aaaa"], ["abcde", "aaaaa"], ["abcde", "aaaaaa"]]:
        did_not_exit = True
        with pytest.raises(SystemExit):
            set_stdin(monkeypatch, inputs)
            reimport_module(MODULE)
            did_not_exit = False
        assert did_not_exit, "Must call exit() with invalid input."
        (word, char) = inputs
        output = _get_output(capsys)
        correct_lines_of_output = len(output) == 1
        assert correct_lines_of_output, "Expected exactly one line of output in the error case."
        regex = re.compile("(?i)error")
        match = regex.search(output[0]) is not None
        assert match, "Output must match exercise specification exactly. Check your spelling and spacing of the error message."


# def test_word_too_long(capsys, monkeypatch):
#     """char_check.py - Input word greater than 5 characters."""
#     for inputs in [["bubbles", ""], ["alplhabet", ""]]:
#         did_not_exit = True
#         with pytest.raises(SystemExit):
#             set_stdin(monkeypatch, inputs)
#             reimport_module(MODULE)
#             did_not_exit = False
#         assert did_not_exit, "Must call exit() with invalid input."
#         (word, char) = inputs
#         output = _get_output(capsys)
#         correct_lines_of_output = len(output) == 1
#         assert correct_lines_of_output, "Expected exactly one line of output."
#         regex = re.compile("(?i)error")
#         match = regex.search(output[0]) is not None
#         assert match, "Output must match expectation exactly. Check your spelling and spacing."
