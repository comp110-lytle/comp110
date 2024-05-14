"""Practice Autograder for EX00 (23F)."""

__author__ = "Vrinda Desai <vrinda@email.unc.edu>"

# This autograder follows much of the autograder already created by Kris Jordan. 
# This autograder is only for training purposes.

import re
import importlib
from pytest import mark


def _reimport_module() -> None:
    """Checking module output (rather than individual functions)."""
    import ex00_hello_world
    importlib.reload(ex00_hello_world)


@mark.weight(20)
def test_author(capsys):
    """Checking author var."""
    from ex00_hello_world import __author__
    author_format = re.compile("[0-9]{9}$")  # regex for expecting a 9 digit PID
    assert author_format.match(__author__) is not None
    _out, _err = capsys.readouterr() 


@mark.weight(25)
def test_hello(capsys):
    """Checking for hello."""
    _reimport_module()
    out, _err = capsys.readouterr()
    assert "hello" in str(out).lower()  # checking if hello is in the output


@mark.weight(25)
def test_world(capsys):
    """Checking for world."""
    _reimport_module()
    out, _err = capsys.readouterr()
    assert "world" in str(out).lower()  # same as above 
