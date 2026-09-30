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
        # 3 -> 7 -> 4 -> 5 -> N
        # v    v    v    v
        # N    5    3    7
        # adj: { 3: (7 N), 7: (4 5), 4: (5 3), 5: (N 7) }
        # adj = {}  # Mapping node -> (node.next, node.random)
        # Time: O(n) | Space: O(n)
        pointer = head
        nodes = []
        copies = []
        nodes_map = {}
        i = 0

        while pointer:
            nodes.append(pointer)
            copied = Node(pointer.val)
            copies.append(copied)
            nodes_map[pointer] = i
            pointer = pointer.next
            i += 1

        new_head = Node(0)
        pointer = new_head
        for node in copies:
            pointer.next = node
            pointer = pointer.next

        pointer = new_head.next
        for node in nodes:
            if node.random in nodes_map:
                i = nodes_map[node.random]
                pointer.random = copies[i]
            pointer = pointer.next

        return new_head.next
