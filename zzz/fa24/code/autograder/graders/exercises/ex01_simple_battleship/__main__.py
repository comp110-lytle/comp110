"""Autograder for Exercise 01 - Simple Battleship"""

__author__ = "Alyssa Lytle <abyrnes1@cs.unc.edu>"

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="ex01_simple_battleship.py",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=80.0,
    typecheck_points=10.0,
    lint_points=0.0,
    ec_date_1="2022-01-22",
    ec_date_2="2022-01-23"
)

results = autograde.run(configuration)

print(results.to_json())
