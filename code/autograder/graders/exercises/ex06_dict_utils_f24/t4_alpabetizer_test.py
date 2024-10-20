"""Tests for Dict Utils Part 1."""

__author__ = "Vrinda Desai <vrinda@email.unc.edu>"
__author__ = "Viktorya Hunanyan <vhunany@unc.edu>"

from pytest import mark
from graders.helpers import assert_parameter_list, reimport_module
from graders.helpers import assert_return_type


MODULE = "exercises.ex06.dictionary"

@mark.weight(3)
def test_alphabetizer_params():
    """alphabetizer - alphabetizer takes in a list[str]."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.alphabetizer, [list[str]])


@mark.weight(3)
def test_alphabetizer_return_type():
    """alphabetizer - alphabetizer returns a dict[str, list[str]]."""
    module = reimport_module(MODULE)
    assert_return_type(module.alphabetizer, dict[str, list[str]])


@mark.weight(3)
def test_alphabetizer_1():
    """alphabetizer - alphabetizer correctly returns a dictionary of sorted words."""
    module = reimport_module(MODULE)
    words = ["cherry", "hello", "mine", "hot", "marshmallow", "crayola"]
    assert module.alphabetizer(words) == {"c": ["cherry", "crayola"], "h": ["hello", "hot"], "m": ["mine", "marshmallow"]}

@mark.weight(4)
def test_alphabetizer_1():
    """alphabetizer - alphabetizer correctly returns a dictionary of sorted words."""
    module = reimport_module(MODULE)
    words = ["apple", "all"]
    assert module.alphabetizer(words) == {"a": ["apple", "all"]}


@mark.weight(1)
def test_alphabetizer_empty():
    """alphabetizer - handles an empty list correctly."""
    module = reimport_module(MODULE)
    assert module.alphabetizer([]) == {}

@mark.weight(2)
def test_alphabetizer_same_letter():
    """alphabetizer - groups words starting with the same letter correctly."""
    module = reimport_module(MODULE)
    words = ["cat", "car", "can"]
    assert module.alphabetizer(words) == {"c": ["cat", "car", "can"]}

