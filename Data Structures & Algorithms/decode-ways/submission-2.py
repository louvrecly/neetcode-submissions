class Solution:
    def numDecodings(self, s: str) -> int:
        # Dynamic Programming - Bottom Up
        # dp(i) = dp(i + 1) + dp(i + 2)
        # Time: O(n) | Space: O(1)
        def is_valid(char: str) -> bool:
            if not char.isdigit() or char[0] == '0':
                return False
            return 0 <= int(char) <= 26

        n = len(s)
        memo_1, memo_2 = 1 if is_valid(s[n - 1]) else 0, 1

        for i in range(n - 2, -1, -1):
            count = 0
            if is_valid(s[i]):
                count += memo_1
            if is_valid(s[i:i + 2]):
                count += memo_2
            memo_1, memo_2 = count, memo_1

        return memo_1
