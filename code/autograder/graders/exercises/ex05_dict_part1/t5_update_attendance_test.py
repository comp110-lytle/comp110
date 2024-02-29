"""Tests for Dict Utils Part 1."""

__author__ = "Vrinda Desai <vrinda@email.unc.edu>"

from pytest import mark
from graders.helpers import assert_parameter_list, reimport_module
from graders.helpers import assert_return_type


MODULE = "exercises.ex05.dictionary"


@mark.weight(3)
def test_update_attendance_params():
    """update_attendance - update_attendance takes in a dict[str, list[str]], str, str."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.update_attendance, [dict[str, list[str]], str, str])


@mark.weight(3)
def test_update_attendance_return_type():
    """update_attendance - update_attendance returns None."""
    module = reimport_module(MODULE)
    assert_return_type(module.update_attendance, None)


@mark.weight(3)
def test_update_attendance_1():
    """update_attendance - update_attendance correctly mutates the passed in dictionary."""
    from exercises.ex05.dictionary import update_attendance
    log = {"Wednesday": ["Jane", "Mary"], "Thursday": ["Daisy"]}
    update_attendance(log, "Thursday", "Jane")
    update_attendance(log, "Friday", "Jane")
    assert log == {"Wednesday": ["Jane", "Mary"], "Thursday": ["Daisy", "Jane"], "Friday": ["Jane"]}
