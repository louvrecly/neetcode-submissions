class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # [
        #     [ 0  1  2 10]
        #     [ 9 14  4 13]
        #     [12  3  8 15]
        #     [11  5  7  6]
        # ]
        # Min Heap
        # cost = Manhattan distance + min(0, elevation - destination elevation)
        # 0 | f: [1 9] | m: 1
        # 1 | f: [2 9 14] | m: 2
        # 2 | f: [4 9 10 14] | m: 4
        # 4 | f: [8 9 10 13 14] | m: 8
        # 8 | f: [3 7 9 10 13 14 15] | m: 8
        # 7 | f: [3 9 10 13 14 15] | m: 8
        # Time: O(mn log mn) | Space: O(mn)
        m, n = len(grid), len(grid[0])
        maxElevation = grid[m - 1][n - 1]

        def cellCost(r: int, c: int) -> int:
            return (m + n) - (r + c) + max(0, grid[r][c] - grid[m - 1][n - 1])

        frontier = [(cellCost(0, 0), 0, 0)]
        steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()  # visited cells (r, c)

        while frontier:
            cost, r, c = heapq.heappop(frontier)
            if r == m - 1 and c == n - 1:
                return maxElevation

            if (r, c) in visited:
                continue

            visited.add((r, c))
            maxElevation = max(maxElevation, grid[r][c])

            for stepR, stepC in steps:
                nextR, nextC = r + stepR, c + stepC
                if (
                    0 <= nextR < m and
                    0 <= nextC < n and
                    (nextR, nextC) not in visited
                ):
                    cost = cellCost(nextR, nextC)
                    heapq.heappush(frontier, (cost, nextR, nextC))
