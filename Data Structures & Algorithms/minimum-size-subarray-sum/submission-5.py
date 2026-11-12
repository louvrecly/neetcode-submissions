class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Time: O(n * target) | Space: O(n)
        n = len(nums)
        prefix_sums = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

        left = 0
        min_length = 0

        for right in range(n):
            left = 0 if min_length == 0 else right - min_length + 1
            subtotal = prefix_sums[right + 1] - prefix_sums[left]

            while subtotal >= target:
                if not min_length:
                    min_length = right - left + 1
                else:
                    min_length = min(min_length, right - left + 1)

                subtotal -= nums[left]
                left += 1

        return min_length
