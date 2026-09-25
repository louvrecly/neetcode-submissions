class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3 4 5 6 1 2] | t: 1
        #  L   M     R | m: 5 > 1 | m > r
        #        L M R | m: 1
        # Binary Search
        # Time: O(log n) | Space: O(1)
        n = len(nums)
        left, right = 0, n - 1

        # if nums[left] == target:
        #     return left
        # if nums[right] == target:
        #     return right

        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            mid = (left + right) // 2
            print('=' * 5)
            print(f"nums[{left}]: {nums[left]} | nums[{mid}]: {nums[mid]} | nums[{right}]: {nums[right]}")
            ordered = nums[left] <= nums[right]
            print(f"ordered: {ordered}")
            if nums[mid] > target:
                if ordered:
                    right = mid - 1
                    print(f"right: {right}")
                    # if nums[right] == target:
                    #     return right
                # l m r | t < m | r < l
                # r < l <= t < m or t <= r < l < m or t < m < r < l
                # r = m - 1 or l = m + 1 or r = m - 1
                elif target <= nums[right] < nums[left] < nums[mid]:
                    left = mid + 1
                    print(f"left: {left}")
                    # if nums[left] == target:
                    #     return left
                else:
                    right = mid - 1
                    print(f"right: {right}")
                    # if nums[right] == target:
                    #     return right
            elif nums[mid] < target:
                if ordered:
                    left = mid + 1
                    print(f"left: {left}")
                    # if nums[left] == target:
                    #     return left
                # l m r | m < t | r < l
                # m < t <= r < l or m < r < l <= t or r < l < m < t
                # l = m + 1 or r = m - 1 or l = m + 1
                elif nums[mid] < nums[right] < nums[left] <= target:
                    right = mid - 1
                    print(f"right: {right}")
                    # if nums[right] == target:
                    #     return right
                else:
                    left = mid + 1
                    print(f"left: {left}")
                    # if nums[left] == target:
                    #     return left
            else:
                print(f"mid: {mid}")
                return mid

        return -1