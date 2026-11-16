class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # dp(i) = min(
        #     1 + dp(i + 1),  # Skip current char
        #     dp(j + 1) for j in range(i, n) if s[i:j + 1] in words_set
        # )
        # Time: O(n^2) | Space: O(n^2)
        n = len(s)
        words_set = set(dictionary)
        cache = { n: 0 }  # mapping i -> min extra chars

        def dp(i: int) -> int:
            if i >= n:
                return cache[n]

            if i in cache:
                return cache[i]

            result = 1 + dp(i + 1)

            for j in range(i, n):
                if s[i:j + 1] in words_set:
                    result = min(result, dp(j + 1))

            cache[i] = result
            return cache[i]

        return dp(0)
