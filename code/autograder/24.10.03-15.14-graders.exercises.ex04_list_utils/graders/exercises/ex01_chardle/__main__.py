"""Autograder for Exercise 01 - Variables and Conditionals."""

__author__ = "Kris Jordan <kris@cs.unc.edu>"

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="exercises/ex01_chardle.py",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=81.0,
    typecheck_points=5.0,
    lint_points=4.0,
    ec_date_1="2022-01-22",
    ec_date_2="2022-01-23"
)

results = autograde.run(configuration)

print(results.to_json())
