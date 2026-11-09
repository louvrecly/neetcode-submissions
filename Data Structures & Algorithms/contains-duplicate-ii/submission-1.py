class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Time: O(n^2) | Space: O(1)
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True

        return False
