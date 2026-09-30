"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Time: O(n) | Space: O(n)
        if not head:
            return None

        nodes_map = {}  # Mapping node -> copy

        node = head
        while node:
            nodes_map[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            copy = nodes_map[node]
            copy.next = nodes_map[node.next] if node.next else None
            copy.random = nodes_map[node.random] if node.random else None
            node = node.next

        return nodes_map[head]
        