"""Formats for Pytest and Gradescope results."""

from __future__ import annotations
import json
from enum import Enum
from typing import Any, Dict, List


class PytestTest:
    """Plain-old data object that represents a Pytest result."""

    testid: str
    title: str
    weight: int
    passed: bool
    stdout: str
    duration: float

    def __init__(self, test: Dict[str, Any], test_root: str):
        """Initialize from a row of JSON output dictionary."""
        self.title = self.testid = test["nodeid"]
        self.passed = test["outcome"] == "passed"
        self.duration = test["duration"]
        self.stdout = ""
        self.weight = 1
        for prop in test["user_properties"]:
            name, value = prop
            if name == "title":
                self.title = value
            elif name == "weight":
                self.weight = value
        for section in test["sections"]:
            title, content = section
            if title == "Captured stdout call":
                self.stdout = content

        if not self.passed:
            message = test['longrepr']['reprcrash']['message']
            lineno = test['longrepr']['reprcrash']['lineno']
            path: str = test['longrepr']['reprcrash']['path']
            path = path.replace(f"{test_root}/", "")
            if self.stdout != "":
                self.stdout += "\n\n"
            self.stdout = f"{path}:{lineno} - {message}"

    def __str__(self):
        """Represent test result as a short string title."""
        return self.title

    def __repr__(self):
        """Represent test result as a longer string."""
        return f"({self.weight}) - {self.testid} - {self.title} - \
            {'passed' if self.passed else 'failed'}"


class GradescopeTest:
    """Plain-old data object that represents a Gradescope Test result."""

    score: float
    max_score: float
    name: str
    output: str

    def __init__(
        self,
        name: str = "",
        score: float = 0.0,
        max_score: float = 1.0,
        output: str = ""
    ) -> None:
        """Construct a GradescopeTest result."""
        self.max_score = max_score
        self.score = score
        self.name = name
        self.output = output

    @staticmethod
    def from_pytest(test: PytestTest) -> GradescopeTest:
        """Construct a GradescopeTest result from a PytestTest result."""
        max_score = test.weight
        score = test.weight if test.passed else 0.0
        name = test.title
        output = test.stdout
        return GradescopeTest(name, score, max_score, output)

    def __repr__(self) -> str:
        """Represent as a JSON string."""
        return json.dumps({
            'score': self.score,
            'max_score': self.max_score,
            'name': self.name,
            'output': self.output
        })

    def to_json(self) -> str:
        return self.__repr__()


class GradescopeVisibility(Enum):
    HIDDEN = "hidden"
    AFTER_DUE_DATE = "after_due_date"
    AFTER_PUBLISHED = "after_published"
    VISIBLE = "visible"


class GradescopeResults:
    visibility: GradescopeVisibility
    stdout_visibility: GradescopeVisibility
    extra_data: Dict[str, any]
    tests: List[GradescopeTest]

    def __init__(self):
        self.visibility = GradescopeVisibility.VISIBLE
        self.stdout_visibility = GradescopeVisibility.VISIBLE
        self.extra_data = {}
        self.tests = []

    @property
    def score(self) -> float:
        total = 0.0
        for test in self.tests:
            total += test.score
        return total

    def __repr__(self) -> str:
        return json.dumps(self, cls=GradescopeEncoder)

    def to_json(self) -> str:
        return self.__repr__()


class GradescopeEncoder(json.JSONEncoder):
    """JSONEncoder for GradescopeResults."""

    def default(self, o: GradescopeResults):
        """Produce the default representation in JSON."""
        if type(o) is GradescopeResults:
            return {
                "score": o.score,
                "visibility": o.visibility.value,
                "stdout_visibility": o.stdout_visibility.value,
                "extra_data": o.extra_data,
                "tests": o.tests
            }
        else:
            return o.__dict__
