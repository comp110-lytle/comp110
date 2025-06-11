"""Autograder for Exercise 00 -  Hello World."""

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="exercises/ex00_hello_world.py",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=70.0,
    typecheck_points=30.0,
    lint_points=0.0,
    ec_date_1="2024-01-17",
    ec_date_2="2024-01-18"
)

results = autograde.run(configuration)

print(results.to_json())
