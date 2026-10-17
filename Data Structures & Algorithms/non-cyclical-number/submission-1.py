class Solution:
    def isHappy(self, n: int) -> bool:
        # Time: O(cycle) | Space: O(cycle)
        visited = set()

        while n != 1:
            if n in visited:
                return False

            visited.add(n)
            digit_squares_sum = 0

            while n:
                digit_squares_sum += (n % 10) ** 2
                n //= 10

            n = digit_squares_sum

        return True
