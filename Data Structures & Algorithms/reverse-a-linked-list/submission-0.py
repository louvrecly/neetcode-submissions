# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 > 1 > 2 > 3 > N
        # H
        # N   0 > 1 > 2 > 3 > N
        # P   C   T
        # N < 0   1 > 2 > 3 > N
        # P   C   T
        # N < 0   1 > 2 > 3 > N
        #     P   C   T
        # N < 0 < 1   2 > 3 > N
        #     P   C   T
        # N < 0 < 1 < 2   3 > N
        #         P   C   T
        # N < 0 < 1 < 2   3 > N
        #             P   C   T
        # N < 0 < 1 < 2 < 3   N
        #             P   C   T
        # Time: O(n) | Space: O(1)
        prev = None
        curr = head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev, curr = curr, nextNode

        return prev
