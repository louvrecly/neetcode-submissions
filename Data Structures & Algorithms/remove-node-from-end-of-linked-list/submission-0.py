# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # h: 1 -> 2 -> 3 -> 4 -> N | n: 2
        #    ^ | m: 1
        #         ^ | m: 2
        #               ^ | m: 3
        #                   ^ | m: 4
        #                        ^ | m: 4
        # H -> 1 -> 2 -> 3 -> 4 -> N | n: 2
        #           ^
        # Time: O(n) | Space: O(1)
        node = head
        m = 0
        while node:
            m += 1
            node = node.next

        new_head = ListNode(0, head)
        node = new_head
        for _ in range(m - n):
            node = node.next

        node.next = node.next.next
        return new_head.next
