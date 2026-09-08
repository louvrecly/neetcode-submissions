# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #      1
        #    /   \
        #   2     3
        #  / \   / \
        # N   N 4   N
        # BFS
        # Time: O(n) | Space: O(n)
        if not root:
            return 0

        children = deque([root])
        level = 0
        
        while children:
            n = len(children)
            level += 1

            for i in range(n):
                node = children.popleft()
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)

        return level
