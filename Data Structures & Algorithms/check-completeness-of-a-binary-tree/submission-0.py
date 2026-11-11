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
        # Time: O(n) | Space: O(n)
        if not root:
            return True

        first_none = 0
        last_node = 0
        i = 0
        queue = deque([root])

        while queue:
            node = queue.popleft()
            i += 1
            if not node and first_none == 0:
                first_none = i
            elif node:
                last_node = i
            if node:
                queue.append(node.left)
                queue.append(node.right)

        return first_none > last_node
