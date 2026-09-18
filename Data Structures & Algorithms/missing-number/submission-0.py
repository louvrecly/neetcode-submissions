class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # [1 0 3] | n: 3
        # set: {0 1 3}
        # Binary Search [0 n]
        # Time: O(n) | Space: O(n)
        n = len(nums)
        numsSet = set([num for num in nums])
        for num in range(n + 1):
            if num not in numsSet:
                return num
