class Solution:
    def reverse(self, x: int) -> int:
        # Time: O(1) | Space: O(1)
        sign = -1 if x < 0 else 1
        x = abs(x)
        reverse = 0
        while x:
            reverse *= 10
            reverse += x % 10
            x //= 10
        return sign * reverse if reverse < 2 ** 31 else 0
