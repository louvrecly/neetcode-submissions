# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative Stack
        # Time: O(n) | Space: O(n)
        node = root
        stack = []
        result = []

        while node or stack:
            if node:
                result.append(node.val)
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()

        return result
