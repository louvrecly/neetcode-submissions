class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid Tree:
        # 1. All nodes connected
        # 2. No cycle (E = V + 1)
        # Time: O(E + V) | Space: O(E + V)
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = set()

        def dfs(i: int, prev: int) -> bool:
            if i in visited:
                return False

            visited.add(i)
            for j in adj[i]:
                if j == prev or j in visited:
                    continue
                if not dfs(j, i):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
