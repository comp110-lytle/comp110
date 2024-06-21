"""Autograder for River Simulation."""

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="ex06",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=80.0,
    typecheck_points=10.0,
    lint_points=10.0
)

results = autograde.run(configuration)

print(results.to_json())
