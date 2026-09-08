class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time: O(n) | Space: O(1)
        left, right = 0, len(s) - 1

        def isAlphaNumeric(char: str) -> bool:
            return (
                ord('A') <= ord(char.lower()) <= ord('Z') or
                ord('a') <= ord(char.lower()) <= ord('z') or
                ord('0') <= ord(char.lower()) <= ord('9')
            )

        while left < right:
            while left < right and not isAlphaNumeric(s[left]):
                left += 1
            while left < right and not isAlphaNumeric(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left, right = left + 1, right - 1

        return True
