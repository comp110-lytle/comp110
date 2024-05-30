"""Autograder for Exercise 03 - Structured Battleship."""

__author__ = "Vrinda Desai <vrinda@email.unc.edu>"

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="ex03_functional_battleship.py",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=90.0,
    typecheck_points=5.0,
    lint_points=5.0,
    ec_date_1="2022-02-05",
    ec_date_2="2022-02-06"
)

results = autograde.run(configuration)

print(results.to_json())
