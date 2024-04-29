"""Autograder for Exercise 09 - Linked List Utils."""

__author__ = "Kaki Ryan <kakiryan@cs.unc.edu>, Kris Jordan <kris@cs.unc.edu>"

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="exercises/ex10",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=95.0,
    typecheck_points=3.0,
    lint_points=2.0,
    ec_date_1="2022-04-25",
    ec_date_2="2022-04-26"
)

results = autograde.run(configuration)

print(results.to_json())