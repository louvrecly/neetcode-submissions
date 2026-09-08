# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Time: O(m + n) | Space: O(m)
        pointer = headA
        setA = set()

        while pointer:
            setA.add(pointer)
            pointer = pointer.next

        pointer = headB
        while pointer:
            if pointer in setA:
                return pointer
            pointer = pointer.next

        return None
