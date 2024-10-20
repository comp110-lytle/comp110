"""Tests for Exercise 07: Dict Functions + Unit Tests."""

__author__ = "Kaki Ryan <kakiryan@live.unc.edu>"
__author__ = "Viktorya Hunanyan <vhunany@unc.edu>"


from pytest import mark
from graders.helpers import assert_parameter_list, reimport_module
from graders.helpers import assert_return_type

MODULE = "exercises.ex06.dictionary"

@mark.weight(2)
def test_favorite_color_params():
    """favorite_color - favorite_color has 1 parameter of type dict[str, str]."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.favorite_color, [dict[str, str]])


@mark.weight(2)
def test_favorite_color_return_type():
    """favorite_color - favorite_color returns a str."""
    module = reimport_module(MODULE)
    assert_return_type(module.favorite_color, str)


@mark.weight(2)
def test_tie():
    """favorite_color - favorite_color returns the most frequently appearing color."""
    module = reimport_module(MODULE)
    tied: dict[str, str] = {"John": "purple", "Mary": "red", "Joseph": "purple", "George": "yellow"}
    assert module.favorite_color(tied) == "purple"

@mark.weight(2)
def test_favorite_color_all_same():
    """favorite_color - favorite_color is correct when everyone has the same favorite color."""
    module = reimport_module(MODULE)
    all_same: dict[str, str] = {"John": "blue", "Mary": "blue", "Joseph": "blue"}
    assert module.favorite_color(all_same) == "blue"


@mark.weight(2)
def test_favorite_color_tie():
    """favorite_color - favorite_color is correct when there is a tie for the best color."""
    module = reimport_module(MODULE)
    tied: dict[str, str] = {"John": "purple", "Mary": "red", "Joseph": "purple", "George": "red"}
    assert module.favorite_color(tied) == "purple"


@mark.weight(2)
def test_favorite_color_one_max():
    """favorite_color - favorite_color returns the most frequently found color."""
    module = reimport_module(MODULE)
    yellow_wins: dict[str, str] = {"John": "green", "Mary": "red", "Joseph": "yellow", "George": "yellow"}
    assert module.favorite_color(yellow_wins) == "yellow"

@mark.weight(2)
def test_favorite_color_empty():
    """favorite_color - handles an empty dictionary."""
    module = reimport_module(MODULE)
    assert module.favorite_color({}) == ""

@mark.weight(2)
def test_favorite_color_empty():
    """favorite_color - handles an empty dictionary."""
    module = reimport_module(MODULE)
    assert module.favorite_color({}) == ""