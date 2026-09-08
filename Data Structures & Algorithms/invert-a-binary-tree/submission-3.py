# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #      1
        #    /   \
        #   2     3
        #  / \   / \
        # 4   5 6   7
        # ================
        #      1   <---- C | L: 2 R: 3 | dfs(L) dfs(R)
        #    /   \
        #   2     3
        #  / \   / \
        # 4   5 6   7
        # ================
        #      1
        #    /   \
        #   2     3   <---- C | L: 6 R: 7 | dfs(L) dfs(R)
        #  / \   / \
        # 4   5 6   7
        # ================
        #      1
        #    /   \
        #   2     3
        #  / \   / \
        # 4   5 6   7   <---- C | L: N R: N
        # ================
        #     2
        #    / \
        #   3   N
        #  / \
        # 1   N
        # Time: O(n) | Space: O(n)
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
