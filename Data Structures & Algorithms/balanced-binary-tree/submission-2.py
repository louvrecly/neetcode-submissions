# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Time: O(n) | Space: O(n)
        if not root:
            return True

        if not root.left and not root.right:
            return True

        def findHeight(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            return max(findHeight(node.left), findHeight(node.right)) + 1

        if not root.left:
            return findHeight(root.right) <= 1

        if not root.right:
            return findHeight(root.left) <= 1

        leftHeight = findHeight(root.left)
        rightHeight = findHeight(root.right)
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(leftHeight - rightHeight) <= 1
