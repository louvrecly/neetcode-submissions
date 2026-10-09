class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp(i, j) = dp(i + 1, j) + (dp(i + 1, j + 1) if s[i] == t[j] else 0)
        # s: xxyxy | t: xy
        # x x y x y | x y
        #         ^   ^   | x != y | 0
        #         ^     ^ | y == y | 1
        # Time: O(mn) | Space: O(n)
        m, n = len(s), len(t)
        memo = [1 if i == n else 0 for i in range(n + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n):
                if s[i] == t[j]:
                    memo[j] += memo[j + 1]

        return memo[0]
