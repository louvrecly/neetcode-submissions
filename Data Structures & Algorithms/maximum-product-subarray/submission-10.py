class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Time: O(2^n) | Space: O(2^n)
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]

        total = math.prod(nums)
        if total > 0:
            return total

        if total == 0:
            for i, num in enumerate(nums):
                if num == 0:
                    return max(
                        self.maxProduct(nums[:i]),
                        self.maxProduct(nums[i + 1:]),
                        0
                    )

        left, right = 0, n - 1
        while left < n and nums[left] > 0:
            left += 1

        while right >= 0 and nums[right] > 0:
            right -= 1

        return max(
            math.prod(nums[:left]),
            math.prod(nums[left + 1:]),
            math.prod(nums[:right]),
            math.prod(nums[right + 1:])
        )
