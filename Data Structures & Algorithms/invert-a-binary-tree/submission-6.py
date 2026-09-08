# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time: O(n) | Space: O(n)
        def swapChildren(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None

            left = node.left
            right = node.right

            node.left = swapChildren(right)
            node.right = swapChildren(left)

            return node

        return swapChildren(root)
