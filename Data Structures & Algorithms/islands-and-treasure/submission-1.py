class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # [in  0 -1 in]
        # [in in in in]
        # [-1 in -1 in]
        # [in in -1  0]
        # ===============
        # [in  0 -1 in]
        # [in in in in]
        # [-1 in -1 in]
        # [in in -1  0]
        # =============== q: [(0 1) (3 3)] | s: 0
        # [in  0 -1 in]
        # [in in in in]
        # [-1 in -1 in]
        # [in in -1  0]
        # =============== q: [(0 0) (1 1) (2 3)] | s: 1
        # [ 1  0 -1 in]
        # [in  1 in in]
        # [-1 in -1  1]
        # [in in -1  0]
        # =============== q: [(1 0) (1 2) (2 1) (1 3)] | s: 2
        # [ 1  0 -1 in]
        # [ 2  1  2  2]
        # [-1  2 -1  1]
        # [in in -1  0]
        # =============== q: [(3 1) (0 3)] | s: 3
        # [ 1  0 -1  3]
        # [ 2  1  2  2]
        # [-1  2 -1  1]
        # [in  3 -1  0]
        # =============== q: [(3 0)] | s: 4
        # [ 1  0 -1  3]
        # [ 2  1  2  2]
        # [-1  2 -1  1]
        # [ 4  3 -1  0]
        # =============== q: [] | s: 5
        # Time: O(m * n) | Space: O(m * n)
        m, n = len(grid), len(grid[0])
        queue = deque()
        visited = set()  # visited cells (r, c)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        distance = 0
        inf = 2 ** 31 - 1
        steps = [(0, -1), (-1, 0), (0, 1), (1, 0)]
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
