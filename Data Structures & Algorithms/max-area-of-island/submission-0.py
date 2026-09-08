class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # [0 1 1 0 1]
        # [1 0 1 0 1]
        # [0 1 1 0 1]
        # [0 1 0 0 1]
        # Time: O(m * n) | Space: O(m * n)
        m, n = len(grid), len(grid[0])
        visited = set()  # visited cells (r, c)

        # Find area (DFS)
        def findArea(r: int, c: int) -> int:
            # Visited Cell -> return 0
            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                (r, c) in visited
            ):
                return 0

            # Mark cell as visited
            visited.add((r, c))

            # Cell is water -> return 0
            if grid[r][c] == 0:
                return 0

            # return 1 + neighbor areas
            return (
                1 +
                findArea(r - 1, c) +
                findArea(r, c - 1) +
                findArea(r + 1, c) +
                findArea(r, c + 1)
            )

        maxArea = 0

        # Iterate rows
        for r in range(m):
            # Iterate columns
            for c in range(n):
                # Found unvisited land -> find area
                if (r, c) not in visited and grid[r][c] == 1:
                    area = findArea(r, c)
                    # Compute max area
                    maxArea = max(maxArea, area)

        # Return max area
        return maxArea
