class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s: abccbadd | t: abbd
        # abccbadd | l: 8
        # bccbad | l: 6
        # s: abccbadd | t: abbd
        #    l      r | c: {a:2 b:2 c:2 d:2} | tCount: {a:1 b:2 d:1}
        #     l    r | c: {a:1 b:2 c:2 d:1} | tCount: {a:1 b:2 d:1}
        #     l    r | c: {a:1 b:2 c:2 d:1} | tCount: {a:1 b:2 d:1}
        # Two Pointers - Opposite Directions (Shrinking Window)
        # s: abccbadd | t: abbd
        # a b c c b a d d | {a:1 b:2 d:1}
        # LR | a | m: 1 < 3 | l: - | r: -
        # L R | ab | m: 1 < 3 | l: - | r: -
        # L   R | abc | m: 1 < 3 | l: - | r: -
        # L     R | abcc | m: 1 < 3 | l: - | r: -
        # L       R | abccb | m: 2 < 3 | l: - | r: -
        # L         R | abccba | m: 2 < 3 | l: - | r: -
        # L           R | abccbad | m: 3 = 3 | l: 7 | r: abccbad
        #   L         R | bccbad | m: 3 = 3 | l: 6 | r: bccbad
        #   L           R | bccbadd | m: 3 = 3 | l: - | r: bccbad
        # Two Pointers - Same Direction (Sliding Window)
        # Time: O(m + n) | Space: O(m + n)
        t_counter = {}
        for char in t:
            t_counter[char] = t_counter.get(char, 0) + 1

        left = 0
        counter = {}
        matches = 0
        window = ''

        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            if counter[s[right]] == t_counter.get(s[right]):
                matches += 1

            while left <= right and matches == len(t_counter):
                if not window or right - left + 1 < len(window):
                    window = s[left:right + 1]

                counter[s[left]] -= 1
                if counter[s[left]] < t_counter.get(s[left], 0):
                    matches -= 1
                left += 1

        return window
