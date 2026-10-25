class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dynamic programming
        # dp[i] = any(dp[i + len(word)] for word in wordDict if s[i:i + len(word)] == word)
        # Time: O(n) | Space: O(n)
        n = len(s)
        cache = [False] * (n + 1)
        cache[n] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                if s[i:i + len(word)] == word and cache[i + len(word)]:
                    cache[i] = True
                    break

        return cache[0]
