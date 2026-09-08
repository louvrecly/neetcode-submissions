class Solution:
    def climbStairs(self, n: int) -> int:
        # dp(i) = dp(i - 1) + dp(i - 2)
        # Time: O(n) | Space: O(1)
        if n < 3:
            return n

        cache1, cache2 = 1, 2
        output = 0

        for _ in range(3, n + 1):
            output = cache1 + cache2
            cache1, cache2 = cache2, output

        return output
