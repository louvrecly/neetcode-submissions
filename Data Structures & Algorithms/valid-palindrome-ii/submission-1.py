class Solution:
    def validPalindrome(self, s: str) -> bool:
        # a|c|a
        # L   R | a = a | tol: T
        #   LR | c = c | tol: T | T
        # a|b|b|a|d|c
        # L         R | a != c | tol: F
        # L       R | a != d | tol: F
        #   L       R | b != c | tol: F | F
        # a b b d a
        # L       R | a = a | tol: T
        #   L   R | b != d | tol: F | l+1: b != d | r-1: b = b
        #   L R | b = b | tol: F | T
        # Two Pointers
        # a b d b b d a
        # L           R | a = a | tol: T
        #   L       R | b != d | tol: F | l+1: b != d | r-1: b = b
        #     L     R | b = b | tol: F | T
        # Two Pointers
        # Time: O(n) | Space: O(n)
        l, r = 0, len(s) - 1

        def isPalindrome(string: str) -> bool:
            return string == string[::-1]

        while l < r:
            if s[l] != s[r]:
                return isPalindrome(s[l + 1:r + 1]) or isPalindrome(s[l:r])
            l, r = l + 1, r - 1

        return True