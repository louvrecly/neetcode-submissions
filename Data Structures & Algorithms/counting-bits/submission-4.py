class Solution:
    def countBits(self, n: int) -> List[int]:
        # n: 9
        # 0: 0 0 0 0 | 0
        # 1: 0 0 0 1 | 1 = 1 + dp[1 - 1] = 1 + dp[0]
        # 2: 0 0 1 0 | 1 = 1 + dp[2 - 2] = 1 + dp[0]
        # 3: 0 0 1 1 | 2 = 1 + dp[3 - 2] = 1 + dp[1]
        # 4: 0 1 0 0 | 1 = 1 + dp[4 - 4] = 1 + dp[0]
        # 5: 0 1 0 1 | 2 = 1 + dp[5 - 4] = 1 + dp[1]
        # 6: 0 1 1 0 | 2 = 1 + dp[6 - 4] = 1 + dp[2]
        # 7: 0 1 1 1 | 3 = 1 + dp[7 - 4] = 1 + dp[3]
        # 8: 1 0 0 0 | 1 = 1 + dp[8 - 8] = 1 + dp[0]
        # 9: 1 0 0 1 | 2 = 1 + dp[9 - 8] = 1 + dp[1]
        # dp[n] = 1 + dp[n - 2 ** i] where 2 ** i <= n
        # [1 2 4 8 16 ...]
        # Time: O(n) | Space: O(1)
        dp = [0] * (n + 1)
        power = 0
        count = 0

        for i in range(1, n + 1):
            offset = 2 ** power
            count += 1
            dp[i] = 1 + dp[i - offset]
            if count >= offset:
                power += 1
                count = 0

        return dp
