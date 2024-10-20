"""Tests for Dict Utils Part 1."""

__author__ = "Vrinda Desai <vrinda@email.unc.edu>"
__author__ = "Viktorya Hunanyan <vhunany@unc.edu>"


from pytest import mark
from graders.helpers import assert_parameter_list, reimport_module
from graders.helpers import assert_return_type


MODULE = "exercises.ex06.dictionary"

@mark.weight(1)
def test_update_attendance_params():
    """update_attendance - update_attendance takes in a dict[str, list[str]], str, str."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.update_attendance, [dict[str, list[str]], str, str])


@mark.weight(1)
def test_update_attendance_return_type():
    """update_attendance - update_attendance returns None."""
    module = reimport_module(MODULE)
    assert_return_type(module.update_attendance, None)


@mark.weight(2)
def test_update_attendance_1():
    """update_attendance - update_attendance correctly mutates the passed in dictionary."""
    module = reimport_module(MODULE)
    log = {"Wednesday": ["Jane", "Mary"], "Thursday": ["Daisy"]}
    module.update_attendance(log, "Thursday", "Jane")
    module.update_attendance(log, "Friday", "Jane")
    assert log == {"Wednesday": ["Jane", "Mary"], "Thursday": ["Daisy", "Jane"], "Friday": ["Jane"]}

@mark.weight(3)
def test_update_attendance_1():
    """update_attendance - update_attendance does not repeat the same name within a day."""
    module = reimport_module(MODULE)
    log = {"Monday": ["Anna"]}
    module.update_attendance(log, "Monday", "Anna")
    module.update_attendance(log, "Tuesday", "Anna")
    module.update_attendance(log, "Tuesday", "Anna")
    assert log == {"Monday": ["Anna"], "Tuesday": ["Anna"]}


@mark.weight(3)
def test_update_attendance_2():
    """update_attendance - update_attendance correctly mutates the passed in dictionary."""
    module = reimport_module(MODULE)
    log = {}
    module.update_attendance(log, "Monday", "Kam")
    module.update_attendance(log, "Tuesday", "Kaleb")
    assert log == {"Monday": ["Kam"], "Tuesday": ["Kaleb"]}


@mark.weight(5)
def test_update_attendance_empty():
    """update_attendance - correctly handles an empty dictionary."""
    module = reimport_module(MODULE)
    log = {}
    module.update_attendance(log, "Monday", "John")
    assert log == {"Monday": ["John"]}


@mark.weight(5)
def test_update_attendance_same_student_different_days():
    """update_attendance - allows the same student on different days."""
    module = reimport_module(MODULE)
    log = {"Monday": ["John"]}
    module.update_attendance(log, "Tuesday", "John")
    assert log == {"Monday": ["John"], "Tuesday": ["John"]}