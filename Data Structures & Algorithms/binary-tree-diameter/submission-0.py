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
        # max(parent + left, parent + right, left + right)
        def dfs(node: Optional[TreeNode]) -> Tuple[int, bool]:
            if not node:
                return (0, False)
            
            leftPath, leftExcludeParent = dfs(node.left)
            rightPath, rightExcludeParent = dfs(node.right)
            leftParentPath = leftPath if leftExcludeParent or not node.left else leftPath + 1
            rightParentPath = rightPath if rightExcludeParent or not node.right else rightPath + 1

            path = leftParentPath
            excludeParent = leftExcludeParent

            if rightParentPath > path:
                path = rightParentPath
                excludeParent = rightExcludeParent

            childrenPath = leftParentPath + rightParentPath

            if childrenPath > path:
                return (childrenPath, True)

            return (path, excludeParent)

        path, _ = dfs(root)
        return path
