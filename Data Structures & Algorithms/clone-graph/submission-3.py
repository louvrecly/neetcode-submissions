"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Time: O(V + E) | Space: O(V)
        nodesMap = {}

        def dfs(curr: Optional['Node']) -> Optional['Node']:
            if not curr:
                return None

            if curr in nodesMap:
                return nodesMap[curr]

            nodesMap[curr] = Node(curr.val)

            for neighbor in curr.neighbors:
                nodesMap[curr].neighbors.append(dfs(neighbor))

            return nodesMap[curr]

        return dfs(node)
