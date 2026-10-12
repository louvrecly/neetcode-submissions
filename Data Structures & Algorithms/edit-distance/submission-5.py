class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Time: O(mn) | Space: O(n)
        m, n = len(word1), len(word2)
        cache = [n - i for i in range(n + 1)]

        for i in range(m - 1, -1, -1):
            temp = [m - i if k == n else 0 for k in range(n + 1)]
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    temp[j] = cache[j + 1]
                else:
                    temp[j] = 1 + min(
                        temp[j + 1],
                        cache[j],
                        cache[j + 1]
                    )
            cache = temp

        return cache[0]
