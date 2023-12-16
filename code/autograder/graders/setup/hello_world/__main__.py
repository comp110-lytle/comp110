"""Autograder for comp110.example."""

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="setup/hello_world.py",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=70.0,
    typecheck_points=15.0,
    lint_points=15.0
)

results = autograde.run(configuration)

print(results.to_json())
