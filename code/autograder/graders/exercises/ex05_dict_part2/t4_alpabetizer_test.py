"""Tests for Exercise 05: Dict Functions + Unit Tests."""

__author__ = "Vrinda Desai <vrinda@email.unc.edu>"

from pytest import mark
from graders.helpers import assert_parameter_list, reimport_module
from graders.helpers import assert_return_type


MODULE = "exercises.ex04.dictionary"


@mark.weight(4)
def test_alphabetizer_1():
    """alphabetizer - alphabetizer correctly returns a dictionary of sorted words."""
    from exercises.ex04.dictionary import alphabetizer
    words = ["apple", "all"]
    assert alphabetizer(words) == {"a": ["apple", "all"]}


@mark.weight(4)
def test_alphabetizer_2():
    """alphabetizer - alphabetizer is correct when sorting words of different cases."""
    from exercises.ex04.dictionary import alphabetizer
    words = ["jogging", "sleep", "Jolly", "Circus", "citrus"]
    assert alphabetizer(words) == {"j": ["jogging", "Jolly"], "s": ["sleep"], "c": ["Circus", "citrus"]}

@mark.weight(1)
def test_alphabetizer_empty():
    """alphabetizer - handles an empty list correctly."""
    from exercises.ex04.dictionary import alphabetizer
    assert alphabetizer([]) == {}

@mark.weight(2)
def test_alphabetizer_same_letter():
    """alphabetizer - groups words starting with the same letter correctly."""
    from exercises.ex04.dictionary import alphabetizer
    words = ["cat", "car", "can"]
    assert alphabetizer(words) == {"c": ["cat", "car", "can"]}

@mark.weight(1)
def test_alphabetizer_special_characters():
    """alphabetizer - handles special characters correctly."""
    from exercises.ex04.dictionary import alphabetizer
    words = ["#hashtag", "123number", "apple"]
    assert alphabetizer(words) == {"a": ["apple"]}
