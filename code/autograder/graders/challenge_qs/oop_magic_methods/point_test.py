"""Tests for OOP Challenge Question."""

__author__ = "Alyssa Lytle <abyrnes1@cs.unc.edu>"


import pytest
from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module
from graders.helpers import assert_return_type
import inspect


POINT_MODULE = "CQs.cq04.point"
LINE_MODULE = "CQs.cq04.line"


@mark.weight(0)
def test_author():
    """__author__ str variable is correct PID format."""
    module = reimport_module(POINT_MODULE)
    assert author_is_a_valid_pid(module)
    
@mark.weight(1)
def test_constructor_params():
    """Part 0. Point constructor should take two floats as input."""
    module = reimport_module(POINT_MODULE)
    sig = inspect.signature(module.Point.__init__)
    assert len(sig.parameters) == 3
    param_names = list(sig.parameters)
    vals = param_names[1]
    assert sig.parameters[vals].annotation == 'float'
    vals2 = param_names[2]
    assert sig.parameters[vals2].annotation == 'float'

@mark.weight(1)
def test_make_point():
    """Part 0. Testing that attributes are initialized correctly in Point##__init__."""
    module = reimport_module(POINT_MODULE)
    test_point = module.Point(3.0,2.0)
    assert test_point.x == 3.0
    assert test_point.y == 2.0

    
@mark.weight(1)
def test_make_line():
    """Part 0. Testing that attributes are initialized correctly in Line##__init__."""
    pmodule = reimport_module(POINT_MODULE)
    module = reimport_module(LINE_MODULE)
    p1 = pmodule.Point(4.0,5.0)
    p2 = pmodule.Point(6.0,7.0)
    l1 = module.Line(p1,p2)
    assert l1.p1.x == 4.0
    assert l1.p1.y == 5.0
    assert l1.p2.x == 6.0
    assert l1.p2.y == 7.0


### Point#__str__ ###

@mark.weight(1)
def test_point_str_signature():
    """Part 1. Point#__str__ signature should have self as parameter and str return type."""
    module = reimport_module(POINT_MODULE)
    sig = inspect.signature(module.Point.__str__)
    assert len(sig.parameters) == 1
    assert sig.return_annotation == 'str'
    
@mark.weight(1)
def test_point_str_mutation():
    """Part 1. Point#__str__ should not mutate `self`."""
    module = reimport_module(POINT_MODULE)
    test_point = module.Point(3.0, 2.0)
    str(test_point)
    assert test_point.x == 3.0
    assert test_point.y == 2.0

@mark.weight(1)
def test_point_str_ret_val():
    """Part 1. Testing that Point#__str__ returns expected value."""
    module = reimport_module(POINT_MODULE)
    test_point = module.Point(3.0,2.0)
    assert str(test_point) == "(3.0, 2.0)"



### Point#__mul__ ###
 
@mark.weight(1)
def test_point_mul_signature():
    """Part 2. Point#__mul__ signature should have self and int as parameters and return a Point."""
    module = reimport_module(POINT_MODULE)
    sig = inspect.signature(module.Point.__mul__)
    assert len(sig.parameters) == 2
    assert sig.return_annotation == 'Point'


@mark.weight(1)
def test_point_mul_mutation():
    """Part 2. Point#__mul__ should not mutate `self`."""
    module = reimport_module(POINT_MODULE)
    test_point = module.Point(3.0,2.0)
    test_point * 3
    assert test_point.x == 3.0
   

@mark.weight(1)
def test_point_mul():
    """Part 2. Testing that Point#__mul__ correctly creates new Point with updated x and y attributes."""
    module = reimport_module(POINT_MODULE)
    test_point = module.Point(1.0,2.0)
    test_point2 = test_point * 4
    assert test_point2.x == 4.0
    assert test_point2.y == 8.0



### Line#__str__ ###

@mark.weight(1)
def test_line_str_signature():
    """Part 3. Line#__str__ signature should have self as parameter and str return type."""
    
    module = reimport_module(LINE_MODULE)
    sig = inspect.signature(module.Line.__str__)
    assert len(sig.parameters) == 1
    assert sig.return_annotation == 'str'
    
@mark.weight(1)
def test_line_str_mutation():
    """Part 3. Linet#__str__ should not mutate `self`."""
    pmodule = reimport_module(POINT_MODULE)
    module = reimport_module(LINE_MODULE)
    p1 = pmodule.Point(4.0,5.0)
    p2 = pmodule.Point(6.0,7.0)
    l1 = module.Line(p1,p2)
    str(l1)
    assert l1.p1.x == 4.0
    assert l1.p1.y == 5.0
    assert l1.p2.x == 6.0
    assert l1.p2.y == 7.0

@mark.weight(1)
def test_line_str_ret_val():
    """Part 3. Testing that Line#__str__ returns expected value."""
    pmodule = reimport_module(POINT_MODULE)
    module = reimport_module(LINE_MODULE)
    p1 = pmodule.Point(4.0,5.0)
    p2 = pmodule.Point(6.0,7.0)
    l1 = module.Line(p1,p2)
    assert str(l1) == "(4.0, 5.0) <-> (6.0, 7.0)"



###Line#__mul__ ###
 
@mark.weight(1)
def test_line_mul_signature():
    """Part 4. Line#__mul__ signature should have self and int as parameters and return a Line."""
    module = reimport_module(LINE_MODULE)
    sig = inspect.signature(module.Line.__mul__)
    assert len(sig.parameters) == 2
    assert sig.return_annotation == 'Line'


@mark.weight(1)
def test_line_mul_mutation():
    """Part 4. Line#__mul__ should not mutate `self`."""
    pmodule = reimport_module(POINT_MODULE)
    module = reimport_module(LINE_MODULE)
    p1 = pmodule.Point(4.0,5.0)
    p2 = pmodule.Point(6.0,7.0)
    l1 = module.Line(p1,p2)
    l1 * 4
    assert l1.p1.x == 4.0
    assert l1.p1.y == 5.0
    assert l1.p2.x == 6.0
    assert l1.p2.y == 7.0
   

@mark.weight(1)
def test_line_mul():
    """Part 4. Testing that Line#__mul__ correctly creates new Point with updated x and y attributes."""
    pmodule = reimport_module(POINT_MODULE)
    module = reimport_module(LINE_MODULE)
    p1 = pmodule.Point(4.0,5.0)
    p2 = pmodule.Point(6.0,7.0)
    l1 = module.Line(p1,p2)
    l2 = l1 * 3
    assert l2.p1.x == 12.0
    assert l2.p1.y == 15.0
    assert l2.p2.x == 18.0
    assert l2.p2.y == 21.0