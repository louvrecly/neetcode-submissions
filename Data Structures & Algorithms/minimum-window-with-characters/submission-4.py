class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s: abcdabd | t: abbd
        # a b c d a b d | {a:1 b:2 d:1} | n: 3
        # LR | a | {a:1} | m: 1 < 3 | l: - | w: -
        # L R | ab | {a:1 b:1} | m: 1 < 3 | l: - | w: -
        # L   R | abc | {a:1 b:1} | m: 1 < 3 | l: - | w: -
        # L     R | abcd | {a:1 b:1 d:1} | m: 2 < 3 | l: - | w: -
        # L       R | abcda | {a:2 b:1 d:1} | m: 2 < 3 | l: - | w: -
        # L         R | abcdab | {a:2 b:2 d:1} | m: 3 = 3 | l: 6 | w: abcdab
        #   L       R | bcdab | {a:1 b:2 d:1} | m: 3 = 3 | l: 5 | w: bcdab
        #     L     R | cdab | {a:1 b:1 d:1} | m: 2 < 3 | l: - | w: bcdab
        #     L       R | cdabd | {a:1 b:1 d:2} | m: 2 < 3 | l: - | w: bcdab
        # Two Pointers with Same Directions (Sliding Window)
        # Time: O(m + n) | Space: O(n)
        t_counter = {}
        for char in t:
            t_counter[char] = t_counter.get(char, 0) + 1

        matches = 0
        window = []
        left = 0
        counter = {}

        for right in range(len(s)):
            if s[right] in t_counter:
                counter[s[right]] = counter.get(s[right], 0) + 1
                if counter[s[right]] == t_counter.get(s[right], 0):
                    matches += 1

            while left <= right and matches == len(t_counter):
                if not window or right - left < window[1] - window[0]:
                    window = [left, right]
                if s[left] in t_counter:
                    counter[s[left]] -= 1
                    if counter[s[left]] < t_counter[s[left]]:
                        matches -= 1
                left += 1

        return s[window[0]:window[1] + 1] if window else ''
