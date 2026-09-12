class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp(i, noLast) = max(dp(i + 2, noLast), dp(i + 1))
        # Time: O(n) | Space: O(n)
        n = len(nums)
        memo = {}

        def dp(i: int, noLast: bool=False) -> int:
            if i >= n:
                return 0

            if noLast and i >= n - 1:
                return 0

            if (i, int(noLast)) in memo:
                return memo[(i, int(noLast))]

            memo[(i, int(noLast))] = max(
                dp(i + 2, True if i == 0 else noLast) + nums[i],
                dp(i + 1, noLast)
            )

            return memo[(i, int(noLast))]

        return dp(0)
