class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Time: O((mn)^2) | Space: O(mn)
        m, n = len(matrix), len(matrix[0])
        steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        memo = [[0] * n for _ in range(m)]

        def dfs(r: int, c: int) -> int:
            if memo[r][c] > 0:
                return memo[r][c]

            nextPath = 0
            for stepR, stepC in steps:
                nextR, nextC = r + stepR, c + stepC
                if (
                    0 <= nextR < m and
                    0 <= nextC < n and
                    matrix[nextR][nextC] > matrix[r][c]
                ):
                    nextPath = max(nextPath, dfs(nextR, nextC))
            memo[r][c] = nextPath + 1
            return memo[r][c]

        maxPath = 0
        for r in range(m):
            for c in range(n):
                maxPath = max(maxPath, dfs(r, c))

        return maxPath
