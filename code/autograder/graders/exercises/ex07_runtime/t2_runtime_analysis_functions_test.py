"""Tests for Exercise 07: Runtime Analysis."""

__author__ = "Vrinda Desai <vrinda@email.unc.edu>"

from pytest import mark

MODULE = "exercises.ex07.runtime_analysis_functions"


@mark.weight(10)
def test_random_descending_list_1():
    """random_descending_list - random_descending_list correctly generates an n-length list."""
    from exercises.ex07.runtime_analysis_functions import random_descending_list
    assert len(random_descending_list(50)) == 50

@mark.weight(10)
def test_random_descending_list_2():
    """random_descending_list - random_descending_list correctly generates an n-length list."""
    from exercises.ex07.runtime_analysis_functions import random_descending_list
    assert len(random_descending_list(37)) == 37

@mark.weight(10)
def test_random_descending_list_3():
    """random_descending_list - random_descending_list correctly generates a descending list."""
    from exercises.ex07.runtime_analysis_functions import random_descending_list
    generated: list = random_descending_list(10)
    i: int = 0
    while i < len(generated) - 1:
        assert generated[i] >= generated[i+1]
        i += 1

@mark.weight(10)
def test_random_descending_list_4():
    """random_descending_list - random_descending_list correctly generates a descending list."""
    from exercises.ex07.runtime_analysis_functions import random_descending_list
    generated: list = random_descending_list(20)
    i: int = 0
    while i < len(generated) - 1:
        assert generated[i] >= generated[i+1]
        i += 1