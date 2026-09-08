class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # Time: O(m + n) | Space: O(1)
        # sCounter = Counter(s)
        # tCounter = Counter(t)
        # if len(sCounter) != len(tCounter):
        #     return False
        # for char in sCounter:
        #     if sCounter.get(char) != tCounter.get(char):
        #         return False
        # return True
        # Time: O(m + n) | Space: O(1)
        sCharCounts = [0] * 26
        tCharCounts = [0] * 26
        for char in s:
            sCharCounts[ord(char) - ord('a')] += 1
        for char in t:
            tCharCounts[ord(char) - ord('a')] += 1
        for i in range(26):
            if sCharCounts[i] != tCharCounts[i]:
                return False
        return True
        