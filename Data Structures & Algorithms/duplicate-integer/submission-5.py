class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # [1,2,3,3]
        #  ^ {}
        # [1,2,3,3]
        #    ^ { 1 }
        # [1,2,3,3]
        #      ^ { 1, 2 }
        # [1,2,3,3]
        #        ^ { 1, 2, 3 } -> Duplicate
        # Time: O(n) | Space: O(n)
        numsSet = set()
        for num in nums:
            if num in numsSet:
                return True
            numsSet.add(num)
        return False
        
