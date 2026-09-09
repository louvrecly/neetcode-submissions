# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #   1
        #  / \
        # N   2
        #    / \
        #   3   4
        #  / \
        # 5   N
        # None node - h: 0
        # leaf node - h: 1
        # branch node - h: max(left, right) + 1
        # diameter = max(diameter, height, left + right)
        # Time: O(n) | Space: O(n)
        self.path = 0

        def findHeight(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            leftHeight = findHeight(node.left)
            rightHeight = findHeight(node.right)

            self.path = max(self.path, leftHeight + rightHeight)
            return max(leftHeight, rightHeight) + 1

        height = findHeight(root) - 1
        return max(height, self.path)
