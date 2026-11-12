# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # In-Order DFS
        # Time: O(n) | Space: O(2^h)
        values = []

        def inOrder(node: Optional[TreeNode]) -> None:
            if node:
                inOrder(node.left)
                values.append(node.val)
                inOrder(node.right)

        inOrder(root)
        return values
