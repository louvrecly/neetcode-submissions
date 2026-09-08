# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [2 4 6 8 10] | l: 5
        # [2 10 4 8 6]
        # 2 > 4 > 6 > 8 > 10 > N
        # [2 4 6 8 10]
        #  L        R | L > R
        #    L      R | R > L
        #    L   R    | L > R
        #      L R    | R > L
        # L > N
        # 2 > 10 > 4 > 8 > 6 > N
        # Time: O(n) | Space: O(n)
        node = head
        nodes = []

        while node:
            nodes.append(node)
            node = node.next

        left, right = 0, len(nodes) - 1

        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            nodes[right].next = nodes[left]
            right -= 1

        nodes[left].next = None
