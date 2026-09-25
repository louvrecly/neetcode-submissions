class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time: O(log n) | Space: O(1)
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        smallest = left
        left, right = 0, smallest - 1

        if target <= nums[n - 1]:
            left, right = smallest, n - 1

        while left <= right:
            if nums[left] == target:
                return left

            if nums[right] == target:
                return right

            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1
