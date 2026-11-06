class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # n: [-1 0 2 4 6 8] | t: 5
        # [-1 0 2 4 6 8]
        #   L   M     R | 2 < 5
        #       L M   R | 4 < 5
        #         L M R | 6 > 5
        #        LM R   | 4 < 5
        # Time: O(log n) | Space: O(1)
        n = len(nums)
        if nums[-1] < target:
            return n

        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid

        return right
