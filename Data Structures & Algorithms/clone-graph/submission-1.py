"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Time: O(V * E + E) | Space: O(V)
        if not node:
            return None

        nodesMap = {}
        nodesMap[node.val] = Node(node.val)
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor.val not in nodesMap:
                    nodesMap[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                nodesMap[curr.val].neighbors.append(nodesMap[neighbor.val])

        return nodesMap[node.val]
