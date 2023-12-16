"""Autograder for Exercise 03 - Structured Wordle."""

__author__ = "Kris Jordan <kris@cs.unc.edu>"

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="exercises/",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=72.0,
    typecheck_points=4.0,
    lint_points=4.0,
    ec_date_1="2022-02-05",
    ec_date_2="2022-02-06"
)

results = autograde.run(configuration)

print(results.to_json())
