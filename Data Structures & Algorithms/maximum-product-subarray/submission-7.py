class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Time: O(n) | Space: O(1)
        window = [1, 1]
        max_prod = max(nums)

        for num in nums:
            prev_max, prev_min = window
            window[0] = max(num * prev_max, num * prev_min, num)
            window[1] = min(num * prev_max, num * prev_min, num)
            max_prod = max(window + [max_prod])

        return max_prod
