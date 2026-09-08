class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # [0 1 0 1]
        # [0 0 1 0]
        # [0 1 1 0]
        # [0 0 1 0]
        # =========
        # [x 1 0 1]
        # [0 0 1 0]
        # [0 1 1 0]
        # [0 0 1 0]
        # ========= l: 1 | opt: [rd(1,1), d(1, 0)]
        # [x 1 0 1]
        # [0 x 1 0]
        # [0 1 1 0]
        # [0 0 1 0]
        # ========= l: 2 | opt: [ru(-1,1), ld(1, -1)]
        # [x 1 0 1]
        # [0 x 1 0]
        # [0 1 1 0]
        # [0 0 1 0]
        # ========= l: 2 | opt: [ru(-1,1), ld(1, -1)]
        # [0,1,0,1,0]
        # [1,0,0,0,1]
        # [0,0,1,1,1]
        # [0,0,0,0,0]
        # [1,0,1,0,0]
        # BFS with queue
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        n = len(grid)
        minLength = [float('inf')]

        def bfs(r: int, c: int, length: int, visited: Set[Tuple[int, int]]) -> None:
            visited.add((r, c))

            if r == n - 1 and c == n - 1:
                minLength[0] = min(minLength[0], length + 1)
                return

            options = deque()

            def checkInRange(r: int, c: int) -> bool:
                return r >= 0 and r < n and c >= 0 and c < n

            def checkVisited(r: int, c: int) -> bool:
                return (r, c) in visited

            def checkIsOption(r: int, c: int) -> bool:
                return checkInRange(r, c) and grid[r][c] == 0 and not checkVisited(r, c)

            # down, right
            if checkIsOption(r + 1, c + 1):
                options.append((r + 1, c + 1))
            # down
            if checkIsOption(r + 1, c):
                options.append((r + 1, c))
            # right
            if checkIsOption(r, c + 1):
                options.append((r, c + 1))

            # up, right
            if checkIsOption(r - 1, c + 1):
                options.append((r - 1, c + 1))
            # down, left
            if checkIsOption(r + 1, c - 1):
                options.append((r + 1, c - 1))

            # up
            if checkIsOption(r - 1, c):
                options.append((r - 1, c))
            # left
            if checkIsOption(r, c - 1):
                options.append((r, c - 1))
            # up, left
            if checkIsOption(r - 1, c - 1):
                options.append((r - 1, c - 1))

            print(f"options: {options}")
            while options:
                r1, c1 = options.popleft()
                bfs(r1, c1, length + 1, visited)

        bfs(0, 0, 0, set())
        return minLength[0] if minLength[0] < float('inf') else -1