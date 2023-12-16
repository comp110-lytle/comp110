"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self. next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Documentation."""
        return self.data
    
    def tail(self) -> Node | None:
        """Documentation."""
        return self.next
    
    def last(self) -> int:
        """Documentation."""
        if self.next is None:
            # base case
            return self.data
        else: 
            return self.next.last()