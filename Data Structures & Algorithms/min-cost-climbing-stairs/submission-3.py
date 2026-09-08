class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [1 2 3]
        #  0 1 2 3
        #                [ ]
        #           /           \
        #         [0]           [1]
        #       /     \         / \
        #     [1]     [2]     [2] [3]
        #     / \     / \     / \
        #   [2] [3] [3] [4] [3] [4]
        #   / \
        # [3] [4]
        # dp(i) = cost[i] + min(dp(i + 1), dp(i + 2))
        # dp(3) = 0 + min(0, 0) = 0
        # dp(2) = 3 + min(0, 0) = 3
        # dp(1) = 2 + min(3, 0) = 2
        # dp(0) = 1 + min(2, 3) = 3
        # minCost = min(dp(0), dp(1)) = min(3, 2) = 2
        # DP with immutability
        # Time: O(n) | Space: O(n)
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2] if i + 2 <= n else 0)

        return min(dp[0], dp[1])
