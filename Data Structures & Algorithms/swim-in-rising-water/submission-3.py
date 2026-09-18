class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Djikstra's Algorithm -> BFS + Min Heap
        # cost = max(prevCost, currCost)
        # Time: O(n^2 log n) | Space: O(n^2)
        n = len(grid)
        minHeap = [(grid[0][0], 0, 0)]
        steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()

        while minHeap:
            cost, r, c = heapq.heappop(minHeap)
            if r == n - 1 and c == n - 1:
                return cost

            if (r, c) in visited:
                continue

            visited.add((r, c))

            for stepR, stepC in steps:
                nextR, nextC = r + stepR, c + stepC
                if (
                    0 <= nextR < n and
                    0 <= nextC < n and
                    (nextR, nextC) not in visited
                ):
                    nextCost = max(cost, grid[nextR][nextC])
                    heapq.heappush(minHeap, (nextCost, nextR, nextC))
