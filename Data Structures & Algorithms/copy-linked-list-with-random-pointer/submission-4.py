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
        # cloned: 3* -> 7* -> 4* -> 5* -> N
        #         v     v     v     v
        #         N     N     N     N
        # map: {3: 3*, 7: 7*, 4: 4*, 5:, 5*}
        # cloned: 3* -> 7* -> 4* -> 5* -> N
        #         v     v     v     v
        #         N     5*    3*    7*
        # Time: O(n) | Space: O(n)
        if not head:
            return None

        old = head
        new = Node(0)
        nodes_map = {}

        while old:
            new.next = Node(old.val)
            nodes_map[old] = new.next
            old, new = old.next, new.next

        old = head
        while old:
            if old.random:
                nodes_map[old].random = nodes_map[old.random]
            old = old.next

        return nodes_map[head]
