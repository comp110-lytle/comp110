"""Tests for the double project."""

__author__ = "Kris Jordan <kris@cs.unc.edu>"

from pytest import mark


@mark.weight(1)
def test_double():
    """Basic test case for double."""
    from setup.failing import double
    assert double(2) == 4
