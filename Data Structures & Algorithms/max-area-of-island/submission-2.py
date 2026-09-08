class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Time: O(m * n) | Space: O(m * n)
        m, n = len(grid), len(grid[0])
        visited = set()  # visited cells (r, c)
        steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        # Find are (BFS)
        def findArea(r: int, c: int) -> int:
            # Initialize queue with cell
            queue = deque([(r, c)])
            area = 0

            # Iterate until empty queue
            while queue:
                # Unqueue cell, add to area
                r, c = queue.popleft()
                area += grid[r][c]

                # Find neighbors -> add to queue, mark visited
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

            # Return area
            return area

        maxArea = 0
        # Iterate rows
        for r in range(m):
            # Iterate columns
            for c in range(n):
                # Found unvisited land -> find area
                if (r, c) not in visited and grid[r][c] == 1:
                    visited.add((r, c))
                    area = findArea(r, c)
                    # Compute max area
                    maxArea = max(maxArea, area)

        # Return max area
        return maxArea
