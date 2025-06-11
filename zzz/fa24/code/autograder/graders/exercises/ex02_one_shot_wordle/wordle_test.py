"""Tests for Execise 02 - Wordle."""

__author__ = "Kris Jordan <kris@cs.unc.edu>"


import re
from pytest import mark
from typing import Any
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture
from graders.helpers import author_is_a_valid_pid, mute_output, set_stdin, import_module, reimport_module


MODULE = "exercises.ex02_one_shot_wordle"
module: Any  # Global variable will hold the module object which can be reloaded


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


@mark.weight(5)
def test_part_1_word_prompt_correct(capsys, monkeypatch):
    """Part 1. Prompting for Inputs - Using expected secret word `python`."""
    words: list[str] = ["python"]
    set_stdin(monkeypatch, words)
    reimport_module(MODULE)
    output = _get_output(capsys)
    regex = re.compile("(?i)You got it")
    match_found = False
    for line in output:
        match = regex.search(line) is not None
        match_found = match_found or match
    assert match_found, "Given word `python`, expected to find \"You got it\" in output."


@mark.weight(5)
def test_part_1_word_prompt_incorrect(capsys, monkeypatch):
    """Part 1. Prompting for Inputs - Using incorrect secret word `foobar`."""
    words: list[str] = ["foobar"]
    set_stdin(monkeypatch, words)
    reimport_module(MODULE)
    output = _get_output(capsys)
    regex = re.compile("(?i)Play again")
    match_found = False
    for line in output:
        match = regex.search(line) is not None
        match_found = match_found or match
    assert match_found, "Given word `foobar`, expected to find \"Play again\" in output."


@mark.weight(10)
def test_part_1_word_prompt_too_short(capsys, monkeypatch):
    """Part 1. Prompting for Inputs - Using too short of word lengths when correct length is 6."""
    words: list[str] = ["a", "bb", "ccc", "eeeeee"]
    set_stdin(monkeypatch, words)
    reimport_module(MODULE)
    output = _get_output(capsys)
    regex = re.compile("(?i)Try again")
    matches_found = False
    for line in output:
        matches_found += len(regex.findall(line))
    assert matches_found == 3, "Given 3x words of incorrect length, expected to find \"Try again\" in output 3x times."


@mark.weight(10)
def test_part_1_word_prompt_too_long(capsys, monkeypatch):
    """Part 1. Prompting for Inputs - Using too long of word lengths when correct length is 6."""
    words: list[str] = ["88888888", "999999999", "0000000000", "88888888", "999999999", "0000000000", "eeeeee"]
    set_stdin(monkeypatch, words)
    reimport_module(MODULE)
    output = _get_output(capsys)
    regex = re.compile("(?i)Try again")
    matches_found = False
    for line in output:
        matches_found += len(regex.findall(line))
    assert matches_found == 6, "Given 6x words of incorrect lengths, expected to find \"Try again\" in output 6x times."


@mark.weight(30)
def test_part_2_checking_indices(capsys, monkeypatch):
    """Part 2. Checking Indices for Correct Matches - Expecting secret `python`."""
    words: list[str] = ["python", "aaaaaa", "mythic", "ayaaaa", "aataaa", "bbbhbb", "bbbbob", "zzzzzn"]
    expected: list[str] = ["🟩🟩🟩🟩🟩🟩", "⬜⬜⬜⬜⬜⬜", "⬜🟩🟩🟩⬜⬜", "⬜🟩⬜⬜⬜⬜", "⬜⬜🟩⬜⬜⬜", "⬜⬜⬜🟩⬜⬜", "⬜⬜⬜⬜🟩⬜", "⬜⬜⬜⬜⬜🟩"]
    for idx, word in enumerate(words):
        set_stdin(monkeypatch, [word])
        reimport_module(MODULE)
        output = _get_output(capsys)
        regex = re.compile(f"(?i){expected[idx]}")
        match_found = False
        for line in output:
            match = regex.search(line) is not None
            match_found = match_found or match
        assert match_found, f"Given guess {word}, expected to {expected[idx]}."


@mark.weight(10)
def test_part_3_checking_indices(capsys, monkeypatch):
    """Part 3. Correct Letters at Incorrect Indices - Expecting secret `python`."""
    words: list[str] = ["nohtyp", "pointy", "jumped"]
    expected: list[str] = ["🟨🟨🟨🟨🟨🟨", "🟩🟨⬜🟨🟨🟨", "⬜⬜🟨⬜⬜"]
    for idx, word in enumerate(words):
        set_stdin(monkeypatch, [word])
        reimport_module(MODULE)
        output = _get_output(capsys)
        regex = re.compile(f"(?i){expected[idx]}")
        match_found = False
        for line in output:
            match = regex.search(line) is not None
            match_found = match_found or match
        assert match_found, f"Given guess {word}, expected to {expected[idx]}."

