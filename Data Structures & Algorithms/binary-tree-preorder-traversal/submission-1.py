# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative Queue + Stack
        # Time: O(n) | Space: O(n)
        result = []

        if not root:
            return result

        visited = set()
        queue = deque([root])
        stack = []

        while queue or stack:
            node = queue.popleft() if queue else stack.pop()
            if node in visited:
                continue

            visited.add(node)
            result.append(node.val)
            while node.left:
                queue.append(node.left)
                if node.right:
                    stack.append(node.right)
                node = node.left
            if node.right:
                stack.append(node.right)

        return result
