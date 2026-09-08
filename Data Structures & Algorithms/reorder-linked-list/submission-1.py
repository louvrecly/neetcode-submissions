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
        # H > N | [2 4 6 8 10]
        # Time: O(n) | Space: O(n)
        pointer = head
        nodes = deque([])

        while pointer:
            nodes.append(pointer)
            pointer = pointer.next

        n = len(nodes)
        head = ListNode()
        pointer = head

        for i in range(n):
            node = nodes.pop() if i % 2 else nodes.popleft()
            pointer.next = node
            pointer = pointer.next

        pointer.next = None
        head = head.next
