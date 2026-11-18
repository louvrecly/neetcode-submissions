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
        if not root:
            return []

        node = root
        stack = []
        result = []

        while stack or node:
            if not node:
                node = stack.pop()
                continue

            result.append(node.val)
            stack.append(node.right)
            node = node.left

            while node:
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                node = node.left

            node = stack.pop()

        return result
