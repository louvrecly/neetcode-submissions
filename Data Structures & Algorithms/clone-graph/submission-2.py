"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Time: O(V * E) | Space: O(V)
        if not node:
            return None

        nodesMap = {}
        nodesMap[node] = Node(node.val)
        queue = [node]

        while queue:
            curr = queue.pop()

            for neighbor in curr.neighbors:
                if neighbor not in nodesMap:
                    nodesMap[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                nodesMap[curr].neighbors.append(nodesMap[neighbor])

        return nodesMap[node]
