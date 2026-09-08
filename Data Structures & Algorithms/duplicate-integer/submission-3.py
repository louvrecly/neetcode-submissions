class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # [1, 2, 3, 3]
        # hash set {}
        # [1, 2, 3, 3]
        #  ^ hash set { 1 }
        #     ^ hash set { 1, 2 }
        #        ^ hash set { 1, 2, 3 }
        #           ^ hash set { 1, 2, 3 }
        # # Time: O(n) | Space: O(n)
        # numsSet = set()
        # for num in nums:
        #     if num in numsSet:
        #         return True
        #     numsSet.add(num)
        # return False
        # Time: O(n) | Space: O(n)
        return len(set(nums)) < len(nums)
