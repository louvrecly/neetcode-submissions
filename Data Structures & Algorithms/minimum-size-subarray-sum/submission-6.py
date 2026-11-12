class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding Window (Same Direction)
        # Time: O(n) | Space: O(1)
        n = len(nums)
        left, right = 0, 0
        subtotal = 0
        min_length = float('inf')

        while right < n:
            while right < n and subtotal < target:
                subtotal += nums[right]
                right += 1

            while left < right and subtotal >= target:
                min_length = min(min_length, right - left)
                subtotal -= nums[left]
                left += 1

        return min_length if min_length < float('inf') else 0
