class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # lengths[i] = max(lengths[i], 1 + lengths[j]) if nums[i] > nums[j] else lengths[i]
        # Time: O(n^2) | Space: O(n)
        n = len(nums)
        lengths = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lengths[i] = max(lengths[i], 1 + lengths[j])

        return max(lengths)
