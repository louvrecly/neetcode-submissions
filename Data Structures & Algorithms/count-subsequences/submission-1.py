class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # s: caaat | t: cat
        # c a a a t
        # ^ ^     ^ | cat
        # ^   ^   ^ | cat
        # ^     ^ ^ | cat
        # s: xxyxy | t: xy
        # x x y x y
        # ^   ^     | xy
        # ^       ^ | xy
        #   ^ ^     | xy
        #   ^     ^ | xy
        #       ^ ^ | xy
        # s: xxyxy | t: xy
        # x x y x y
        # knapsack 0/1
        #           [ ]
        #     /             \
        #   [x]             [ ]
        #   / \          /        \
        # [-] [x]      [x]        [ ]
        #     / \      / \     /        \
        #  [xy] [x] [xy] [x] [-]        [ ]
        #       / \      / \          /     \
        #     [-] [x]  [-] [x]      [x]     [ ]
        #         / \      / \      / \     / \
        #      [xy] [-] [xy] [-] [xy] [-] [-] [-]
        # dp(i, j) = dp(i + 1, j) + dp(i + 1, j + 1)
        # Time: O(mn) | Space: O(mn)
        m, n = len(s), len(t)
        if m < n:
            return 0

        memo = {}  # Mapping (i, j) -> count
        def dp(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]

            if j >= n:
                memo[(i, j)] = 1
                return memo[(i, j)]

            if i >= m:
                memo[(i, j)] = 0
                return memo[(i, j)]

            count = dp(i + 1, j)
            if s[i] == t[j]:
                count += dp(i + 1, j + 1)

            memo[(i, j)] = count
            return memo[(i, j)]

        return dp(0, 0)
