import re
import importlib
from pytest import mark
from graders.helpers import author_is_a_valid_pid, mute_output, set_stdin, import_module, reimport_module
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture
from typing import Any
import inspect
import types
from lessons.practice.courses import Course

MODULE = "lessons.practice.courses"


def _construct_course(name: str, level: int, prereqs: list[str]) -> Course:
    c: Course = Course()
    c.name = name
    c.level = level
    c.prerequisites = prereqs
    return c

@mark.weight(1)
def test_find_course():
    """find_courses should take 2 parameters: list[Course] and str and return list[str]"""
    module = import_module(MODULE)
    sig = inspect.signature(module.find_courses)
    assert len(sig.parameters) == 2
    param_names = list(sig.parameters)
    vals = param_names[0]
    assert sig.parameters[vals].annotation == list[Course]
    vals2 = param_names[1]
    assert sig.parameters[vals2].annotation == str
    assert sig.return_annotation == list[str]

@mark.weight(1)
def test_find_course_functionality1():
    """Testing find_courses basic use case"""
    module = import_module(MODULE)
    course_list: list[Course] = []
    course_list.append(_construct_course("Intro to CS", 110, ["Calculus"]))
    course_list.append(_construct_course("Intro to Data Structures", 210, ["Calculus", "Intro to CS"]))
    course_list.append(_construct_course("Special Topic", 590, ["Intro to CS", "Data Structures", "Calculus"]))
    try:
        assert module.find_courses(course_list, "Calculus") == ["Special Topic"]
    except:
        assert False
        
@mark.weight(1)
def test_find_course_functionality2():
    """Testing find_courses edge case: returning an empty list"""
    module = import_module(MODULE)
    course_list: list[Course] = []
    course_list.append(_construct_course("Intro to CS", 110, ["Calculus"]))
    course_list.append(_construct_course("Intro to Data Structures", 210, ["Calculus", "Intro to CS"]))
    course_list.append(_construct_course("Special Topic", 590, ["Intro to CS", "Data Structures", "Calculus"]))
    try:
        assert module.find_courses(course_list, "Trig") == []
    except:
        assert False
        
@mark.weight(1)
def test_is_valid_course():
    """is_valid_course should take 2 parameters: self and str and return bool"""
    module = import_module(MODULE)
    sig = inspect.signature(module.Course.is_valid_course)
    assert len(sig.parameters) == 2
    param_names = list(sig.parameters)
    vals = param_names[1]
    assert sig.parameters[vals].annotation == str
    assert sig.return_annotation == bool

@mark.weight(1)
def test_is_valid_course_functionality1():
    """Testing is_valid_course use case where the course is valid"""
    course = _construct_course("Special Topic", 590, ["Intro to CS", "Data Structures", "Calculus"])
    try:
        assert course.is_valid_course("Calculus") == True
    except:
        assert False
        
@mark.weight(1)
def test_is_valid_course_functionality2():
    """Testing is_valid_course use case where there course is not valid"""
    course = _construct_course("Special Topic", 590, ["Intro to CS", "Data Structures", "Calculus"])
    try:
        assert course.is_valid_course("Trig") == False
    except:
        assert False