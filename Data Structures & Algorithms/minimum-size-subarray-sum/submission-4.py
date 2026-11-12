class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Time: O(n^2) | Space: O(1)
        n = len(nums)
        left = 0
        min_length = 0

        for right in range(n):
            left = 0 if min_length == 0 else right - min_length + 1
            subtotal = sum(nums[left:right + 1])

            while subtotal >= target:
                if not min_length:
                    min_length = right - left + 1
                else:
                    min_length = min(min_length, right - left + 1)

                subtotal -= nums[left]
                left += 1

        return min_length
