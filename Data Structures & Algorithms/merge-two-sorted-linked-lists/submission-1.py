# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # [1 2 4] [1 3 5]
        #  ^       ^     | 1 = 1 | [1 1]
        #    ^       ^   | 2 < 3 | [1 1 2]
        #      ^     ^   | 4 > 3 | [1 1 2 3]
        #      ^       ^ | 4 < 5 | [1 1 2 3 4]
        #        ^     ^ | N vs 5 | [1 1 2 3 4 5]
        # Time: O(m + n) | Space: O(1)
        pointer1, pointer2 = list1, list2
        head = ListNode()
        node = head

        while pointer1 and pointer2:
            if pointer1.val < pointer2.val:
                node.next = pointer1
                pointer1 = pointer1.next
            else:
                node.next = pointer2
                pointer2 = pointer2.next
            node = node.next

        if pointer1:
            node.next = pointer1

        if pointer2:
            node.next = pointer2

        return head.next
