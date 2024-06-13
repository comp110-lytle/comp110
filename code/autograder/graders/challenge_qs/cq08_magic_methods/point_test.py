import re
import importlib
from pytest import mark
from graders.helpers import author_is_a_valid_pid, mute_output, set_stdin, import_module, reimport_module
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture
from typing import Any
import inspect
import types

POINT_MODULE = "lessons.CQ08.point"
POINT_CLASS = "Point"

# riv_module: Any
# bear_module: Any
# fish_module: Any

@mark.weight(0)
def test_author(capsys: CaptureFixture, monkeypatch: MonkeyPatch):
    """0. __author__ str variable is correct PID format."""
    set_stdin(monkeypatch, ["hello", "z"])  # 
    mute_output(capsys)
    global module
    module = import_module(POINT_MODULE)
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

@mark.weight(2)
def test_str_method():
    """0: __str__ method should return a str with format x: <x_attribute>; y: <y_attribute>"""
    point_module = import_module(POINT_MODULE)
    my_point = point_module.Point(3.0, 2.0)
    assert str(my_point) == "x: 3.0; y: 2.0"
    
@mark.weight(2)
def test_mul_method_functionality():
    """1: __mul__ method should return a Point with both attributes multiplied"""
    point_module = import_module(POINT_MODULE)
    my_point = point_module.Point(3.0, 2.0)
    try: 
       new_point =  my_point * 2
    except:
        assert False
    test_point = point_module.Point(6.0, 4.0)
    assert new_point.x == test_point.x
    assert new_point.y == test_point.y
    sig = inspect.signature(module.Point.__mul__)
    assert sig.return_annotation == 'Point'
    
@mark.weight(2)
def test_mul_params():
    """1.1: __mul__ should take the union of int and float as a parameter."""
    module = reimport_module(POINT_MODULE)
    sig = inspect.signature(module.Point.__mul__)
    assert len(sig.parameters) == 2
    param_names = list(sig.parameters)
    vals = param_names[1]
    assert sig.parameters[vals].annotation == "int | float"
    

   
@mark.weight(2)
def test_add_method_functionality():
    """1: __add__ method should return a Point with both attributes increased by a factor."""
    point_module = import_module(POINT_MODULE)
    my_point = point_module.Point(3.0, 4.0)
    try: 
       new_point =  my_point + 2
    except:
        assert False
    test_point = point_module.Point(5.0, 6.0)
    assert new_point.x == test_point.x
    assert new_point.y == test_point.y
    sig = inspect.signature(module.Point.__add__)
    assert sig.return_annotation == 'Point'
    
@mark.weight(2)
def test_add_params():
    """2.1: __add__ should take the union of int and float as a parameter."""
    module = reimport_module(POINT_MODULE)
    sig = inspect.signature(module.Point.__add__)
    assert len(sig.parameters) == 2
    param_names = list(sig.parameters)
    vals = param_names[1]
    assert sig.parameters[vals].annotation == "int | float"
    

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
