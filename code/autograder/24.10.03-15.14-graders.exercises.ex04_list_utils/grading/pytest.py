"""Script for unit testing a file/directory with Pytest.

Output format is Gradescope JSON format. An array of test object JSON is produced.

CLI Usage: python -m comp110.codeqa.pytest [test root] [test path] [source root]

API Usage:
    pytest(test_root: str, test_path: str, src_root: str, max_score: float) -> List[GradescopeTest]

Args:
    test root: path to root of testing module
    test path: path relative to `test root` to specify tests
    source root: path to root of src under test
"""

__author__ = "Kris Jordan <kris@cs.unc.edu>"
__copyright__ = "Copyright 2020, Kris Jordan"
__license__ = "MIT"

import json
import os
import subprocess
import sys
import tempfile

from typing import List, Tuple
from .formats import PytestTest, GradescopeTest, GradescopeEncoder

PYTHON = sys.executable


def main() -> None:
    """Entrypoint of script."""
    test_root, test_path, src_root = _parse_args(sys.argv)
    gradescope_tests = pytest(test_root, test_path, src_root, 100.0)
    print(json.dumps(gradescope_tests, cls=GradescopeEncoder))


def _parse_args(argv: List[str]) -> Tuple[str, str, str]:
    if len(argv) != 4:
        print("Usage: python -m grading.pytest [test root] [test path] [source root]", file=sys.stderr)
        sys.exit(1)
    return (argv[1], argv[2], argv[3])


def pytest(test_root: str, test_path: str, src_root: str, max_score: float) -> List[GradescopeTest]:
    """Run Pytest tests in `test_path` over `src_root`.

    Args:
        test_root: path to root of testing module
        test_path: path relative to `test root` to specify tests
        source_root: path to root of src under test

    Returns:
        A List of results weighted based on @weight annotation (1 is default).
    """
    temp_handle, temp_results = tempfile.mkstemp()
    _ensure_pythonpath(src_root)
    _ensure_pythonpath(test_root)
    subprocess.run(
        [
            PYTHON,
            '-m', 'pytest',
            '-p', 'grading.pytest_gradescope_plugin',
            '-q',
            f'--report-log={temp_results}', 
            os.path.join(test_root, test_path)
        ],
        capture_output=True)
    pytest_tests = _parse_json_report(temp_results, test_root)
    tests = [GradescopeTest.from_pytest(test) for test in pytest_tests]
    try:
        os.close(temp_handle)
        os.remove(temp_results)
    except PermissionError:
        print(f"Could not remove {temp_results}", file=sys.stderr)
    _scale_results(tests, max_score)
    return tests


def _ensure_pythonpath(path: str) -> None:
    if "PYTHONPATH" not in os.environ:
        os.environ["PYTHONPATH"] = path
    elif path not in os.environ["PYTHONPATH"]:
        os.environ["PYTHONPATH"] = f"{path}:{os.environ['PYTHONPATH']}"


def _parse_json_report(path_to_json_report: str, test_root: str) -> List[PytestTest]:
    """Read a JSON report file and returns a list of PytestTest results."""
    tests = []
    with open(path_to_json_report) as result_file:
        for line in result_file:
            test = json.loads(line)
            if 'when' in test and test['when'] == 'call':
                tests.append(PytestTest(test, test_root))
    return tests


def _scale_results(tests: List[GradescopeTest], max_score: float) -> None:
    """Scales the score and max_score data attributes to be out of the total max_score parameter."""
    total_possible = 0.0
    for test in tests:
        total_possible += test.max_score

    if total_possible > 0:
        scale = max_score / total_possible
    else:
        scale = 0

    for test in tests:
        test.max_score = round(test.max_score * scale, 1)
        test.score = round(test.score * scale, 1)


if __name__ == "__main__":
    main()
