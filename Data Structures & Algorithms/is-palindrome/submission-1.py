class Solution:
    def isPalindrome(self, s: str) -> bool:
        # t|a|b| |a| |c|a|t
        # L               R | t = t
        #   L           R | a = a
        #     L       R | b != c | F
        # t|o|p| |o|f| |p|o|t
        # L                 R | t = t
        #   L             R | o = o
        #     L         R | p = p
        #         L R | o != f | F
        # Time: O(n) | Space: O(1)
        l, r = 0, len(s) - 1
        s = s.lower()
        validChars = set('abcdefghijklmnopqrstuvwxyz0123456789')

        while l < r:
            while l < r and s[l] not in validChars:
                l += 1
            while l < r and s[r] not in validChars:
                r -= 1

            if l >= r:
                break

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True
