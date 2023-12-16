"""Unit tests for dict_01"""

__author__ = "Kaki Ryan <kakiryan@live.unc.edu>"

from pytest import mark
from graders.helpers import assert_parameter_list, reimport_module
from graders.helpers import assert_return_type

MODULE = "exercises.ex05.dictionary"


@mark.weight(6)
def test_favorite_color_params():
    """favorite_color.py - favorite_color has 1 parameter of type dict[str,str]."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.favorite_color, [dict[str, str]])


@mark.weight(6)
def test_favorite_color_return_type():
    """favorite_color.py - favorite_color returns a str."""
    module = reimport_module(MODULE)
    assert_return_type(module.favorite_color, str)


@mark.weight(6)
def test_all_same():
    """Everyone has the same favorite color."""
    from exercises.ex05.dictionary import favorite_color
    all_same: dict[str, str] = {"John": "blue", "Mary": "blue", "Joseph": "blue"}
    assert favorite_color(all_same) == "blue"


@mark.weight(6)
def test_tie():
    """There is a tie for the best color."""
    from exercises.ex05.dictionary import favorite_color
    tied: dict[str, str] = {"John": "purple", "Mary": "red", "Joseph": "purple", "George": "red"}
    assert favorite_color(tied) == "purple"


@mark.weight(6)
def test_one_max():
    """Correctly finds the most frequently favorite color."""
    from exercises.ex05.dictionary import favorite_color
    yellow_wins: dict[str, str] = {"John": "green", "Mary": "red", "Joseph": "yellow", "George": "yellow"}
    assert favorite_color(yellow_wins) == "yellow"