class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # w1: acb | w2: ab
        #       j
        #     0 1 2
        #   0     3
        #   1     2
        # i 2     1
        #   3 2 1 0
        # dp(i, j) = (
        #     0 if i >= m and j >= n else
        #     n - j if i >= m else
        #     m - i if j >= n else
        #     dp(i + 1, j + 1) if word1[i] == word2[j] else
        #     1 + min(
        #         dp(i + 1, j),  # delete
        #         dp(i, j + 1),  # insert
        #         dp(i + 1, j + 1)  # replace
        #     )
        # )
        # Time: O(mn) | Space: O(mn)
        m, n = len(word1), len(word2)
        memo = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            memo[i][n] = m - i

        for j in range(n + 1):
            memo[m][j] = n - j

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    memo[i][j] = memo[i + 1][j + 1]
                else:
                    memo[i][j] = 1 + min(
                        memo[i + 1][j],
                        memo[i][j + 1],
                        memo[i + 1][j + 1]
                    )

        return memo[0][0]
