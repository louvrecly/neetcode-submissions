class Solution:
    def countSubstrings(self, s: str) -> int:
        # s: abc
        #    ^ | a | c: 1
        #     ^ | b | c: 2
        #      ^ | c | c: 3
        # s: a a a b c b
        #    ^ | a | c: 1
        #    [ ] | aa | c: 2
        #      ^ | a | c: 3
        #    [ ^ ] | aaa | c: 4
        #      [ ] | aa | c: 5
        #        ^ | a | c: 6
        #          ^ | b | c: 7
        #            ^ | c | c: 8
        #          [ ^ ] | bcb | c: 9
        #              ^ | b | c: 10
        # Time: O(n) | Space: O(1)
        n = len(s)
        count = 0

        for i in range(n):
            left, right = i - 1, i + 1
            count += 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left, right = left - 1, right + 1

            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left, right = left - 1, right + 1

        return count
