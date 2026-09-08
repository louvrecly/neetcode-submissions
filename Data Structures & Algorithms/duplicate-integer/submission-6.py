class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Time: O(n) | Space: O(n)
        return len(set(nums)) < len(nums)