"""Tests for Exercise 07: Runtime Analysis."""

__author__ = "Vrinda Desai <vrinda@email.unc.edu>"

from pytest import mark

MODULE = "exercises.ex07.sort_functions"


@mark.weight(10)
def test_selection_sort_1():
    """selection_sort - selection_sort correctly sorts a list."""
    from exercises.ex07.sort_functions import selection_sort
    lista: list = [10, 9, 8, 7, 1, 2, 3, 4]
    selection_sort(lista)
    assert lista == [1, 2, 3, 4, 7, 8, 9, 10]


@mark.weight(10)
def test_selection_sort_2():
    """selection_sort - selection_sort correctly sorts a list with negatives."""
    from exercises.ex07.sort_functions import selection_sort
    lista: list = [-98, -100, -1000, -1, -33, -67]
    selection_sort(lista)
    assert lista == [-1000, -100, -98, -67, -33, -1]


@mark.weight(10)
def test_selection_sort_3():
    """selection_sort - selection_sort correctly sorts a list with duplicates."""
    from exercises.ex07.sort_functions import selection_sort
    lista: list = [1, 3, 1, 3, 1, 3]
    selection_sort(lista)
    assert lista == [1, 1, 1, 3, 3, 3]


@mark.weight(10)
def test_insertion_sort_1():
    """insertion_sort - insertion_sort correctly sorts a list."""
    from exercises.ex07.sort_functions import insertion_sort
    lista: list = [10, 9, 8, 7, 1, 2, 3, 4]
    insertion_sort(lista)
    assert lista == [1, 2, 3, 4, 7, 8, 9, 10]


@mark.weight(10)
def test_insertion_sort_2():
    """insertion_sort - insertion_sort correctly sorts a list with negatives."""
    from exercises.ex07.sort_functions import insertion_sort
    lista: list = [-98, -100, -1000, -1, -33, -67]
    insertion_sort(lista)
    assert lista == [-1000, -100, -98, -67, -33, -1]
    

@mark.weight(10)
def test_insertion_sort_3():
    """insertion_sort - insertion_sort correctly sorts a list with duplicates."""
    from exercises.ex07.sort_functions import insertion_sort
    lista: list = [1, 3, 1, 3, 1, 3]
    insertion_sort(lista)
    assert lista == [1, 1, 1, 3, 3, 3]
