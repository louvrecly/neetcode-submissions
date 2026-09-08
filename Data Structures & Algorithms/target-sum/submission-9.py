class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # [0 1 1 2] | t: 0
        # [0 +1 +1 -2]
        # [0 -1 -1 +2]
        #            0
        #            |
        #            0
        #       /         \
        #      1          -1
        #    /   \       /   \
        #   2     1     0    -2
        #  / \   / \   / \   / \
        # 4   0 3  -1 2  -2 0  -4
        #     *             *
        # dp(i, t) = dp(i + 1, t - nums[i]) + dp(i + 1, t + nums[i])
        # Time: O(n * target) | Space: O(n * target)
        n = len(nums)
        memo = {}

        def dp(i: int, t: int) -> int:
            if (i, t) in memo:
                return memo[(i, t)]

            if i == n:
                memo[(i, t)] = 1 if t == 0 else 0
                return memo[(i, t)]

            num = nums[i]
            memo[(i, t)] = dp(i + 1, t - num) + dp(i + 1, t + num)
            return memo[(i, t)]

        return dp(0, target)
