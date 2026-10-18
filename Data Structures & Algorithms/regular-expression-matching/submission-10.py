class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # s: aab | p: c*a*b
        # Time: O(m^ij) | Space: O(m^ji)
        m, n = len(s), len(p)
        memo = {}

        def dp(i: int, j: int) -> bool:
            if i < 0 and j < 0:
                return True

            if i < 0:
                return j % 2 == 1 and p[j] == '*' and dp(i, j - 2)

            if j < 0:
                return False

            if (i, j) in memo:
                return memo[(i, j)]

            if p[j] == '*':
                # Compare s[:i+1] vs p[j-1:j+1]
                if j <= 0:
                    memo[(i, j)] = False
                    return memo[(i, j)]

                if p[j - 1] == '.':
                    memo[(i, j)] = any(dp(i - k, j - 2) for k in range(i + 2))
                    return memo[(i, j)]

                x = 0
                while x <= i and s[i - x] == p[j - 1]:
                    x += 1
                memo[(i, j)] = any(dp(i - k, j - 2) for k in range(x + 1))
                return memo[(i, j)]

            if p[j] == '.':
                memo[(i, j)] = dp(i - 1, j - 1)
                return memo[(i, j)]

            memo[(i, j)] = s[i] == p[j] and dp(i - 1, j - 1)
            return memo[(i, j)]

        return dp(m - 1, n - 1)
