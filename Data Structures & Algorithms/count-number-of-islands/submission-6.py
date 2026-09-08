class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        # Time: O(m * n) | Space: O(m * n)
        m, n = len(grid), len(grid[0])
        visited = set()  # visited cells (r, c)

        def dfs(r: int, c: int) -> None:
            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                (r, c) in visited or
                grid[r][c] != '1'
            ):
                return

            visited.add((r, c))
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r, c + 1)

        count = 0

        for r in range(m):
            for c in range(n):
                if (r, c) not in visited and grid[r][c] == '1':
                    dfs(r, c)
                    count += 1

        return count

        