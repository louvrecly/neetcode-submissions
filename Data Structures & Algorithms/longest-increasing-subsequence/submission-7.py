class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [0 3 1 3 2 3]
        #            ^ | [3] -> 1
        #          ^ | [2] vs [2 3] -> 2
        #        ^ | [3] -> 1
        #      ^ | [1] vs [1 3] vs [1 2 3] vs [1 3] -> 3
        #    ^ | [3] -> 1
        #  ^ | [0] vs [0 1 2 3] vs [0 3] vs [0 2 3] vs [0 3] -> 4
        # dp(i) = (
        #     dp(i) if nums[i] >= nums[j] else
        #     max(dp(i), 1 + dp(j)) for j in range(i + 1, n)
        # )
        # Time: O(n^2) | Space: O(1)
        n = len(nums)
        dp = [1] * n

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
