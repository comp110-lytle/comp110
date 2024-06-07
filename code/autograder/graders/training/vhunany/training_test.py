"""Unit tests for remove_repeats."""

__author__ = "Viktorya Hunanyan vhunany@unc.edu"

from pytest import mark

   
def test_one_check_for_return_value():
    """Empty input list to check that the function has expected return value None."""
    from training.vhunany import remove_repeats
    assert remove_repeats([]) == None


@mark.weight(2) 
def test_two_check_for_correct_mutation_for_list_with_repeats():
    """Test for correct mutation of an input that has both sequentional repeated values and non-sequential repeated values."""
    from training.vhunany import remove_repeats
    a: list[int] = [4, 8, 9, 4, 2, 2, 0, 9, 7, 10]
    remove_repeats(a)
    assert a == [4, 8, 9, 2, 0, 7, 10]


def test_two_check_for_correct_mutation_for_list_with_no_repeats():
    """Test for correct mutation of an input that has no repeated values."""
    from training.vhunany import remove_repeats
    a: list[int] = [4, 8, 9, -1, 2, -2, 0, 19, 7, 10]
    remove_repeats(a)
    assert a == [4, 8, 9, -1, 2, -2, 0, 19, 7, 10]


