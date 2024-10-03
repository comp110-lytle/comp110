"""Tests for Exercise 07: Dict Functions + Unit Tests."""

__author__ = "Vrinda Desai <vrinda@email.unc.edu>"

from pytest import mark
from graders.helpers import assert_parameter_list, reimport_module
from graders.helpers import assert_return_type


MODULE = "ex05.dictionary"


@mark.weight(4)
def test_update_attendance_1():
    """update_attendance - update_attendance does not repeat the same name within a day."""
    from ex05.dictionary import update_attendance
    log = {"Monday": ["Anna"]}
    update_attendance(log, "Monday", "Anna")
    update_attendance(log, "Tuesday", "Anna")
    update_attendance(log, "Tuesday", "Anna")
    assert log == {"Monday": ["Anna"], "Tuesday": ["Anna"]}


@mark.weight(4)
def test_update_attendance_2():
    """update_attendance - update_attendance correctly mutates the passed in dictionary."""
    from ex05.dictionary import update_attendance
    log = {}
    update_attendance(log, "Monday", "Kam")
    update_attendance(log, "Tuesday", "Kaleb")
    assert log == {"Monday": ["Kam"], "Tuesday": ["Kaleb"]}
