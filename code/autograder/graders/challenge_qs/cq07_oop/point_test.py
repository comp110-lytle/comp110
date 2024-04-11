"""Tests for OOP Challenge Question."""

__author__ = "Alyssa Lytle <abyrnes1@cs.unc.edu>"


import pytest
from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module
from graders.helpers import assert_return_type
import inspect


MODULE = "lessons.CQ08.point"


@mark.weight(0)
def test_author():
    """invert - __author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module)
    
@mark.weight(1)
def test_constructor_params():
    """Part 1. Point constructor should take two floats as input"""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Point.__init__)
    assert len(sig.parameters) == 3
    param_names = list(sig.parameters)
    vals = param_names[1]
    assert sig.parameters[vals].annotation == 'float'
    vals2 = param_names[2]
    assert sig.parameters[vals2].annotation == 'float'
    
@mark.weight(1)
def test_make_point_x():
    """Part 1. Testing that x attribute is initialized correctly in __init__"""
    from lessons.CQ08.point import Point
    test_point: Point = Point(1.0,2.0)
    assert test_point.x == 1.0

@mark.weight(1)
def test_make_point_y():
    """Part 1. Testing that y attribute is initialized correctly in __init__"""
    from lessons.CQ08.point import Point
    test_point: Point = Point(1.0,2.0)
    assert test_point.y == 2.0

@mark.weight(1)
def test_scale_by_signature():
    """Part 2. scale_by should have self and int as parameters and return None"""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Point.scale_by)
    assert len(sig.parameters) == 2
    assert sig.return_annotation == 'None'

# @mark.weight(1)
# def test_scale_by_params():
#     
#     module = reimport_module(MODULE)
#     assert_parameter_list(module.scale_by, [int])

# @mark.weight(1)
# def test_scale_by_return_type():
#     """Part 2. scale_by should return None"""
#     module = reimport_module(MODULE)
#     assert_return_type(module.scale_by, None)


@mark.weight(1)
def test_scale_by_x():
    """Part 2. Testing that scale_by modifies x attribute correctly"""
    from lessons.CQ08.point import Point
    test_point: Point = Point(1.0,2.0)
    test_point.scale_by(3)
    assert test_point.x == 3.0

@mark.weight(1)
def test_scale_by_y():
    """Part 2. Testing that scale_by modifies y attribute correctly"""
    from lessons.CQ08.point import Point
    test_point: Point = Point(1.0,2.0)
    test_point.scale_by(3)
    assert test_point.y == 6.0


   
# @mark.weight(1)
# def test_scale_return_type():
#     """Part 3. scale should return Point"""
#     module = reimport_module(MODULE)
#     assert_return_type(module.scale_by, Point)
 
@mark.weight(1)
def test_scale_by_signature():
    """Part 3. scale should have self and int as parameters and return Point"""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Point.scale)
    assert len(sig.parameters) == 2
    assert sig.return_annotation == 'Point'


@mark.weight(1)
def test_scale_mutation():
    """Part 3. Testing that scale does not modify input"""
    from lessons.CQ08.point import Point
    test_point: Point = Point(1.0,2.0)
    test_point.scale(3)
    assert test_point.x == 1.0
   

@mark.weight(1)
def test_scale_x():
    """Part 3. Testing that scale correctly creates new point with updated x attribute"""
    from lessons.CQ08.point import Point
    test_point: Point = Point(1.0,2.0)
    test_point2: Point = test_point.scale(4)
    assert test_point2.x == 4.0

@mark.weight(1)
def test_scale_y():
    """Part 3. Testing that scale correctly creates new point with updated y attribute"""
    from lessons.CQ08.point import Point
    test_point: Point = Point(1.0,2.0)
    test_point2: Point = test_point.scale(4)
    assert test_point2.y == 8.0