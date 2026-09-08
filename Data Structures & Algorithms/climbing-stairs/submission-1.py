class Solution:
    def climbStairs(self, n: int) -> int:
        # n: 2
        # [1 1]
        # [2]
        # c: 2
        # ==========
        # n: 3
        # [1 1 1]
        # [1 2]
        # [2 1]
        # c: 4
        # ==========
        # n: 4
        # [1 1 1 1]
        # [1 1 2]
        # [1 2 1]
        # [2 1 1]
        # [2 2]
        # c: 5
        # ==========
        #                [ ]
        #            /         \
        #          [1]         [2]
        #          / \         /
        #      [1 1] [1 2] [2 1]
        #       /
        # [1 1 1]
        # DP[i] = DP[i - 1] + DP[i - 2]
        # Time: O(n) | Space: O(n)
        memo = {1: 1, 2: 2}

        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n]
