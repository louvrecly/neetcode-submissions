# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 321: 1 -> 2 -> 3 -> N
        # 654: 4 -> 5 -> 6 -> N
        #      ^ | 1+4=5 | c: 0 | 5 -> N
        #           ^ | 2+5=7 | c: 0 | 5 -> 7 -> N
        #                ^ | 3+6=9 | c: 0 | 5 -> 7 -> 9 -> N
        # 4321: 1 -> 2 -> 3 -> 4 -> N
        # 765:  5 -> 6 -> 7 -> N
        #       ^ | 1+5=6 | c: 0  | 6 -> N
        #            ^ | 2+6=8 | c: 0  | 6 -> 8 -> N
        #                 ^ | 3+7=10 | c: 1 | 5 -> 7 -> 0 -> N
        #                      ^ | 4+0+1=5 | c: 0 | 5 -> 7 -> 0 -> 5 -> N
        # Time: O(max(m, n)) | Space: O(1)
        root = ListNode()
        node = root
        carry = 0

        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = val // 10
            node.next = ListNode(val % 10)
            node = node.next
            l1, l2 = l1.next, l2.next

        for l in [l1, l2]:
            while l:
                val = l.val + carry
                carry = val // 10
                node.next = ListNode(val % 10)
                node = node.next
                l = l.next

        if carry:
            node.next = ListNode(carry)

        return root.next
