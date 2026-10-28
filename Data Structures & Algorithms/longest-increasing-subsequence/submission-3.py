class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Time: O(n^2) | Space: O(n^2)
        n = len(nums)
        lengths = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lengths[i] = max(lengths[i], 1 + lengths[j])

        return max(lengths)
