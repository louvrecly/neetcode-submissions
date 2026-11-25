class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Time: O(mn) | Space: O(mn)
        m, n = len(grid), len(grid[0])
        adj = {}  # mapping (r, c) -> land neighbors count
        steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        # Iterate through row
        for r in range(m):
            # Iterate through col
            for c in range(n):
                # Cell is land -> Count land neighbors, mark land
                if grid[r][c] == 1:
                    adj[(r, c)] = 0
                    for step_r, step_c in steps:
                        r1, c1 = r + step_r, c + step_c
                        if (
                            0 <= r1 < m and
                            0 <= c1 < n and
                            grid[r1][c1] == 1
                        ):
                            adj[(r, c)] += 1

        # Return (land cells count) * 4 - sum(land neighbors count)
        return len(adj.keys()) * 4 - sum(adj.values())
