import re
import importlib
from pytest import mark
from graders.helpers import author_is_a_valid_pid, mute_output, set_stdin, import_module, reimport_module
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture
from typing import Any
import inspect
import types

MODULE = "lessons.data_practice.data_utils"


# riv_module: Any
# bear_module: Any
# fish_module: Any

@mark.weight(0)
def test_author(capsys: CaptureFixture, monkeypatch: MonkeyPatch):
    """0. __author__ str variable is correct PID format."""
    set_stdin(monkeypatch, ["hello", "z"])  # 
    mute_output(capsys)
    global module
    module = import_module(MODULE)
    mute_output(capsys)
    assert author_is_a_valid_pid(module)


@mark.weight(2)
def test_columnar_params():
    """columnar should take a list[dict[str, str]] as param."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.columnar)
    assert len(sig.parameters) == 1
    param_names = list(sig.parameters)
    vals = param_names[0]
    assert sig.parameters[vals].annotation == list[dict[str,str]]
    
@mark.weight(2)
def test_columnar_ret():
    """columnar should return a dict[str, list[str]]."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.columnar)
    assert sig.return_annotation == dict[str, list[str]]
    
@mark.weight(5)
def test_columnar_functionality():
    """columnar should work for a generic input."""
    module = reimport_module(MODULE)
    test_d = [{'Hello': '1', 'World': '2'}, {'Hello': '3', 'World': '4'}]
    test_result = {"Hello" : ["1", "3"], "World": ["2", "4"]}
    assert module.columnar(test_d) == test_result
   
# @mark.weight(2)
# def test_add_method_functionality():
#     """1: __add__ method should return a Point with both attributes increased by a factor."""
#     point_module = import_module(POINT_MODULE)
#     my_point = point_module.Point(3.0, 4.0)
#     try: 
#        new_point =  my_point + 2
#     except:
#         assert False
#     test_point = point_module.Point(5.0, 6.0)
#     assert new_point.x == test_point.x
#     assert new_point.y == test_point.y
#     sig = inspect.signature(module.Point.__add__)
#     assert sig.return_annotation == 'Point'
    
# @mark.weight(1)
# def test_add_params():
#     """2.1: __add__ should take the union of int and float as a parameter."""
#     module = reimport_module(POINT_MODULE)
#     sig = inspect.signature(module.Point.__add__)
#     assert len(sig.parameters) == 2
#     param_names = list(sig.parameters)
#     vals = param_names[1]
#     assert sig.parameters[vals].annotation == "int | float"
    

# @mark.weight(1)
# def test_default_params():
#     """3: Point contructor should have default values of 0.0 for both x and y"""
#     point_module = reimport_module(POINT_MODULE)
#     try:
#         my_point = point_module.Point()
#     except:
#         assert False
#     assert my_point.x == 0.0
#     assert my_point.y == 0.0
    
# @mark.weight(1)
# def test_default_params_constructor():
#     """3: Default values shouldn't have impacted existing constructor"""
#     point_module = reimport_module(POINT_MODULE)
#     try:
#         my_point = point_module.Point(2.0,2.0)
#     except:
#         assert False
#     assert my_point.x == 2.0
#     assert my_point.y == 2.0

# @mark.weight(5)
# def test_bear_create(capsys,monkeypatch):
#     """Part I: 1.1 + 1.2 A new Bear should have age 0 and hunger_score"""
#     bear_module = import_module(BEAR_MODULE)
#     new_bear = bear_module.Bear()
#     assert new_bear.age == 0
#     assert new_bear.hunger_score == 0
    
# @mark.weight(4)
# def test_fish_create(capsys,monkeypatch):
#     """Part I: 2.1 + 2.2 A new Fish should have age 0"""
#     fish_module = import_module(FISH_MODULE)
#     new_fish = fish_module.Fish()
#     assert new_fish.age == 0
    
# # def _test_river_create(num_fish, num_bears):
# #     river_module = import_module(RIV_MODULE)
# #     new_river = river_module.River(num_fish, num_bears)
# #     assert new_river.day == 0
# #     assert len(new_river.fish) == num_fish
# #     assert len(new_river.bears) == num_bears

# # @mark.weight(0)
# # def test_river_create1(capsys,monkeypatch):
# #     """3.1 + 3.2 A new River should have day = 0, and the correct number of fish and bears"""
# #     _test_river_create(3,2)

# def _test_view_river(num_fish, num_bears):
#     """returns the expected string output for view_river"""
#     x = f"~~~ Day {0}: ~~~"
#     y = f"Fish population: {num_fish}"
#     z = f"Bear population: {num_bears}"
#     return [x,y,z]

# @mark.weight(10)
# def test_view_river(capsys,monkeypatch):
#     """Part I: 3.3 view_river Output Should Work for Any Amount of Fish and Bears"""
#     river_module = import_module(RIV_MODULE)
#     new_river = river_module.River(10, 11)
#     new_river.view_river()
#     output = _get_output(capsys)
#     [x,y,z] = _test_view_river(10, 11)
#     regex = re.compile(f"(?i){x}")
#     match = regex.search(output[0]) is not None
#     assert match, "Output must match expectation exactly. Check your spelling and spacing."
#     regex = re.compile(f"(?i){y}")
#     match = regex.search(output[1]) is not None
#     assert match, "Output must match expectation exactly. Check your spelling and spacing."
#     regex = re.compile(f"(?i){z}")
#     match = regex.search(output[2]) is not None
#     assert match, "Output must match expectation exactly. Check your spelling and spacing."

# @mark.weight(5)
# def test_bear_one_day(capsys):
#     """Part I: 4.1 Calling one_day() in the Bear class should age Bear by one"""
#     bear_module = import_module(BEAR_MODULE)
#     new_bear = bear_module.Bear()
#     new_bear.one_day()
#     assert new_bear.age == 1
    
# @mark.weight(5)
# def test_fish_one_day(capsys):
#     """Part I: 4.2 Calling one_day() in the Fish class should age Fish by one"""
#     fish_module = import_module(FISH_MODULE)
#     new_fish = fish_module.Fish()
#     new_fish.one_day()
#     assert new_fish.age == 1
    
# @mark.weight(10)
# def test_river_one_week(capsys):
#      """Part I: 4.3 One River Week Should End With day = 7"""
#      river_module = import_module(RIV_MODULE)
#      new_river = river_module.River(1,1)
#      new_river.one_river_week()
#      print(new_river.day)
#      assert new_river.day == 7
     