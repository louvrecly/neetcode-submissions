class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # [1 0 3]
        # 3 0011 ^ 0011 = 0000
        # 2 0010 ^ 0010 = 0000
        # 1 0001
        # 0 0000 ^ 0000 = 0000
        # Time: O(n) | Space: O(1)
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
