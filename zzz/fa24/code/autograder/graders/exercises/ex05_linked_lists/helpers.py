"""Helpers for ex05 grader."""
from __future__ import annotations
from typing import Optional


class Node:
    """Generic linked list Node."""
    value: int
    next: Optional[Node]

    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next
    
    def __repr__(self) -> str:
        """Produce a string representation of a linked list."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"
    
    def __eq__(self, rhs: Optional[Node]) -> bool:
        """Compare deep equality of two linked lists."""
        if rhs is None or self.value != rhs.value:
            return False
        elif self.next is None and rhs.next is not None:
            return False
        else:
            return self.next == rhs.next


def listify(xs: list[int]) -> Optional[Node]:
    """Construct a singly linked list of Nodes from a list."""
    if len(xs) == 0:
        return None
    else:
        return Node(xs[0], listify(xs[1:]))