class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # [
        #     [in -1  0 in]
        #     [in in in -1]
        #     [in -1 in -1]
        #     [ 0 -1 in in]
        # ]
        # Time: O(m * n) | Space: O(m * n)
        m, n = len(grid), len(grid[0])
        queue = deque([])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        inf = 2 ** 31 - 1
        visited = set()
        distance = 0

        while queue:
            count = len(queue)
            for i in range(count):
                r, c = queue.popleft()
                if (r, c) in visited:
                    continue

                visited.add((r, c))
                grid[r][c] = distance

                for stepR, stepC in steps:
                    nextR, nextC = r + stepR, c + stepC
                    if (
                        0 <= nextR < m and
                        0 <= nextC < n and
                        (nextR, nextC) not in visited and
                        grid[nextR][nextC] == inf
                    ):
                        queue.append((nextR, nextC))

            distance += 1
