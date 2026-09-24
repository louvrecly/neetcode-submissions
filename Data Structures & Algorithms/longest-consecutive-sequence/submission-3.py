class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2 20 4 10 3 4 5]
        # sorted: [2 3 4 4 5 10 20]
        #          LR | l: 2 p: 2 r: 2 | l: 1 | m: 1
        #          L R | l: 2 p: 2 r: 3 | l: 2 | m: 2
        #          L   R | l: 2 p: 3 r: 4 | l: 3 | m: 3
        #          L     R | l: 2 p: 3 r: 4 | l: 3 | m: 3
        #          L       R | l: 2 p: 4 r: 5 | l: 4 | m: 4
        #          L          R | l: 2 p: 5 r: 10 | l: 1 | m: 4
        #                     LR | l: 10 p: 10 r: 10 | l: 1 | m: 4
        #                     L   R | l: 10 p: 10 r: 20 | l: 1 | m: 4
        #                         LR | l: 20 p: 20 r: 20 | l: 1 | m: 4
        # Time: O(n log n) | Space: O(1)
        nums.sort()
        n = len(nums)
        left, right = 0, 0
        last = 0
        maxLength = 0

        while left <= right < n:
            if nums[right] - nums[last] > 1:
                left, last = right, right
                continue
            maxLength = max(maxLength, nums[right] - nums[left] + 1)
            last = right
            right += 1

        return maxLength
