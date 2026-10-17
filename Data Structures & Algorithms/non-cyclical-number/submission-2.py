class Solution:
    def isHappy(self, n: int) -> bool:
        # Time: O(cycle) | Space: O(cycle)
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            n = self.sum_digit_squares(n)

        return True

    def sum_digit_squares(self, n: int) -> int:
        total = 0
        while n:
            total += (n % 10) ** 2
            n //= 10
        return total
        