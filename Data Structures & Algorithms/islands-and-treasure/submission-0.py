class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # [
        #   [ 0,-1],
        #   [IN,IN]
        # ]
        # ===========
        # [ 0 -1]
        # [IN IN]
        # ===========
        # [ 0 -1]
        # [ 1 IN]
        # ===========
        # Time: O(m * n) | Space: O(m * n)
        m, n = len(grid), len(grid[0])
        queue = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c))

        steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()
        distance = 0
        inf = 2 ** 31 - 1
        while queue:
            length = len(queue)
            for _ in range(length):
                r, c = queue.popleft()
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
                        visited.add((nextR, nextC))

            distance += 1
