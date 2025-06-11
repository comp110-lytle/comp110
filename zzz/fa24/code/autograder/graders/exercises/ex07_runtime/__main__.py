"""Autograder for Exercise 07."""

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="exercises/ex07",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=100.0,
    typecheck_points=0.0,
    lint_points=0.0,
    ec_date_1="2022-10-10",
    ec_date_2="2022-10-11"
)

results = autograde.run(configuration)

print(results.to_json())
