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
        head = ListNode()
        pointer = head

        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                pointer, list1 = pointer.next, list1.next
            else:
                pointer.next = list2
                pointer, list2 = pointer.next, list2.next
        
        if list1:
            pointer.next = list1

        if list2:
            pointer.next = list2

        return head.next
