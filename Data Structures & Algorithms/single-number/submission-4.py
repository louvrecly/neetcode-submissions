class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Time: O(n) | Space: O(1)
        result = 0
        for num in nums:
            result ^= num
        return result
