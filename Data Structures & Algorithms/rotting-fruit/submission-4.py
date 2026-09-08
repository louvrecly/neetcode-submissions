class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Iterate through the grid
        # Count fresh
        # Push rotten to queue
        # Iterate through queue
        # 1) Extract option -> Mark visited
        #   i) 1 -> fresh count -= 1
        #   ii) 2 -> 
        # 2) Find neighbors via BFS -> Add to queue
        # Check fresh count
        m, n = len(grid), len(grid[0])
        freshCount = 0
        queue = deque()  # node (r, c)
        visited = set()  # visited node (r, c)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    freshCount += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))

        steps = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        level = 0
        while queue and freshCount > 0:
            level += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                for stepR, stepC in steps:
                    nextR, nextC = r + stepR, c + stepC
                    if (
                        0 <= nextR < m and
                        0 <= nextC < n and
                        (nextR, nextC) not in visited and
                        grid[nextR][nextC] == 1
                    ):
                        queue.append((nextR, nextC))
                        visited.add((nextR, nextC))
                        freshCount -= 1
                    
        return level if freshCount == 0 else -1
        # # Time: O(m * n) | Space: O(m * n)
        # m, n = len(grid), len(grid[0])
        # freshCount = 0
        # queue = deque()  # (row, col, time)

        # for r in range(m):
        #     for c in range(n):
        #         if grid[r][c] == 1:
        #             freshCount += 1
        #         elif grid[r][c] == 2:
        #             queue.append((r, c, 0))

        # visited = set()  # Visited cell (r, c)
        # steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        # maxTime = 0
        # while queue:
        #     r, c, time = queue.popleft()
        #     if (r, c) not in visited and grid[r][c] == 1:
        #         freshCount -= 1
        #         time += 1
        #     visited.add((r, c))
        #     maxTime = max(maxTime, time)
        #     for stepR, stepC in steps:
        #         nextR, nextC = r + stepR, c + stepC
        #         if (
        #             0 <= nextR < m and
        #             0 <= nextC < n and
        #             (nextR, nextC) not in visited and
        #             grid[nextR][nextC] == 1
        #         ):
        #             queue.append((nextR, nextC, time))
        # return maxTime if freshCount == 0 else -1
