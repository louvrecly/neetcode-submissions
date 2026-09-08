class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Was it a car or a cat I saw?
        # L                         R  | w = w
        #  L                       R  | a = a
        #   L                     R  | s = s
        #     L                 R  | i = i
        #      L              R  | t = t
        #        L           R  | a = a
        #          L        R  | c = c
        #           L     R  | a = a
        #            L  R  | r = r
        #              LR  | o = o
        # Time: O(n) | Space: O(1)
        n = len(s)
        left, right = 0, n - 1
        alphaNumerics = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')

        while left < right:
            while left < right and s[left] not in alphaNumerics:
                left += 1
            while left < right and s[right] not in alphaNumerics:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left, right = left + 1, right - 1

        return True
