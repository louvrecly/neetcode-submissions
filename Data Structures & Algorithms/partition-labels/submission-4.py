class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Time: O(n) | Space: O(n)
        last = {}  # Mapping char -> last index
        for i, char in enumerate(s):
            last[char] = i

        result = []
        start, end = 0, 0
        for i, char in enumerate(s):
            end = max(end, last[char])
            if i == end:
                result.append(end - start + 1)
                start, end = i + 1, i + 1

        return result
