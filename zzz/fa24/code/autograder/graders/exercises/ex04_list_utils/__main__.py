"""Autograder for Exercise 04."""

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="exercises/ex04_utils.py",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=80.0,
    typecheck_points=20.0,
    lint_points=0.0,
    ec_date_1="2022-09-17",
    ec_date_2="2022-09-18",
)

results = autograde.run(configuration)

print(results.to_json())
