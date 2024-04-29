"""Helpers for ex10 grader."""
from __future__ import annotations
from typing import Optional


class Node:
    """Generic linked list Node."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node] = None):
        self.data = data
        self.next = next
    
    def __repr__(self) -> str:
        """Produce a string representation of a linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
    
    def __eq__(self, rhs: Optional[Node]) -> bool:
        """Compare deep equality of two linked lists."""
        if rhs is None or self.data != rhs.data:
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