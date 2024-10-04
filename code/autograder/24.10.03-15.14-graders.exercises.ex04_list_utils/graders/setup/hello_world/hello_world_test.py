"""Tests for the hello world project."""

__author__ = "Kris Jordan <kris@cs.unc.edu>"

import io
import re
import sys
from pytest import mark
from subprocess import run

PYTHON = sys.executable


@mark.weight(20)
def test_author(monkeypatch, capsys):
    """__author__ global variable is present and correct format."""
    monkeypatch.setattr('sys.stdin', io.StringIO("Kris"))
    from setup.hello_world import __author__
    author_format = re.compile("(.+) *<(.+@.+)>")
    assert author_format.match(__author__) is not None
    _out, _err = capsys.readouterr()  # This prevents stdout from reporting.


@mark.weight(50)
def test_integration(capsys):
    """Prints 'Hello, world.'."""
    result = run(
        [PYTHON, "-m", "setup.hello_world"],
        capture_output=True
    )
    assert "Hello, world." in str(result.stdout, "utf-8")
