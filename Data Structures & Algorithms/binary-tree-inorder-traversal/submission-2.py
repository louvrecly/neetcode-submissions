# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # In-Order DFS
        # Time: O(n) | Space: O(n)
        values = []
        stack = []
        pointer = root

        while stack or pointer:
            while pointer:
                stack.append(pointer)
                pointer = pointer.left

            node = stack.pop()
            values.append(node.val)
            pointer = node.right

        return values
