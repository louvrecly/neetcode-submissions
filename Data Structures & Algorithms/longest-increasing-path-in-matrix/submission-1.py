class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # [
        #     [3 2 3]
        #     [5 1 4]
        #     [7 6 5]
        # ]
        # DFS: dfs(r, c) = 1 + max(
        #     dfs(r + 1, c),
        #     dfs(r, c + 1),
        #     dfs(r - 1, c),
        #     dfs(r, c - 1)
        # )
        # Time: O((mn)^2) | Space: O(mn)
        m, n = len(matrix), len(matrix[0])
        steps = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        memo = {}  # Mapping (r, c) -> path

        def dfs(r: int, c: int) -> int:
            if (r, c) in memo:
                return memo[(r, c)]
            nextPath = 0
            for stepR, stepC in steps:
                nextR, nextC = r + stepR, c + stepC
                if (
                    0 <= nextR < m and
                    0 <= nextC < n and
                    matrix[nextR][nextC] > matrix[r][c]
                ):
                    nextPath = max(nextPath, dfs(nextR, nextC))
            memo[(r, c)] = nextPath + 1
            return memo[(r, c)]

        maxPath = 0
        for r in range(m):
            for c in range(n):
                maxPath = max(maxPath, dfs(r, c))

        return maxPath
