"""Autograder for Exercise 07 -  Simpy."""

__author__ = "Kaki Ryan <kakiryan@cs.unc.edu>"

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="exercises/ex09",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=80.0,
    typecheck_points=0.0,
    lint_points=10.0,
    ec_date_1="2022-04-10",
    ec_date_2="2022-04-11"
)

results = autograde.run(configuration)

print(results.to_json())