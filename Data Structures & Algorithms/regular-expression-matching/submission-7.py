class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # s: aab | p: c*a*b
        #    ^        ^ | a != c or a == c*
        #     ^         ^ | a == a or a == a*
        #       ^         ^ | b == b
        # dp(i, j) = (
        #     False if p[j] == '*' else
        #     s[i] vs p[j:j+2] and dp(i + 1, j + 2) if j < n - 1 and p[j + 1] == * else
        #     s[i] vs p[j] and dp(i + 1, j + 1)
        # )
        # Time: O(ij) | Space: O(ij)
        m, n = len(s), len(p)
        memo = {}  # Mapping (i, j) -> is_match

        def dp(i: int, j: int) -> bool:
            if i >= m and j >= n:
                return True

            if i >= m:
                return (n - j) % 2 == 0 and p[j + 1] == '*' and dp(i, j + 2)

            if j >= n:
                return False

            if (i, j) in memo:
                return memo[(i, j)]

            if p[j] == '*':
                memo[(i, j)] = False
                return memo[(i, j)]

            if j < n - 1 and p[j + 1] == '*':
                # compare s[i:] vs p[j:j + 2]
                if p[j] == '.':
                    memo[(i, j)] = any(dp(i + k, j + 2) for k in range(m - i + 1))
                    return memo[(i, j)]

                x = 0
                while i + x < m and s[i + x] == p[j]:
                    x += 1

                memo[(i, j)] = any(dp(i + k, j + 2) for k in range(x + 1))
                return memo[(i, j)]

            # compare s[i] vs p[j]
            if p[j] == '.':
                memo[(i, j)] = dp(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = s[i] == p[j] and dp(i + 1, j + 1)
            return memo[(i, j)]

        return dp(0, 0)
