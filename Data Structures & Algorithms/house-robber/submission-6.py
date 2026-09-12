class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time: O(n) | Space: O(1)
        n = len(nums)
        memo1 = 0
        memo2 = nums[-1]

        for i in range(n - 2, -1, -1):
            temp = max(memo1 + nums[i], memo2)
            memo1, memo2 = memo2, temp

        return memo2
