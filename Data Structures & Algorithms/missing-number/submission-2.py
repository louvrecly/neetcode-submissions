class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum of arithmetic sequence = n * (n + 1) // 2
        # Time: O(n) | Space: O(1)
        n = len(nums)
        seqSum = n * (n + 1) // 2
        return seqSum - sum(nums)
        