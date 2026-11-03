class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Time: O(n * sum(nums)) | Space: O(n * sum(nums))
        n = len(nums)
        cache = {}  # mapping (i, diff) -> bool

        def dp(i: int, diff: int) -> bool:
            if (i, diff) in cache:
                return cache[(i, diff)]

            if diff < 0:
                cache[(i, diff)] = False
                return cache[(i, diff)]

            if i >= n:
                cache[(i, diff)] = diff == 0
                return cache[(i, diff)]

            cache[(i, diff)] = dp(i + 1, diff - 2 * nums[i]) or dp(i + 1, diff)
            return cache[(i, diff)]

        return dp(0, sum(nums))
