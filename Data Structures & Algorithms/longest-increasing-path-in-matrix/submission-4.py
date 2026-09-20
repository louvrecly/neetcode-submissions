class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Time: O(mn log mn) | Space: O(mn)
        m, n = len(matrix), len(matrix[0])
        maxHeap = []

        for r in range(m):
            for c in range(n):
                heapq.heappush_max(maxHeap, (matrix[r][c], r, c))

        dp = [[0] * n for _ in range(m)]
        steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        maxPath = 0

        while maxHeap:
            value, r, c = heapq.heappop_max(maxHeap)
            path = 1

            for stepR, stepC in steps:
                nextR, nextC = r + stepR, c + stepC
                if (
                    0 <= nextR < m and
                    0 <= nextC < n and
                    matrix[nextR][nextC] > value
                ):
                    path = max(path, 1 + dp[nextR][nextC])

            dp[r][c] = path
            maxPath = max(maxPath, path)

        return maxPath
