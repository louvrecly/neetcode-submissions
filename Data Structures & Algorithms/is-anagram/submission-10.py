class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(m log m + n log n) | Space: O(m + n)
        return ''.join(sorted(s)) == ''.join(sorted(t))