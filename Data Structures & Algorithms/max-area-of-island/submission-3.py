class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # [
        #     [0 1 1 0 1]
        #     [1 0 1 0 1]
        #     [0 1 1 0 1]
        #     [0 1 0 0 1]
        # ]
        # Time: O(m * n * 4 ** (m * n)) | Space: O(m * n * 4 * (m * n))
        m, n = len(grid), len(grid[0])
        visited = set()
        # Find area (DFS)
        def findArea(r: int, c: int) -> int:
            # Mark cell visited
            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                (r, c) in visited or
                grid[r][c] != 1
            ):
                return 0
            visited.add((r, c))
            # Find neighbors -> find area
            return 1 + (
                findArea(r - 1, c) +
                findArea(r, c - 1) +
                findArea(r + 1, c) +
                findArea(r, c + 1)
            )

        # Init max area as 0
        maxArea = 0
        # Iterate Row
        for r in range(m):
            # Iterate Column
            for c in range(n):
                # Found 0 -> Skip
                # Found 1 -> find area
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = findArea(r, c)
                    # Update max area
                    maxArea = max(maxArea, area)
        # Return Max area
        return maxArea
