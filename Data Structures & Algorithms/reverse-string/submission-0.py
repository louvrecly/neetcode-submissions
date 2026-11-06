class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s: [n e e t]
        # [t e e n]
        # s: [r a c e c a r]
        # [r a c e c a r]
        # Time: O(n) | Space: O(1)
        n = len(s)
        mid = n // 2

        for i in range(mid):
            temp = s[i]
            s[i] = s[n - i - 1]
            s[n - i - 1] = temp