class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Time: O(n) | Space: O(n)
        numsSet = set()
        for num in nums:
            if num in numsSet:
                return True
            numsSet.add(num)
        return False