class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # n: 5 | e: [[0 1] [1 2] [3 4]]
        # 0 - 1 - 2
        # 3 - 4
        # c: 2
        # n: 5 | e: [[0 1] [1 2] [2 3] [3 4]]
        # 0 - 1 - 2 - 3 - 4
        # c: 1
        # Time: O(E + V) | Space: O(E + V)
        adj = [[] for _ in range(n)]

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = set()
        count = 0

        def dfs(node: int, prev: int = -1) -> bool:
            if node in visited:
                return False

            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == prev or neighbor in visited:
                    continue
                dfs(neighbor, node)
            return True

        for i in range(n):
            if dfs(i):
                count += 1

        return count
