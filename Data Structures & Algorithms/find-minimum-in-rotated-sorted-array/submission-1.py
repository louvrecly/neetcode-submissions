class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3 4 5 6 1 2]
        # sort: [1 2 3 4 5 6] | min: 1
        # [4 5 0 1 2 3]
        # sort: [0 1 2 3 4 5] | min: 0
        # nums[0] vs nums[-1] -> rotated ?
        # binary search
        # |       X
        # |     X X
        # |   X X X
        # | X X X X
        # | X X X X   X
        # | X X X X X X
        # +-------------
        # Time: O(log n) | Space: O(1)
        if nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1
        minNum = nums[right]

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                left = mid
            else:
                minNum = min(minNum, nums[mid])
                right = mid
        
        return minNum
      