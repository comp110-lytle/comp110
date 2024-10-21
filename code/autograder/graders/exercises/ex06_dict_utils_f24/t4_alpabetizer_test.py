"""Tests for Dict Utils Part 1."""

__author__ = "Vrinda Desai <vrinda@email.unc.edu>"
__author__ = "Viktorya Hunanyan <vhunany@unc.edu>"

from pytest import mark
from graders.helpers import assert_parameter_list, reimport_module
from graders.helpers import assert_return_type


MODULE = "exercises.ex06.dictionary"

@mark.weight(5)
def test_alphabetizer_params():
    """alphabetizer - alphabetizer takes in a list[str]."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.alphabetizer, [list[str]])

@mark.weight(5)
def test_alphabetizer_return_type():
    """alphabetizer - returns a dict[str, list[str]]."""
    module = reimport_module(MODULE)
    assert_return_type(module.alphabetizer, dict[str, list[str]])

@mark.weight(5)
def test_alphabetizer_correct():
    """alphabetizer - correctly returns a dictionary of sorted words."""
    module = reimport_module(MODULE)
    words = ["cherry", "hello", "mine", "hot", "marshmallow", "crayola"]
    assert module.alphabetizer(words) == {"c": ["cherry", "crayola"], "h": ["hello", "hot"], "m": ["mine", "marshmallow"]}