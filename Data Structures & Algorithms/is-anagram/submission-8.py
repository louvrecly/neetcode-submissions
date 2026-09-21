class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(m + n) | Space: O(m + n)
        if len(s) != len(t):
            return False

        sCounter = {}
        for char in s:
            sCounter[char] = sCounter.get(char, 0) + 1

        tCounter = {}
        for char in t:
            tCounter[char] = tCounter.get(char, 0) + 1

        for char, count in sCounter.items():
            if char not in tCounter or tCounter[char] != count:
                return False

        return True
        