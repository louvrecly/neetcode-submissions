class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2 9 8 3 6]
        #               0
        #      2 /             \
        #       2               0
        #   8 /   \      9 /         \
        #    8     2      9           0
        # 6 / \ 3 / \  3 / \      8 /   \
        # 14   8 5   2 12   9      8     0
        #         6 / \  6 / \  6 / \ 3 / \
        #          8   2 15   9 14   8 3   0
        #                               6 / \
        #                                6   0
        # dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        # Time: O(n) | Space: O(n)
        n = len(nums)
        memo = {}

        def dp(i: int) -> int:
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(dp(i + 2) + nums[i], dp(i + 1))
            return memo[i]

        return dp(0)
