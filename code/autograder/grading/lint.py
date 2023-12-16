"""Script for linting a directory with Flake8.

Output format is Gradescope JSON format. A single test object JSON is produced.
The test's max_score is 10.0 and for each lint infraction a point is subtracted.
The minimum score is 0.0.

CLI Usage: python -m comp110.codeqa.lint [source]

API Usage: lint(dir) - returns comp110.grading.formats.GradescopeTest

Args:
    source: Directory of Python source files to lint.
    target: Path to JSON result file to produce.

Future Improvements:
    - Make the point system more flexible.
"""

__author__ = "Kris Jordan <kris@cs.unc.edu>"
__copyright__ = "Copyright 2020, Kris Jordan"
__license__ = "MIT"

import json
import subprocess
import sys
import os
from typing import List
from .formats import GradescopeTest, GradescopeEncoder

PYTHON = sys.executable


def main() -> None:
    """Entrypoint of script. Gathers CLI arguments."""
    source = _parse_args(sys.argv)
    result = lint(source, 10.0)
    print(json.dumps(result, cls=GradescopeEncoder))


def _parse_args(argv: List[str]) -> str:
    if len(argv) != 2:
        print("Usage: python -m comp110.codeqa.lint [source]", file=sys.stderr)
        sys.exit(1)
    return argv[1]


def lint(path: str, max_score: float) -> GradescopeTest:
    """Lint a path with Flake8 and return a GradescopeTest.

    The GradescopeTest is out of 10 points with 1 point deducted per infraction.

    Args:
        path: Path of directory or file to lint.

    Returns:
        A GradescopeTest object.
    """
    result = subprocess.run(
        [PYTHON, "-m", "flake8", "--ignore", "W2,W291,W292,W293,E501", path], 
        capture_output=True
    )
    src_root = f'{os.environ["GRADING_SUBMISSION_ROOT"]}/' if "GRADING_SUBMISSION_ROOT" in os.environ else ""
    output = result.stdout.decode("utf-8").replace(src_root, "")
    lines = output.splitlines()
    if len(lines) > 0:
        output += "\nFor help understanding this feedback, see Resources > Style, Linting and Autograder Guide on the Course Site. \n"
    name = "Lint - Code style, documentation, and formatting."
    score = max(0.0, max_score - len(lines))
    return GradescopeTest(name, score, max_score, output)


if __name__ == "__main__":
    main()
