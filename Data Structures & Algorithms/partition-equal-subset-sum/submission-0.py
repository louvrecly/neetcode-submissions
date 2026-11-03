class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # nums: [1 2 3 4]
        # [1 4] = [2 3] = 5 | True
        # nums: [1 2 3 4 5]
        # [1 2 5] = 8 vs [3 4] = 7
        # [1 3 4] = 8 vs [2 5] = 7 | False
        # dp(i, a) = dp(i + 1, a - 2 * nums[i]) or dp(i + 1, a)
        # Time: O(2 ^ (n * sum(nums))) | Space: O(2 ^ (n * sum(nums)))
        n = len(nums)

        def dp(i: int, diff: int) -> bool:
            if diff < 0:
                print(False)
                return False

            if i >= n:
                return diff == 0

            return dp(i + 1, diff - 2 * nums[i]) or dp(i + 1, diff)

        return dp(0, sum(nums))
