class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # w1: monkeys | w2: money
        # monkeys | remove k at 3
        # moneys | remove s at 5
        # money
        # w1: neatcdee | w2: neetcode
        # neatcdee | replace a with e at 2
        # neetcdee | insert o at 5
        # neetcodee | remove e at 7
        # neetcode
        # dp(i, j)
        # -> match w1[i] == w2[j] -> dp(i + 1, j + 1)
        # -> mismatch w1[i] != w2[j]
        #     min(
        #         dp(i, j + 1),  # insert
        #         dp(i + 1, j),  # delete
        #         dp(i + 1, j + 1),  # replace
        #     )
        # base cases
        # i out-of-bound -> count + n - j
        # j out-of-bound -> count + m - i
        # Time: O(mn) | Space: O(mn)
        m, n = len(word1), len(word2)
        memo = {}  # Mapping (i, j) -> edits

        def dp(i: int, j: int) -> int:
            if i >= m and j >= n:
                return 0

            if i >= m:
                return n - j

            if j >= n:
                return m - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = 1 + min(
                dp(i, j + 1),
                dp(i + 1, j),
                dp(i + 1, j + 1)
            )
            return memo[(i, j)]

        return dp(0, 0)
