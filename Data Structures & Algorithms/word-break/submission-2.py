class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dynamic programming
        # dp[i] = any(dp[i + len(word)] for word in wordDict if s[i:i + len(word)] == word)
        # Time: O(n) | Space: O(n)
        n = len(s)
        memo = {}  # Mapping i -> T | F

        def dp(i: int) -> bool:
            if i == n:
                return True

            if i in memo:
                return memo[i]

            for word in wordDict:
                if s[i:i + len(word)] == word and dp(i + len(word)):
                    memo[i] = True
                    return memo[i]

            memo[i] = False
            return memo[i]

        return dp(0)
