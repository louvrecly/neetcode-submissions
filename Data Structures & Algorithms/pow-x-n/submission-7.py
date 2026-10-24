class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Time: O(log n) | Space: O(log n)
        def helper(num: float, i: int) -> float:
            if i == 0:
                return 1

            value = helper(num, i // 2)
            value *= value
            if i % 2 == 1:
                value *= num

            return value

        result = helper(x, abs(n))
        return result if n >= 0 else 1 / result
