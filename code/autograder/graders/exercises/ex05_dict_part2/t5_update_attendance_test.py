"""Tests for Exercise 05: Dict Functions + Unit Tests."""

__author__ = "Vrinda Desai <vrinda@email.unc.edu>"

from pytest import mark
from graders.helpers import assert_parameter_list, reimport_module
from graders.helpers import assert_return_type


MODULE = "exercises.ex04.dictionary"


@mark.weight(4)
def test_update_attendance_1():
    """update_attendance - update_attendance does not repeat the same name within a day."""
    from exercises.ex04.dictionary import update_attendance
    log = {"Monday": ["Anna"]}
    update_attendance(log, "Monday", "Anna")
    update_attendance(log, "Tuesday", "Anna")
    update_attendance(log, "Tuesday", "Anna")
    assert log == {"Monday": ["Anna"], "Tuesday": ["Anna"]}


@mark.weight(4)
def test_update_attendance_2():
    """update_attendance - update_attendance correctly mutates the passed in dictionary."""
    from exercises.ex04.dictionary import update_attendance
    log = {}
    update_attendance(log, "Monday", "Kam")
    update_attendance(log, "Tuesday", "Kaleb")
    assert log == {"Monday": ["Kam"], "Tuesday": ["Kaleb"]}


@mark.weight(1)
def test_update_attendance_empty():
    """update_attendance - correctly handles an empty dictionary."""
    from exercises.ex04.dictionary import update_attendance
    log = {}
    update_attendance(log, "Monday", "John")
    assert log == {"Monday": ["John"]}


@mark.weight(2)
def test_update_attendance_multiple_students():
    """update_attendance - correctly adds multiple students on the same day."""
    from exercises.ex04.dictionary import update_attendance
    log = {"Monday": ["John"]}
    update_attendance(log, "Monday", "Alice")
    update_attendance(log, "Monday", "Bob")
    assert log == {"Monday": ["John", "Alice", "Bob"]}


@mark.weight(1)
def test_update_attendance_same_student_different_days():
    """update_attendance - allows the same student on different days."""
    from exercises.ex04.dictionary import update_attendance
    log = {"Monday": ["John"]}
    update_attendance(log, "Tuesday", "John")
    assert log == {"Monday": ["John"], "Tuesday": ["John"]}

