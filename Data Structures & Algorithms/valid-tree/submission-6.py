class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid Tree -> no cycle & all nodes connected
        # Time: O(E + V) | Space: O(E + V)
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = set()
        queue = deque([0])

        while queue:
            i = queue.popleft()
            visited.add(i)

            for j in adj[i]:
                if j not in visited:
                    queue.append(j)

        return len(visited) == n
