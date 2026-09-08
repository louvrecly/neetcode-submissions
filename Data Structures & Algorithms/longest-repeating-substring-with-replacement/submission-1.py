class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s: XYYX | k: 2
        #     ^^  | XXXX | 4
        # s: AAABABB | k: 1
        #       ^    | AAAAABB | 5
        # A A A B A B B B | k: 1
        # LR | A | 1 0 | O | 1
        # L R | AA | 2 0 | O | 2
        # L   R | AAA | 3 0 | O | 3
        # L     R | AAAB | 3 1 | O | 4
        # L       R | AAABA | 4 1 | O | 5
        # L         R | AAABAB | 4 1 | X | 5
        #       L   R | BAB | 2 1 | O | 5
        #       L     R | BABB | 3 1 | O | 5
        #       L       R | BABBB | 4 1 | O | 5
        # Time: O(n) | Space: O(n)
        counter = {}  # Mapping char -> count
        left = 0
        maxCount = 0
        maxLength = 0

        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            maxCount = max(maxCount, counter.get(s[right]))

            while right - left + 1 - maxCount > k:
                counter[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength
