"""Autograder for Exercise 06 -  Data Wrangling."""

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="exercises/ex06",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=70.0,
    typecheck_points=10.0,
    lint_points=10.0,
    ec_date_1="2022-10-24",
    ec_date_2="2022-10-25"
)

results = autograde.run(configuration)

print(results.to_json())