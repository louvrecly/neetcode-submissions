class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # n: 5 | e: [[0 1] [0 2] [0 3] [1 4]]
        # 0 - 1 - 4
        # | \
        # 3  2
        # n: 5 | e: [[0 1] [1 2] [2 3] [1 3] [1 4]]
        # 0 - 1 - 2
        #     | \ |
        #     4   3
        # Topological Sort - Post-Order DFS
        # n: 5 | e: [[0 1] [0 2] [0 3] [1 4]]
        # adj: { 0:[1 2 3] 1:[0 4] 2:[0] 3:[0] 4:[1] }
        # f: [0] | c: 0 | adj[0]: [1 2 3] | v: {}
        # Time: O(E + V) | Space: O(E + V)
        if n <= 1:
            return True

        if n > 1 and not edges:
            return False

        adj = [set() for _ in range(n)]

        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        visiting = {}  # Mapping node i -> True=visiting | False=visited

        def dfs(i: int) -> bool:
            if i in visiting:
                return visiting[i]

            visiting[i] = True

            for j in adj[i].copy():
                adj[i].remove(j)
                adj[j].remove(i)
                if dfs(j):
                    return True

            visiting[i] = False

        if dfs(edges[0][0]):
            return False

        return len(visiting) == n
