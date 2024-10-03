"""Tests for Exercise 06 - Data Wrangling."""

__author__ = "Kaki Ryan <kakiryan@cs.unc.edu>"

from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module
from graders.helpers import assert_return_type
from csv import DictReader
from random import randint


MODULE = "exercises.ex06.data_utils"
DATA_PATH = 'graders/exercises/ex06/nc_durham_2015_march_21_to_26.csv'
#DATA_PATH = '/autograder/source/graders/exercises/ex04_data/nc_durham_2015_march_21_to_26.csv'


def read_csv_rows_soln(path: str) -> list[dict[str, str]]:
    """Read a CSV file and return a list of its rows."""
    file_handle = open(path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    rows: list[dict[str, str]] = []
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows

@mark.timeout(3)
@mark.weight(0)
def test_author():
    """data_utils.py - __author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module)

@mark.timeout(3)
@mark.weight(1)
def test_head_defined():
    """data_utils.py - head function defined."""
    module = reimport_module(MODULE)
    assert callable(module.head)


@mark.timeout(3)
@mark.weight(2)
def test_head_params():
    """data_utils.py - head takes in a dict[str, list[str]] and an int."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.head, [dict[str, list[str]], int])


@mark.timeout(3)
@mark.weight(3)
def test_head_return_type():
    """data_utils.py - head returns a dict[str, list[str]]."""
    module = reimport_module(MODULE)
    assert_return_type(module.head, dict[str, list[str]])


@mark.timeout(3)
@mark.weight(8)
def test_head_1():
    """data_utils.py - head returns a dictionary with column names as keys and values empty lists when the number of rows is 0."""
    module = reimport_module(MODULE)
    expected = {'breed': ['pug', 'corgi', 'beagle'], 'color': ['brown', 'blue', 'pink'],
    'name': ['Kris', 'Kaki', 'Marc']}
    assert module.head(expected, 0) == {'breed': [], 'color': [], 'name': []}


@mark.timeout(3)
@mark.weight(8)
def test_head_2():
    """data_utils.py - head returns only 2 rows when int param is 2"""
    module = reimport_module(MODULE)
    expected = {'breed': ['pug', 'corgi', 'beagle'], 'color': ['brown', 'blue', 'pink'],
    'name': ['Kris', 'Kaki', 'Marc']}
    assert module.head(expected, 2) == {'breed': ['pug', 'corgi'], 'color': ['brown', 'blue'], 'name': ['Kris', 'Kaki']}


@mark.timeout(3)
@mark.weight(8)
def test_head_3():
    """data_utils.py - head returns entire table when int param >= the length."""
    module = reimport_module(MODULE)
    expected = {'breed': ['pug', 'corgi', 'beagle'], 'color': ['brown', 'blue', 'pink'],
    'name': ['Kris', 'Kaki', 'Marc']}
    assert module.head(expected, 5) == expected


@mark.timeout(3)
@mark.weight(1)
def test_select_defined():
    """data_utils.py - select function defined."""
    module = reimport_module(MODULE)
    assert callable(module.select)


@mark.timeout(3)
@mark.weight(2)
def test_select_params():
    """data_utils.py - select takes in a dict[str, list[str]] and a list[str]."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.select, [dict[str, list[str]], list[str]])


@mark.timeout(3)
@mark.weight(2)
def test_select_return_type():
    """data_utils.py - select returns a dict[str, list[str]]."""
    module = reimport_module(MODULE)
    assert_return_type(module.select, dict[str, list[str]])


@mark.timeout(3)
@mark.weight(10)
def test_select_1():
    """data_utils.py - select returns the correct subset of data given a list with a single element."""
    module = reimport_module(MODULE)
    expected = {'breed': ['pug', 'corgi', 'beagle'], 'color': ['brown', 'blue', 'pink'],
    'name': ['Kris', 'Kaki', 'Marc']}
    assert module.select(expected, ['breed']) == {'breed': ['pug', 'corgi', 'beagle']}


@mark.timeout(3)
@mark.weight(10)
def test_select_2():
    """data_utils.py - select returns the correct subset of data given a list with multiple elements."""
    module = reimport_module(MODULE)
    expected = {'breed': ['pug', 'corgi', 'beagle'], 'color': ['brown', 'blue', 'pink'],
    'name': ['Kris', 'Kaki', 'Marc']}
    assert module.select(expected, ['breed', 'name']) == {'breed': ['pug', 'corgi', 'beagle'], 
    'name': ['Kris', 'Kaki', 'Marc']}


@mark.timeout(3)
@mark.weight(1)
def test_concat_defined():
    """data_utils.py - concat function defined."""
    module = reimport_module(MODULE)
    assert callable(module.concat)


@mark.timeout(3)
@mark.weight(2)
def test_concat_params():
    """data_utils.py - concat takes in two dict[str, list[str]]."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.concat, [dict[str, list[str]], dict[str, list[str]]])


@mark.timeout(3)
@mark.weight(2)
def test_concat_return_type():
    """data_utils.py - concat returns a dict[str, list[str]]."""
    module = reimport_module(MODULE)
    assert_return_type(module.concat, dict[str, list[str]])


@mark.timeout(3)
@mark.weight(5)
def test_concat_1():
    """data_utils.py - concat works with duplicate keys between a and b."""
    module = reimport_module(MODULE)
    a = {'cats': ["Lily", "Macho"], 'dogs': ["Daisy"]}
    b = {"people": ["Kaki"], 'cats': ['kieto']}
    assert module.concat(a, b) == {'cats': ['Lily', 'Macho', 'kieto'], 'dogs': ['Daisy'], 'people': ['Kaki']}


@mark.timeout(3)
@mark.weight(5)
def test_concat_2():
    """data_utils.py - concat returns the correct counts with no duplicate."""
    module = reimport_module(MODULE)
    a = {'cats': ["Lily", "Macho"], 'dogs': ["Daisy"]}
    b = {"people": ["Kaki", "Kris"], 'cars': ['kieto']}
    assert module.concat(a, b) == {'cats': ['Lily', 'Macho'], 'dogs': ['Daisy'], 'people': ['Kaki', "Kris"], 'cars': ["kieto"]}


