class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(m + n) | Space: O(1)
        sCounter = Counter(s)
        tCounter = Counter(t)
        if len(sCounter) != len(tCounter):
            return False
        for char in sCounter:
            if sCounter.get(char) != tCounter.get(char):
                return False
        return True
        