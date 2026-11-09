class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Sliding Window (Same direction)
        # Time: O(n) | Space: O(k)
        n = len(nums)
        nums_set = set()
        left = 0

        for right in range(n):
            if right - left > k:
                nums_set.remove(nums[left])
                left += 1

            if nums[right] in nums_set:
                return True

            nums_set.add(nums[right])

        return False
