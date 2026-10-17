class Solution:
    def isHappy(self, n: int) -> bool:
        # Time: O(cycle) | Space: O(cycle)
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumDigitSquares(n)

            if n == 1:
                return True

        return False

    def sumDigitSquares(self, n: int) -> int:
        output = 0

        while n:
            output += (n % 10) ** 2
            n //= 10

        return output
