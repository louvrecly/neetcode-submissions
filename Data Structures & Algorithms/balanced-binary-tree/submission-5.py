# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Time: O(n) | Space: O(n)
        def dfs(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if not node:
                return (True, 0)

            l_balanced, l_height = dfs(node.left)
            r_balanced, r_height = dfs(node.right)
            return (
                l_balanced and r_balanced and abs(l_height - r_height) <= 1,
                max(l_height, r_height) + 1
            )

        return dfs(root)[0]
