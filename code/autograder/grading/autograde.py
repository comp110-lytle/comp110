"""Gradescope based autograder.

Environment Variables:
    GRADING_SUBMISSION_ROOT: specify the root of student submission
    GRADING_GRADER_ROOT: specify the root of autograder
"""

import json
from os import environ, path
from .lint import lint
from .pytest import pytest
from .typecheck import typecheck
from .formats import GradescopeResults, GradescopeVisibility

SUBMISSION_METADATA: str = "/autograder/submission_metadata.json"


class Configuration:
    """Data object to represent configuration settings of the autograding tool suite."""
    pytest_points: float
    typecheck_points: float
    lint_points: float
    src_root: str
    src_path: str
    test_root: str
    test_path: str
    ec_date_1: str
    ec_multiplier_1: float
    ec_date_2: str
    ec_multiplier_2: float

    def __init__(
            self,
            src_path: str,
            test_path: str = "",
            pytest_points: float = 0.0,
            typecheck_points: float = 0.0,
            lint_points: float = 0.0,
            src_root: str = None,
            test_root: str = None, 
            ec_date_1: str = "2020-10-19",
            ec_multiplier_1: float = 1.05,
            ec_date_2: str = "2020-10-21",
            ec_multiplier_2: float = 1.03
    ):
        """Construct a fully configured autograder configuration.

        Args:
            pytest_points: Weight of Pytest Unit Tests. Test results will be scaled to this total.
                0 to disable Pytest.
            typecheck_points: Weight of mypy strict check. Each error will deduct 1 point from this total.
                0 to disable type checking.
            lint_points: Weight of Flake8 linting. Each error will deduct 1 point from this total.
                0 to disable Flake8 linting.
            src_path: Path to subdirectory or file containing the source code under assessment.
            test_path: Path to subdirectory containing the pytest tests.
            src_root: Root directory of where the modules of the source code under assessment are stored.
            test_root: Root directory of where the modules of the pytest unit tests are stored.
            ec_date_1: Date 48 hours before due date.
            ec_multiplier_1: Score multiplier for 48 hr early. Default to 1.05.
            ec_date_2: Date 24 hours before due date.
            ec_multiplier_2: Score multiplier for 24 hr early. Default to 1.03.
        """
        self.pytest_points = pytest_points
        """Weight of Pytest Unit Tests. Test results will be scaled to this total. 0 to disable Pytest."""

        self.typecheck_points = typecheck_points
        """Weight of mypy strict check. Each error will deduct 1 point from this total. 0 to disable type checking."""

        self.lint_points = lint_points
        """Weight of Flake8 linting. Each error will deduct 1 point from this total. 0 to disable Flake8 linting."""

        if src_root is None:
            if "GRADING_SUBMISSION_ROOT" in environ:
                src_root = environ["GRADING_SUBMISSION_ROOT"]
            else:
                src_root = "."
        self.src_root = path.abspath(src_root)
        """Root directory of where the modules of the source code under assessment are stored."""

        self.src_path = src_path
        """Path to subdirectory or file containing the source code under assessment."""

        if test_root is None:
            if "GRADING_GRADER_ROOT" in environ:
                test_root = environ["GRADING_GRADER_ROOT"]
            else:
                test_root = "."
        self.test_root = path.abspath(test_root)
        """Root directory of where the modules of the pytest unit tests are stored."""

        self.test_path = test_path
        """Path to subdirectory containing the pytest tests."""

        self.ec_date_1 = ec_date_1
        """Set 48 hr extra credit date."""

        self.ec_multiplier_1 = ec_multiplier_1
        """Set 48 hr extra credit multiplier."""

        self.ec_date_2 = ec_date_2
        """Set 24 hr extra credit date."""

        self.ec_multiplier_2 = ec_multiplier_2
        """Set 24 hr extra credit multiplier."""


def run(conf: Configuration) -> GradescopeResults:
    """Run a suite of assessment tools configured by `settings`.

    Args:
        conf: Configuration used. If points are 0.0 for any tool, the tool is skipped.

    Returns:
        Results scaled to the number of points in configuration.
    """
    results = GradescopeResults()
    tests = []

    submission_path = path.join(conf.src_root, conf.src_path)

    if conf.pytest_points > 0.0:
        tests += pytest(conf.test_root, conf.test_path, conf.src_root, conf.pytest_points)

    if conf.typecheck_points > 0.0:
        tests.append(typecheck(submission_path, conf.typecheck_points))

    if conf.lint_points > 0.0:
        tests.append(lint(submission_path, conf.lint_points))

    meta_data = None
    if path.exists(SUBMISSION_METADATA):
        with open(SUBMISSION_METADATA, 'r') as f:
            try:
                meta_data = json.load(f)
            except Exception:
                ...

    results.tests = tests
    results.visibility = GradescopeVisibility.VISIBLE
    results.extra_data = conf.__dict__

    if meta_data is not None:
        if meta_data['created_at'].split("T")[0] <= conf.ec_date_1:
            for x in results.tests:
                ec1 = conf.ec_multiplier_1 * 100 - 100
                x.score += ec1 / len(results.tests)
        elif meta_data['created_at'].split("T")[0] <= conf.ec_date_2:
            for x in results.tests:
                ec2 = conf.ec_multiplier_2 * 100 - 100
                x.score += ec2 / len(results.tests)
                
    return results
