"""Autograder for Exercise 00 -  Hello World."""

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="exercises/ex01_tea_party.py",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=90.0,
    typecheck_points=10.0,
    lint_points=0.0,
    ec_date_1="2024-01-27",
    ec_date_2="2024-01-28"
)

results = autograde.run(configuration)

print(results.to_json())
