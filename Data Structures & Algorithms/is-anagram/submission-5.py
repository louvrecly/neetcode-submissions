class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounts = [0] * 26
        tCounts = [0] * 26
        for char in s:
            sCounts[ord(char) - ord('a')] += 1
        for char in t:
            tCounts[ord(char) - ord('a')] += 1
        for i in range(26):
            if sCounts[i] != tCounts[i]:
                return False
        return True