"""Tests for OOP Challenge Question."""

__author__ = "Alyssa Lytle <abyrnes1@cs.unc.edu>"


import pytest
from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module
from graders.helpers import assert_return_type
import inspect


MODULE = "CQs.cq07.point"


@mark.weight(1)
def test_author():
    """invert - __author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module)
    
@mark.weight(1)
def test_constructor_params():
    """Part 1.1. Point constructor should take two floats as input."""
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
    """Part 1.1. Testing that x and y attributes are initialized correctly in __init__."""
    module = reimport_module(MODULE)
    test_point = module.Point(1.0,2.0)
    assert test_point.x == 1.0
    assert test_point.y == 2.0


@mark.weight(1)
def test_scale_by_signature():
    """Part 1.2. scale_by signature should have self and int as parameters and return None."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Point.scale_by)
    assert len(sig.parameters) == 2
    assert sig.return_annotation == 'None'
    
@mark.weight(1)
def test_scale_by_ret_val():
    """Part 1.2. Testing that scale_by doesn't return anything."""
    module = reimport_module(MODULE)
    test_point = module.Point(1.0,2.0)
    test_point.scale_by(3)
    assert test_point.scale_by(3) is None

@mark.weight(1)
def test_scale_by_x():
    """Part 1.2. Testing that scale_by modifies x and y attributes correctly."""
    module = reimport_module(MODULE)
    test_point = module.Point(1.0,2.0)
    test_point.scale_by(3)
    assert test_point.x == 3.0
    assert test_point.y == 6.0


@mark.weight(1)
def test_str_signature():
    """Part 2.1. __str__ signature should have self as a parameter and return a str."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Point.__str__)
    assert len(sig.parameters) == 1
    assert sig.return_annotation == 'str'
    
@mark.weight(1)
def test_str_mutation():
    """Part 2.1. Testing that __str__ does not modify input."""
    module = reimport_module(MODULE)
    test_point = module.Point(1.0,2.0)
    str(test_point)
    assert test_point.x == 1.0
    
@mark.weight(1)
def test_str_output():
    """Part 2.1 Testing that __str__ returns the desired output."""
    module = reimport_module(MODULE)
    test_point = module.Point(4.0,4.0)
    assert str(test_point) == "x: 4.0; y: 4.0"
 
@mark.weight(1)
def test_mul_signature():
    """Part 2.2. __mul__ signature should have self and int as parameters and return a Point."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Point.__mul__)
    assert len(sig.parameters) == 2
    assert sig.return_annotation == 'Point'


@mark.weight(1)
def test_scale_mutation():
    """Part 2.2. Testing that __mul__ does not modify input."""
    module = reimport_module(MODULE)
    test_point = module.Point(1.0,2.0)
    test_point * 3
    assert test_point.x == 1.0
   

@mark.weight(1)
def test_scale_x():
    """Part 2.2. Testing that __mul__ correctly creates new point with updated x and y attributes."""
    module = reimport_module(MODULE)
    test_point = module.Point(1.0,2.0)
    test_point2 = test_point * 4
    assert test_point2.x == 4.0
    assert test_point2.y == 8.0



@mark.weight(1)
def test_add_signature():
    """Part 2.3. __add__ signature should have self and int as parameters and return a Point."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Point.__add__)
    assert len(sig.parameters) == 2
    assert sig.return_annotation == 'Point'


@mark.weight(1)
def test_add_mutation():
    """Part 2.3. Testing that __add__ does not modify input."""
    module = reimport_module(MODULE)
    test_point = module.Point(1.0,2.0)
    test_point + 3
    assert test_point.x == 1.0
   

@mark.weight(1)
def test_add_x():
    """Part 2.3. Testing that __add__ correctly creates new point with updated x and y attributes."""
    module = reimport_module(MODULE)
    test_point = module.Point(1.0,2.0)
    test_point2 = test_point + 4
    assert test_point2.x == 5.0
    assert test_point2.y == 6.0