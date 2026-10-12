class Solution:
    def reverse(self, x: int) -> int:
        # Time: O(1) | Space: O(1)
        sign = 1 if x >= 0 else -1
        x = abs(x)
        value = 0
        limit = 2 ** 31
        while x:
            value = 10 * value + x % 10
            x //= 10
            if value >= limit:
                return 0
        result = sign * value
        return result if -limit <= result < limit else 0
