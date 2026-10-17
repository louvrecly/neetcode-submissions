class Solution:
    def isHappy(self, n: int) -> bool:
        # Time: O(cycle) | Space: O(cycle)
        slow = n
        fast = self.iterate(n)

        while slow != fast:
            slow = self.iterate(slow)
            fast = self.iterate(self.iterate(fast))

        return slow == 1

    def iterate(self, n: int) -> int:
        result = 0
        while n:
            result += (n % 10) ** 2
            n //= 10
        return result
