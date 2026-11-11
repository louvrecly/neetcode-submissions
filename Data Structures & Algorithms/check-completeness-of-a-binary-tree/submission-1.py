# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        #      1
        #    /   \
        #   2     3
        #  / \   /
        # 4   5 6
        # Level-Order Traversal
        # Time: O(n) | Space: O(n)
        if not root:
            return True

        found_none = False
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node and found_none:
                return False

            if not node:
                found_none = True

            if node:
                queue.append(node.left)
                queue.append(node.right)

        return True
