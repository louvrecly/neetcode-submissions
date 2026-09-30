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
        # 3 > 7 > 4 > 5 > N
        # v   v   v   v
        # N   5   3   7
        # old: 3    7    4    5
        #      v    v    v    v
        # new: 3* > 7* > 4* > 5* > N
        #      v    v    v    v
        #      N    N    N    N
        # new: 3* > 7* > 4* > 5* > N
        #      v    v    v    v
        #      N    5*   3*   7*
        # Time: O(n) | Space: O(1)
        if not head:
            return None

        old = head

        while old:
            new = Node(old.val)
            new.next = old.next
            old.next = new
            old = new.next

        new_head = head.next
        old = head
        while old:
            if old.random:
                old.next.random = old.random.next
            old = old.next.next

        old = head
        while old:
            new = old.next
            old.next = new.next
            if new.next:
                new.next = new.next.next
            old = old.next

        return new_head
        