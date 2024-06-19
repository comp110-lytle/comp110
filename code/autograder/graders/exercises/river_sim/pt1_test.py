import re
import importlib
from pytest import mark
from graders.helpers import author_is_a_valid_pid, mute_output, set_stdin, import_module, reimport_module
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture
from typing import Any

RIV_MODULE = "ex06.river"
BEAR_MODULE = "ex06.bear"
FISH_MODULE = "ex06.fish"
RIVER_CLASS = "River"
BEAR_CLASS = "Bear"
FISH_CLASS = "Fish"
# riv_module: Any
# bear_module: Any
# fish_module: Any

@mark.weight(1)
def test_author(capsys: CaptureFixture, monkeypatch: MonkeyPatch):
    """0. __author__ str variable is correct PID format."""
    set_stdin(monkeypatch, ["hello", "z"])  # 
    mute_output(capsys)
    global module
    module = import_module(RIV_MODULE)
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


@mark.weight(5)
def test_bear_create(capsys,monkeypatch):
    """Part I: 1.1 + 1.2 A new Bear should have age 0 and hunger_score"""
    bear_module = import_module(BEAR_MODULE)
    new_bear = bear_module.Bear()
    assert new_bear.age == 0
    assert new_bear.hunger_score == 0
    
@mark.weight(4)
def test_fish_create(capsys,monkeypatch):
    """Part I: 2.1 + 2.2 A new Fish should have age 0"""
    fish_module = import_module(FISH_MODULE)
    new_fish = fish_module.Fish()
    assert new_fish.age == 0
    
# def _test_river_create(num_fish, num_bears):
#     river_module = import_module(RIV_MODULE)
#     new_river = river_module.River(num_fish, num_bears)
#     assert new_river.day == 0
#     assert len(new_river.fish) == num_fish
#     assert len(new_river.bears) == num_bears

# @mark.weight(0)
# def test_river_create1(capsys,monkeypatch):
#     """3.1 + 3.2 A new River should have day = 0, and the correct number of fish and bears"""
#     _test_river_create(3,2)

def _test_view_river(num_fish, num_bears):
    """returns the expected string output for view_river"""
    x = f"~~~ Day {0}: ~~~"
    y = f"Fish population: {num_fish}"
    z = f"Bear population: {num_bears}"
    return [x,y,z]

@mark.weight(10)
def test_view_river(capsys,monkeypatch):
    """Part I: 3.3 view_river Output Should Work for Any Amount of Fish and Bears"""
    river_module = import_module(RIV_MODULE)
    new_river = river_module.River(10, 11)
    new_river.view_river()
    output = _get_output(capsys)
    [x,y,z] = _test_view_river(10, 11)
    regex = re.compile(f"(?i){x}")
    match = regex.search(output[0]) is not None
    assert match, "Output must match expectation exactly. Check your spelling and spacing."
    regex = re.compile(f"(?i){y}")
    match = regex.search(output[1]) is not None
    assert match, "Output must match expectation exactly. Check your spelling and spacing."
    regex = re.compile(f"(?i){z}")
    match = regex.search(output[2]) is not None
    assert match, "Output must match expectation exactly. Check your spelling and spacing."

@mark.weight(5)
def test_bear_one_day(capsys):
    """Part I: 4.1 Calling one_day() in the Bear class should age Bear by one"""
    bear_module = import_module(BEAR_MODULE)
    new_bear = bear_module.Bear()
    new_bear.one_day()
    assert new_bear.age == 1
    
@mark.weight(5)
def test_fish_one_day(capsys):
    """Part I: 4.2 Calling one_day() in the Fish class should age Fish by one"""
    fish_module = import_module(FISH_MODULE)
    new_fish = fish_module.Fish()
    new_fish.one_day()
    assert new_fish.age == 1
    
@mark.weight(10)
def test_river_one_week(capsys):
     """Part I: 4.3 One River Week Should End With day = 7"""
     river_module = import_module(RIV_MODULE)
     new_river = river_module.River(1,1)
     new_river.one_river_week()
     print(new_river.day)
     assert new_river.day == 7
     