"""Script for type checking a path with mypy.

Output format is Gradescope JSON format. A single test object JSON is produced.
The test's max_score is 10.0 and for each mypy infraction a point is subtracted.
The minimum score is 0.0.

CLI Usage: python -m comp110.codeqa.typecheck [source]

API Usage: typecheck(path) - returns comp110.grading.formats.GradescopeTest

Args:
    source: Path of source code file or directory to type check.

Future Improvements:
    - Make the point system more flexible from CLI
"""

__author__ = "Kris Jordan <kris@cs.unc.edu>"
__copyright__ = "Copyright 2020, Kris Jordan"
__license__ = "MIT"

import json
import os
import subprocess
import sys
from typing import List
from .formats import GradescopeTest, GradescopeEncoder

PYTHON = sys.executable


def main() -> None:
    """Entrypoint of script."""
    source = _parse_args(sys.argv)
    result = typecheck(source, 10.0)
    print(json.dumps(result, cls=GradescopeEncoder))


def _parse_args(argv: List[str]) -> str:
    if len(argv) != 2:
        print("Usage: python -m grading.typecheck [source]", file=sys.stderr)
        sys.exit(1)
    return argv[1]


def typecheck(path: str, max_score: float) -> GradescopeTest:
    """Lint a path with Flake8 and return a GradescopeTest.

    The GradescopeTest is out of 10 points with 1 point deducted per infraction.

    Args:
        path: Path of directory or file to lint.

    Returns:
        A GradescopeTest object.
    """
    cwd = os.getcwd()
    if "GRADING_SUBMISSION_ROOT" in os.environ:
        os.chdir(os.environ["GRADING_SUBMISSION_ROOT"])  # mypy needs to be in root for imports
    mypy_options = ["--strict", "--namespace-packages", "--no-color-output", "--no-error-summary", path]
    command = [PYTHON, "-m", "mypy"] + mypy_options
    result = subprocess.run(command, capture_output=True)
    os.chdir(cwd)  # Go back to previous CWD
    src_root = f'{os.environ["GRADING_SUBMISSION_ROOT"]}/' if "GRADING_SUBMISSION_ROOT" in os.environ else ""
    output = result.stdout.decode("utf-8").replace(src_root, "")
    lines = output.splitlines()
    lines = [line for line in lines if "Source file found" not in line]
    lines = [line for line in lines if "mapping-file-paths-to-modules" not in line]
    output = "\n".join(lines)
    name = "Type Safety - Static type annotations."
    score = max(0.0, max_score - len(lines))
    return GradescopeTest(name, score, max_score, output)


if __name__ == "__main__":
    main()
