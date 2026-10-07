class Solution:
    def numDecodings(self, s: str) -> int:
        # s: 12
        # 1-2 -> AB
        # 12 -> L
        # s: 01
        # take 1 vs 2
        # s: 123201
        #                                           [ ]
        #                           /                                  \
        #                         [1]                                  [12]
        #                   /             \                             / \
        #               [1-2]             [1-23]                   [12-3] [-]
        #                / \             /       \                /       \
        #          [1-2-3] [-]    [1-23-2]       [1-23-20] [12-3-2]       [12-3-20]
        #         /       \            / \             / \      / \             / \
        # [1-2-3-2]       [1-2-3-20] [-] [-] [1-23-20-1] [-]  [-] [-] [12-3-20-1] [-]
        #    / \              / \
        #  [-] [-] [1-2-3-20-1] [-]
        # Dynamic Programming - Knapsack 0/1
        # dp(i) = dp(i + 1) + dp(i + 2)
        # Time: O(2^n) | Space: O(2^n)
        def is_valid(char: str) -> bool:
            if not char.isdigit() or char[0] == '0':
                return False
            return 1 <= int(char) <= 26

        n = len(s)
        memo = {}  # Mapping i -> count
        def dp(i: int) -> int:
            if i in memo:
                return memo[i]

            if i == n:
                return 1

            if i == n - 1:
                return 1 if is_valid(s[i]) else 0

            count = 0
            if is_valid(s[i]):
                count += dp(i + 1)
            if is_valid(s[i:i+2]):
                count += dp(i + 2)

            memo[i] = count
            return memo[i]

        return dp(0)
