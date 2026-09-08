class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [-1 0 2 4 6 8] | t: 4
        #         ^      | 3
        # [-1 0 2 4 6 8] | t: 3
        #                | -1
        # Binary Search
        # [-1 0 2 4 6 8] | t: 4
        #   L   M     R  | 2 < 4
        #       L M   R  | 4 = 4 | 3
        # Time: O(log n) | Space: O(1)
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]
            if num > target:
                right = mid - 1
            elif num < target:
                left = mid + 1
            else:
                return mid

        return -1
