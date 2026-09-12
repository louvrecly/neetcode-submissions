"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
visited = set()
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # [[2] [1 3] [2]]
        # 1 - 2 - 3
        # ^ | v: 1 | n: [2]
        #     ^ | v: 2 | n: [1 3]
        #         ^ | v: 3 | n: [2]
        # Time: O(V * E + E) | Space: O(V * E + E)
        if not node:
            return None

        adj = defaultdict(list)  # adjacency list: val -> neighbors[]

        def dfs(curr: Optional['Node']) -> None:
            if not curr or curr.val in adj:
                return

            for neighbor in curr.neighbors:
                adj[curr.val].append(neighbor.val)
                dfs(neighbor)

        dfs(node)
        nodesMap = {}
        for val in adj:
            nodesMap[val] = Node(val)

        for val, neighborVals in adj.items():
            for neighborVal in neighborVals:
                neighbor = nodesMap[neighborVal]
                nodesMap[val].neighbors.append(neighbor)

        return nodesMap[node.val] if node.val in nodesMap else Node()
