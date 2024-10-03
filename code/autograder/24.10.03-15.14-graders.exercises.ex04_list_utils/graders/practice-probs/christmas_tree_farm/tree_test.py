import re
import importlib
from pytest import mark
from graders.helpers import author_is_a_valid_pid, mute_output, set_stdin, import_module, reimport_module
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture
from typing import Any
import inspect
import types
from lessons.practice.tree_farm import ChristmasTreeFarm

TREE_MODULE = "lessons.practice.tree_farm"
TREE_CLASS = "ChristmasTreeFarm"

def _get_num_planted(tree_plots: list[int]):
    """Counts the number of trees planted."""
    tree_count: int = 0
    for tree in tree_plots:
        if tree > 0:
            tree_count += 1
    return tree_count
    

@mark.weight(1)
def test_constructor():
    """Part b: ChristmasTreeFarm constructor should have 3 parameters: self, int, and int."""
    module = import_module(TREE_MODULE)
    sig = inspect.signature(module.ChristmasTreeFarm.__init__)
    assert len(sig.parameters) == 3
    param_names = list(sig.parameters)
    vals = param_names[1]
    assert sig.parameters[vals].annotation == 'int'
    vals2 = param_names[2]
    assert sig.parameters[vals2].annotation == 'int'

@mark.weight(1)
def test_constructor_functionality():
    """Part b: Constructor should initialize self.plots with the correct amount of empty plots and planted trees."""
    module = reimport_module(TREE_MODULE)
    num_plots: int = 100
    num_planted: int = 20
    farm = module.ChristmasTreeFarm(num_plots, num_planted)
    assert len(farm.plots) == num_plots
    assert _get_num_planted(farm.plots) == 20

@mark.weight(1)
def test_plant():
    """Part c: plant method should have 2 parameters: self and int and return None."""
    module = reimport_module(TREE_MODULE)
    sig = inspect.signature(module.ChristmasTreeFarm.plant)
    assert len(sig.parameters) == 2
    param_names = list(sig.parameters)
    vals = param_names[1]
    assert sig.parameters[vals].annotation == 'int'
    assert sig.return_annotation == 'None'


@mark.weight(1)
def test_plant_functionality():
    """Part c: plant should create a tree of size 1 at the correct index."""
    num_plots: int = 100
    num_planted: int = 15
    plant_loc: int = 34
    farm = ChristmasTreeFarm(num_plots, num_planted)
    farm.plant(plant_loc)
    assert farm.plots[plant_loc] == 1

@mark.weight(1)
def test_growth():
    """Part d: growth method should take 1 parameter (self) and return None."""
    module = reimport_module(TREE_MODULE)
    sig = inspect.signature(module.ChristmasTreeFarm.growth)
    assert len(sig.parameters) == 1
    assert sig.return_annotation == 'None'


@mark.weight(1)
def test_growth_functionality():
    """Part d: growth should increase all existing trees by 1 and not increase unplanted trees."""
    num_plots: int = 100
    num_planted: int = 15
    farm = ChristmasTreeFarm(num_plots, num_planted)
    farm.growth()
    assert farm.plots[10] == 2
    farm.growth()
    assert farm.plots[10] == 3
    assert farm.plots[50] == 0
    
@mark.weight(1)
def test_harvest():
    """Part e: harvest method should have 2 parameters: self and bool and return int."""
    module = reimport_module(TREE_MODULE)
    sig = inspect.signature(module.ChristmasTreeFarm.harvest)
    assert len(sig.parameters) == 2
    param_names = list(sig.parameters)
    vals = param_names[1]
    assert sig.parameters[vals].annotation == 'bool'
    assert sig.return_annotation == 'int'


@mark.weight(1)
def test_harvest_functionality():
    """Part e: harvest should only harvest trees of size 5 or larger and return the number harvested."""
    num_plots: int = 100
    num_planted: int = 3
    farm = ChristmasTreeFarm(num_plots, num_planted)
    for x in range(0,6):
        farm.growth()
    # plant a young tree in another location for reference
    farm.plant(5)
    # all trees but the young plant should be harvested and none replanted
    assert farm.harvest(False) == 3


@mark.weight(1)
def test_harvest_functionality():
    """Part e: harvest should replant trees if argument is True."""
    num_plots: int = 100
    num_planted: int = 3
    farm = ChristmasTreeFarm(num_plots, num_planted)
    for x in range(0,6):
        farm.growth()
    # plant a young tree in another location for reference
    farm.plant(5)
    # all trees but the young plant should be harvested and 3 replanted
    farm.harvest(True)
    assert _get_num_planted(farm.plots) == 4
    
@mark.weight(1)
def test_harvest_functionality2():
    """Part e: harvest should not replant trees if argument is False."""
    num_plots: int = 100
    num_planted: int = 3
    farm = ChristmasTreeFarm(num_plots, num_planted)
    for x in range(0,6):
        farm.growth()
    # plant a young tree in another location for reference
    farm.plant(5)
    # all trees but the young plant should be harvested and 3 replanted
    farm.harvest(False)
    assert _get_num_planted(farm.plots) == 1

@mark.weight(1)
def test_add():
    """Part f: add method should have 2 parameters: self and ChristmasTreeFarm and return ChristmasTreeFarm."""
    module = reimport_module(TREE_MODULE)
    sig = inspect.signature(module.ChristmasTreeFarm.__add__)
    assert len(sig.parameters) == 2
    param_names = list(sig.parameters)
    vals = param_names[1]
    assert sig.parameters[vals].annotation == 'ChristmasTreeFarm'
    assert sig.return_annotation == 'ChristmasTreeFarm'


@mark.weight(1)
def test_add_functionality():
    """Part f: add should create correct amount of new empty plots."""
    num_plots: int = 100
    num_planted: int = 3
    num_plots2: int = 30
    num_planted2: int = 13
    farm = ChristmasTreeFarm(num_plots, num_planted)
    farm2 = ChristmasTreeFarm(num_plots2, num_planted2)
    try: 
        new_farm = farm + farm2
        assert len(new_farm.plots) == num_plots + num_plots2
    except:
        assert False, "__add__ not defined"
   
@mark.weight(1)
def test_add_functionality2():
    """Part f: add should plant correct amount of new trees."""
    num_plots: int = 100
    num_planted: int = 3
    num_plots2: int = 30
    num_planted2: int = 13
    farm = ChristmasTreeFarm(num_plots, num_planted)
    farm2 = ChristmasTreeFarm(num_plots2, num_planted2)
    try: 
        new_farm = farm + farm2
        assert _get_num_planted(new_farm.plots) == num_planted + num_planted2
    except:
        assert False, "__add__ not defined" 

# @mark.weight(1)
# def test_str_method():
#     """0: __str__ method should return a str with format x: <x_attribute>; y: <y_attribute>"""
#     tree_module = import_module(TREE_MODULE)
#     point_module = import_module(POINT_MODULE)
#     my_point = point_module.Point(3.0, 2.0)
#     assert str(my_point) == "x: 3.0; y: 2.0"
    
# @mark.weight(2)
# def test_mul_method_functionality():
#     """1: __mul__ method should return a Point with both attributes multiplied"""
#     point_module = import_module(POINT_MODULE)
#     my_point = point_module.Point(3.0, 2.0)
#     try: 
#        new_point =  my_point * 2
#     except:
#         assert False
#     test_point = point_module.Point(6.0, 4.0)
#     assert new_point.x == test_point.x
#     assert new_point.y == test_point.y
#     sig = inspect.signature(module.Point.__mul__)
#     assert sig.return_annotation == 'Point'
    
# @mark.weight(1)
# def test_mul_params():
#     """1.1: __mul__ should take the union of int and float as a parameter."""
#     module = reimport_module(POINT_MODULE)
#     sig = inspect.signature(module.Point.__mul__)
#     assert len(sig.parameters) == 2
#     param_names = list(sig.parameters)
#     vals = param_names[1]
#     assert sig.parameters[vals].annotation == "int | float"
    

   
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

