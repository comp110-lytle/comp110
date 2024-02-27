"""Unit tests for dict_01"""

__author__ = "Kaki Ryan <kakiryan@live.unc.edu>"

from pytest import mark
from graders.helpers import assert_parameter_list, reimport_module
from graders.helpers import assert_return_type

MODULE = "exercises.ex05.dictionary"


@mark.weight(3)
def test_favorite_color_params():
    """favorite_color - favorite_color has 1 parameter of type dict[str, str]."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.favorite_color, [dict[str, str]])


@mark.weight(3)
def test_favorite_color_return_type():
    """favorite_color - favorite_color returns a str."""
    module = reimport_module(MODULE)
    assert_return_type(module.favorite_color, str)


@mark.weight(3)
def test_tie():
    """favorite_color - favorite_color returns the most frequently appearing color."""
    from exercises.ex05.dictionary import favorite_color
    tied: dict[str, str] = {"John": "purple", "Mary": "red", "Joseph": "purple", "George": "yellow"}
    assert favorite_color(tied) == "purple"
