class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Time: O(2 ^ (n * sum(nums))) | Space: O(2 ^ (n * sum(nums)))
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        n = len(nums)

        def dp(i: int, curr: int) -> bool:
            if curr > target:
                return False

            if curr == target:
                return True

            if i >= n:
                return False

            return dp(i + 1, curr + nums[i]) or dp(i + 1, curr)

        return dp(0, 0)
