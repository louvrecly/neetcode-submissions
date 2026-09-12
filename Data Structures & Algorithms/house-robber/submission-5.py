class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time: O(n) | Space: O(n)
        n = len(nums)
        memo = [0] * (n + 1)
        memo[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            memo[i] = max(memo[i + 2] + nums[i], memo[i + 1])

        return memo[0]
