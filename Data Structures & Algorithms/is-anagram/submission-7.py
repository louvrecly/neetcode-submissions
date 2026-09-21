class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s: racecar | t: carrace
        # sCounter: { a: 2, c: 2, e: 1, r: 2 }
        # tCounter: { a: 2, c: 2, e: 1, r: 2 }
        # Time: O(m + n) | Space: O(m + n)
        sCounter = Counter(s)
        tCounter = Counter(t)
        return sCounter == tCounter
