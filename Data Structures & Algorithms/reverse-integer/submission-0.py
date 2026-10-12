class Solution:
    def reverse(self, x: int) -> int:
        # Time: O(1) | Space: O(1)
        negative = x < 0
        value_string = str(x)[1:] if negative else str(x)
        value_string = value_string[::-1]
        limit = 2 ** 31
        result = int(value_string) * (-1 if negative else 1)
        return result if -limit <= result < limit else 0
