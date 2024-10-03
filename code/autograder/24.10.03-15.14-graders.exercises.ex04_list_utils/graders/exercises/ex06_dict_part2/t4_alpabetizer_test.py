"""Tests for Exercise 07: Dict Functions + Unit Tests."""

__author__ = "Vrinda Desai <vrinda@email.unc.edu>"

from pytest import mark
from graders.helpers import assert_parameter_list, reimport_module
from graders.helpers import assert_return_type


MODULE = "ex05.dictionary"


@mark.weight(4)
def test_alphabetizer_1():
    """alphabetizer - alphabetizer correctly returns a dictionary of sorted words."""
    from ex05.dictionary import alphabetizer
    words = ["apple", "all"]
    assert alphabetizer(words) == {"a": ["apple", "all"]}


@mark.weight(4)
def test_alphabetizer_2():
    """alphabetizer - alphabetizer is correct when sorting words of different cases."""
    from ex05.dictionary import alphabetizer
    words = ["jogging", "sleep", "Jolly", "Circus", "citrus"]
    assert alphabetizer(words) == {"j": ["jogging", "Jolly"], "s": ["sleep"], "c": ["Circus", "citrus"]}
