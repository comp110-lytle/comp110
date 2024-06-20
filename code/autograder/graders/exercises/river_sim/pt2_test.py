import re
import importlib
from pytest import mark
from graders.helpers import import_module
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture
from typing import Any
import inspect

RIV_MODULE = "ex06.river"
BEAR_MODULE = "ex06.bear"
FISH_MODULE = "ex06.fish"
RIVER_CLASS = "River"
BEAR_CLASS = "Bear"
FISH_CLASS = "Fish"
# riv_module: Any
# bear_module: Any
# fish_module: Any




# def _regex_test_stdout(capsys, regex):
#     out, _err = capsys.readouterr()
#     lines = out.split("\n")
#     match = False
#     print(lines)
#     for line in lines:
#         if line.trim() == "":
#             continue
#         if regex.search(line) is not None:
#             match = True
#     assert match, "Output must match exactly. Check your spelling and spacing."     


# def _get_output(capsys):
#     out, _err = capsys.readouterr()
#     lines = out.split("\n")
#     lines = list(filter(lambda s: s != "", lines))
#     return lines


@mark.weight(3)
def test_check_ages(capsys):
    """Part II: 1.1 check_ages should remove any Fish with age > 3 and Bear with age > 5"""
    river_module = import_module(RIV_MODULE)
    new_river = river_module.River(1,1)
    new_river.fish[0].age = 4
    new_river.bears[0].age = 6
    new_river.check_ages()
    assert len(new_river.fish) == 0
    assert len(new_river.bears) == 0
    
@mark.weight(2)
def test_check_ages2(capsys):
    """Part II: 1.1 check_ages should not remove any Fish with age <= 3 and Bear with age <= 5"""
    river_module = import_module(RIV_MODULE)
    new_river = river_module.River(1,1)
    new_river.fish[0].age = 3
    new_river.bears[0].age = 5
    new_river.check_ages()
    assert len(new_river.fish) == 1
    assert len(new_river.bears) == 1
    
@mark.weight(5)
def test_remove_fish(capsys):
    """Part II: 1.2 remove_fish should remove frontmost fish from river"""
    river_module = import_module(RIV_MODULE)
    new_river = river_module.River(2,1)
    new_river.fish[0].age = 3
    new_river.remove_fish(1)
    assert new_river.fish[0].age == 0
    
@mark.weight(5)
def test_bear_one_day():
    """Part II: 2.1 Bear one_day method should decrease hunger score by 1"""
    bear_module = import_module(BEAR_MODULE)
    new_bear = bear_module.Bear()
    new_bear.one_day()
    assert new_bear.hunger_score == -1

@mark.weight(5)
def test_bear_eat():
    """Part II: 2.2 Bear eat() method should increase the Bear's hunger score"""
    bear_module = import_module(BEAR_MODULE)
    new_bear = bear_module.Bear()
    new_bear.eat(5)
    assert new_bear.hunger_score == 5

@mark.weight(2)
def test_bears_eating():
    """Part II: 2.3 bears_eating() method: if there are at least 5 Fish in the river, the Bear will eat 3 Fish"""
    river_module = import_module(RIV_MODULE)
    new_river = river_module.River(9,2)
    new_river.bears_eating()
    assert len(new_river.fish) == 3
    
@mark.weight(3)
def test_bears_eating2():
    """Part II: 2.3 bears_eating() method: if there are less than 5 Fish in the river at least one Bear won't eat"""
    river_module = import_module(RIV_MODULE)
    new_river = river_module.River(7,2)
    new_river.bears_eating()
    assert len(new_river.fish) == 4

@mark.weight(5)
def test_check_hunger():
    """Part II: 2.4 Any Bear's with hunger score < 0 will be removed from river"""
    river_module = import_module(RIV_MODULE)
    new_river = river_module.River(7,2)
    new_river.bears[0].hunger_score = -1
    new_river.check_hunger()
    assert len(new_river.bears) == 1


@mark.weight(1)
def test_for_inf_loop_repop_bears():
    """Part II: 3.2 repopulate_bears should not have len(self.bears) in the loop condition."""
    river_module = import_module(RIV_MODULE)
    new_river = river_module.River(1,1)
    sc = inspect.getsource(new_river.repopulate_bears)
    sc_arr = sc.split('\n')
    for line in sc_arr:
        assert not (("while" in line) and ("len(self.bears)" in line))


@mark.weight(4)
def test_repop_bears():
    """Part II: 3.1  repopulate_bears method: for n bears, there will be n//2 new Bears added to bears."""
    try:
        river_module = import_module(RIV_MODULE)
        new_river = river_module.River(7,2)
        new_river.repopulate_bears()
        amount_of_new_bears: int = 2//2
        assert len(new_river.bears) == (2+ amount_of_new_bears)
    except:
        assert False, "Unable to call repopulate_bears()"

@mark.weight(1)
def test_for_inf_loop():
    """Part II: 3.2 repopulate_fish should not have len(self.fish) in the loop condition."""
    river_module = import_module(RIV_MODULE)
    new_river = river_module.River(1,1)
    sc = inspect.getsource(new_river.repopulate_fish)
    sc_arr = sc.split('\n')
    for line in sc_arr:
        assert not (("while" in line) and ("len(self.fish)" in line))

@mark.weight(4)
def test_repop_fish():
    """Part II: 3.2 repopulate_fish method: for n fish, there will be (n//2) * 4 new Fish added to fish."""
    try:
        river_module = import_module(RIV_MODULE)
        new_river = river_module.River(7,2)
        new_river.repopulate_fish()
        amount_of_new_fish: int = (7//2)*4
        assert len(new_river.fish) == (7+ amount_of_new_fish)
    except:
        assert False, "Unable to call repopulate_fish()"
 