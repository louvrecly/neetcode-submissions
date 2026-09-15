class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time: O(n ^ 2) | Space: O(1)
        n = len(s)
        result = [0, 0]

        for i in range(n):
            # Check odd length palindrome
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left > result[1] - result[0]:
                    result = [left, right]
                left, right = left - 1, right + 1
            # Check even length palindrome
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left > result[1] - result[0]:
                    result = [left, right]
                left, right = left - 1, right + 1

        left, right = result
        return s[left:right + 1]
