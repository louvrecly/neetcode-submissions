class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Time: O(m * n) | Space: O(m * n)
        m, n = len(grid), len(grid[0])
        queue = deque([])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c))

        steps = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        visited = set()
        inf = 2 ** 31 - 1

        while queue:
            r, c = queue.popleft()
            if (r, c) in visited:
                continue

            visited.add((r, c))
            for stepR, stepC in steps:
                nextR, nextC = r + stepR, c + stepC
                if (
                    0 <= nextR < m and
                    0 <= nextC < n and
                    (nextR, nextC) not in visited and
                    grid[nextR][nextC] == inf
                ):
                    grid[nextR][nextC] = grid[r][c] + 1
                    queue.append((nextR, nextC))
