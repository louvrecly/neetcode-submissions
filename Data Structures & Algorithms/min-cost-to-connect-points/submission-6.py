class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # [[0 0] [2 2] [0 3] [0 2]]
        # adj: {
        #     (0 0): [(4 2 2) (3 0 3) (2 0 2)]
        #     (0 2): [(2 0 0) (2 2 2) (1 0 3)]
        #     (0 3): [(3 0 0) (3 2 2) (1 0 2)]
        #     (2 2): [(4 2 2) (3 0 3) (2 0 2)]
        # }
        # Time: O(n ^ 2 log n) | Space: O(n ^ 2)
        n = len(points)
        adj = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi = points[i]
                xj, yj = points[j]
                cost = abs(xi - xj) + abs(yi - yj)
                adj[i].append((cost, j))
                adj[j].append((cost, i))

        minCost = 0
        visited = set()
        frontier = [(0, 0)]
    
        while len(visited) < n:
            cost, i = heapq.heappop(frontier)
            if i in visited:
                continue
            visited.add(i)
            minCost += cost
            for c, j in adj[i]:
                if j not in visited:
                    heapq.heappush(frontier, (c, j))

        return minCost
