class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time: O(n ^ 2) | Space: O(n)
        n = len(s)
        self.window = [0, 0]

        def checkPalindrome(i: int, isEven: bool) -> None:
            left, right = i, i + 1 if isEven else i

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left > self.window[1] - self.window[0]:
                    self.window = [left, right]
                left, right = left - 1, right + 1

        for i in range(n):
            checkPalindrome(i, True)
            checkPalindrome(i, False)

        left, right = self.window
        return s[left:right + 1]
