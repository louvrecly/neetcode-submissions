class Solution:
    def checkValidString(self, s: str) -> bool:
        # Time: O(3^n) | Space: O(3^n)
        n = len(s)
        memo = {}  # mapping (i, open_count) -> valid

        def dp(i: int, open_count: int) -> bool:
            if (i, open_count) in memo:
                return memo[(i, open_count)]

            if i == n:
                return open_count == 0

            if s[i] == "(":
                memo[(i, open_count)] = dp(i + 1, open_count + 1)
                return memo[(i, open_count)]

            if s[i] == ")":
                memo[(i, open_count)] = open_count >= 1 and dp(i + 1, open_count - 1)
                return memo[(i, open_count)]

            memo[(i, open_count)] = (
                dp(i + 1, open_count + 1) or  # * as (
                dp(i + 1, open_count) or      # * as empty
                dp(i + 1, open_count - 1)     # * as )
            )
            return memo[(i, open_count)]

        return dp(0, 0)
