class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: O(n) | Space: O(n)
        numsSet = set(nums)
        maxLength = 0

        for num in numsSet:
            if num - 1 in numsSet:
                continue

            length = 1
            while num + length in numsSet:
                length += 1

            maxLength = max(maxLength, length)

        return maxLength
