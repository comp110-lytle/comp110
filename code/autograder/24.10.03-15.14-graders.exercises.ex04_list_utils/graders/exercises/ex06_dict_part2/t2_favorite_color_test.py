"""Tests for Exercise 07: Dict Functions + Unit Tests."""

__author__ = "Kaki Ryan <kakiryan@live.unc.edu>"

from pytest import mark
from graders.helpers import assert_parameter_list, reimport_module
from graders.helpers import assert_return_type

MODULE = "ex05.dictionary"


@mark.weight(3)
def test_favorite_color_all_same():
    """favorite_color - favorite_color is correct when everyone has the same favorite color."""
    from ex05.dictionary import favorite_color
    all_same: dict[str, str] = {"John": "blue", "Mary": "blue", "Joseph": "blue"}
    assert favorite_color(all_same) == "blue"


@mark.weight(3)
def test_favorite_color_tie():
    """favorite_color - favorite_color is correct when there is a tie for the best color."""
    from ex05.dictionary import favorite_color
    tied: dict[str, str] = {"John": "purple", "Mary": "red", "Joseph": "purple", "George": "red"}
    assert favorite_color(tied) == "purple"


@mark.weight(2)
def test_favorite_color_one_max():
    """favorite_color - favorite_color returns the most frequently found color."""
    from ex05.dictionary import favorite_color
    yellow_wins: dict[str, str] = {"John": "green", "Mary": "red", "Joseph": "yellow", "George": "yellow"}
    assert favorite_color(yellow_wins) == "yellow"
