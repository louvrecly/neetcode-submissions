class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,4,5,6] | 7
        #  ^ [7 - 3 = 4]: 0 | {}
        #    ^ [7 - 4 = 3]: 1 | { 4: 0 } 
        # Time: O(n) | Space: O(n)
        candidates = {}
        for i in range(len(nums)):
            if nums[i] in candidates:
                return [candidates[nums[i]], i]
            difference = target - nums[i]
            candidates[difference] = i
        