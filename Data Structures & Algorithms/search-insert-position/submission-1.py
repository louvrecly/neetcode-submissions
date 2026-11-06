class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Time: O(log n) | Space: O(1)
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return left
