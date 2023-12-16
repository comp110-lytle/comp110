"""Helper functions used for testing."""

__author__ = "Kaki Ryan <kakiryan@live.unc.edu>"

import importlib
import io
import re
import typing
import inspect
from types import ModuleType
from typing import Any, List
import subprocess



def import_module(module_name: str) -> ModuleType:
    """Import a module for the first time and only load it once.

    Args:
        module_name: Fully qualified name of the module being reimported.

    Returns:
        Module object."""
    return importlib.import_module(module_name)
    

def reimport_module(module_name: str) -> ModuleType:
    """Reevaluate a module if you're testing printed output at the module level. This function is likely only used
    early in the semester before functions take shape.

    Args:
        module_name: Fully qualified name of the module being reimported.

    Returns:
        Module object."""
    module = import_module(module_name)
    return importlib.reload(module)
    


def set_stdin(monkeypatch, input: List[str]) -> None:
    """Patch in lines of input to standard in."""
    io_string = io.StringIO("\n".join(input) + "\n")
    monkeypatch.setattr("sys.stdin", io_string)


def assert_out_err(capsys, expected_out: str, expected_err: str = "") -> None:
    """This is a helper function to capture and test output to stdout/stderr.

    Args:
        capsys: Built-in fixture to capture output.
        expected_out: The expected contents of stdout.
        expected_err: The expected contents of stderr.

    Returns: 
        None.
    """
    out, err = capsys.readouterr()
    assert expected_out.lower() in out.lower()
    assert expected_err.lower() in err.lower()


def author_is_a_valid_pid(module: Any) -> bool:
    """Confirm `author` is a 9-digit PID string with no spaces or dash.

    Arguments:
        module: The student's submission module.

    Returns:
        Whether author is a str and made of 9 digit characters.
    """
    passes = module.__author__ is not None
    author_format = re.compile("^[0-9]{9}$")
    passes = passes and author_format.match(module.__author__) is not None
    return passes


def mute_output(capsys) -> None:
    """Prevent stdout or stderr from being reported in Gradescope.

    Arguments:
        capsys: automatic variable in pytest.

    Returns:
        None
    """
    _out, _err = capsys.readouterr()


def assert_parameter_list(function: callable, expected: List[typing.Type]) -> None:
    """Test the type annotations of a function's parameter list."""
    sig = inspect.signature(function)
    assert len(sig.parameters) == len(expected)
    param_names = list(sig.parameters)
    for i in range(0, len(param_names)):
        name = param_names[i]
        assert sig.parameters[name].annotation == expected[i]


def assert_method_parameter_list(method: callable, expected: List[typing.Type]) -> None:
    """Methods take a first positional parameter of self. It will not have a type annotation.

    This assertion checks for a length of 1 + len(expected). It skips over the first positional
    parameter when evaluating the parameters of the method passed in as a callable.

    Arguments:
        method: A reference to the method under test (this doesn't work for plain-old functions)
        expected: List of types not including the self parameter

    Returns:
        None
    """
    sig = inspect.signature(method)
    assert len(sig.parameters) == len(expected) + 1
    param_names = list(sig.parameters)
    for i in range(1, len(param_names)):
        name = param_names[i]
        assert sig.parameters[name].annotation == expected[i - 1]


def assert_return_type(function: callable, expected: typing.Type):
    """Test the return type annotation of a function."""
    sig = inspect.signature(function)
    assert sig.return_annotation == expected


def assert_is_class(reference: any):
    """Test that a name is defined as a class."""
    assert inspect.isclass(reference)

def try_function_call(module_name, function_name, args: list):
    """TODO"""
    try:
        mod_name = import_module(module_name)
    except:
        raise AssertionError    
    
def check_for_while(module_name, fn_name, args: list, ):
    mod_name = import_module(module_name)
    