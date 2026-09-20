class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Time: O(mn log mn) | Space: O(mn)
        m, n = len(matrix), len(matrix[0])
        items = []  # tuple (value, r, c)

        for r in range(m):
            for c in range(n):
                items.append((matrix[r][c], r, c))

        items.sort(reverse=True)
        dp = [[0] * n for _ in range(m)]
        steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        maxPath = 0

        for value, r, c in items:
            path = 1
            for stepR, stepC in steps:
                nextR, nextC = r + stepR, c + stepC
                if (
                    0 <= nextR < m and
                    0 <= nextC < n and
                    matrix[r][c] < matrix[nextR][nextC]
                ):
                    path = max(path, 1 + dp[nextR][nextC])

            dp[r][c] = path
            maxPath = max(maxPath, path)

        return maxPath
