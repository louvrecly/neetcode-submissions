class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # [0 1 1 1 0]
        # [0 1 0 1 0]
        # [1 1 0 0 0]
        # [0 0 0 0 0]
        # 1
        # [1 1 0 0 1]
        # [1 1 0 0 1]
        # [0 0 1 0 0]
        # [0 0 0 1 1]
        # 4
        # BFS
        # Time: O(m * n) | Space: O(m * n)
        m, n = len(grid), len(grid[0])
        visited = set()  # visited cell (r, c)
        count = 0
        steps = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        def bfs(r: int, c: int) -> None:
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                r, c = queue.popleft()

                for stepR, stepC in steps:
                    nextR, nextC = r + stepR, c + stepC

                    if (
                        0 <= nextR < m and
                        0 <= nextC < n and
                        (nextR, nextC) not in visited and
                        grid[nextR][nextC] == '1'
                    ):
                        queue.append((nextR, nextC))
                        visited.add((nextR, nextC))

        for r in range(m):
            for c in range(n):
                if (r, c) not in visited and grid[r][c] == '1':
                    bfs(r, c)
                    count += 1

        return count
