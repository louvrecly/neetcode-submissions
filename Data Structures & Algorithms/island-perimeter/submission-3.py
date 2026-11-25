class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Time: O(mn) | Space: O(1)
        m, n = len(grid), len(grid[0])
        perimeter = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r and grid[r - 1][c] == 1:
                        perimeter -= 2
                    if c and grid[r][c - 1] == 1:
                        perimeter -= 2
        return perimeter
