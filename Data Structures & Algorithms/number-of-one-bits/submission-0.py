class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time: O(n) | Space: O(n)
        return f"{n:b}".count('1')
