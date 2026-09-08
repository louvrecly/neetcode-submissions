class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # [1 1 0 0 1]
        # [1 1 0 0 1]
        # [0 0 1 0 0]
        # [0 0 0 1 1]
        # ==============
        # [0 1 1 1 0]
        # [0 1 0 1 0]
        # [1 1 0 0 0]
        # [0 0 0 0 0]
        # DFS with stack
        # r, c: 1 -> neighbors (up, down, left, right) -> stack
        # Time: O(m * n) | Space: O(m * n)
        count = [0]
        m, n = len(grid), len(grid[0])
        visited = set()
        steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r: int, c: int, fromLand: bool) -> None:
            visited.add((r, c))
            isLand = grid[r][c] == '1'

            if isLand and not fromLand:
                count[0] += 1
                grid[r][c] = '0'

            for stepR, stepC in steps:
                nextR, nextC = r + stepR, c + stepC
                if (
                    0 <= nextR < m and
                    0 <= nextC < n and
                    grid[nextR][nextC] == '1' and
                    (nextR, nextC) not in visited
                ):
                    dfs(nextR, nextC, isLand)

        for r in range(m):
            for c in range(n):
                if (r, c) not in visited:
                    dfs(r, c, False)

        return count[0]
