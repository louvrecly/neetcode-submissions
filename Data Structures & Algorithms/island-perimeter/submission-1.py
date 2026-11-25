class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Time: O(mn) | Space: O(mn)
        m, n = len(grid), len(grid[0])
        lands_count = 0
        edges = set()
        steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    lands_count += 1
                    for step_r, step_c in steps:
                        r1, c1 = r + step_r, c + step_c
                        if (
                            0 <= r1 < m and
                            0 <= c1 < n and
                            grid[r1][c1]
                        ):
                            edges.add(tuple(sorted([(r, c), (r1, c1)])))

        return 4 * lands_count - 2 * len(edges)
