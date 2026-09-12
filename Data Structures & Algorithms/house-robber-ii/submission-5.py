class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp(i, noLast) = max(dp(i + 2, noLast), dp(i + 1))
        # Time: O(n) | Space: O(n)
        n = len(nums)
        memo = [[None] * n for _ in range(2)]

        def dp(i: int, noLast: int=0) -> int:
            if i >= n:
                return 0

            if noLast and i >= n - 1:
                return 0

            if memo[noLast][i] is not None:
                return memo[noLast][i]

            memo[noLast][i] = max(
                dp(i + 2, 1 if i == 0 else noLast) + nums[i],
                dp(i + 1, noLast)
            )

            return memo[noLast][i]

        return dp(0)
