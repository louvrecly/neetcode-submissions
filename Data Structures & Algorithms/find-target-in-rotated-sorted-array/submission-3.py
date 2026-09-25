class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3 4 5 6 1 2] | t: 1
        #  L   M     R | m: 5 > 1 | m > r
        #        L M R | m: 1
        # Binary Search
        # Time: O(log n) | Space: O(1)
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right

            mid = (left + right) // 2
            ordered = nums[left] <= nums[right]
            if nums[mid] > target:
                if ordered:
                    right = mid - 1
                # l m r | t < m | r < l
                # r < l <= t < m or t <= r < l < m or t < m < r < l
                # r = m - 1 or l = m + 1 or r = m - 1
                elif target <= nums[right] < nums[left] < nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] < target:
                if ordered:
                    left = mid + 1
                # l m r | m < t | r < l
                # m < t <= r < l or m < r < l <= t or r < l < m < t
                # l = m + 1 or r = m - 1 or l = m + 1
                elif nums[mid] < nums[right] < nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                return mid

        return -1