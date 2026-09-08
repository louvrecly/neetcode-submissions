class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1: abc | s2: lecabee
        # abc acb
        # bac bca
        # cab cba
        # sliding window + counter
        # l e c a b e e | abc
        # LR | l | 0 < 3
        #   LR | e | 0 < 3
        #     LR | c | 1 < 3
        #     L R | ca | 2 < 3
        #     L   R | cab | 3 = 3 | True
        # l e c a a b e e | abc
        # LR | l | 1 vs 0 < 3
        #   LR | e | 1 vs 0 < 3
        #     LR | c | 0 vs 1 < 3
        #     L R | ca | 0 vs 2 < 3
        #     L   R | caa | 1 vs 2 < 3
        #       L R | aa | 1 vs 1 < 3
        #         LR | a | 0 vs 1 < 3
        #         L R | ab | 0 vs 2 < 3
        #         L   R | abe | 1 vs 2 < 3
        #             LR | e | 1 vs 0 < 3
        #               LR | e | 1 vs 0 < 3
        # Time: O(m + n) | Space: O(m + n)
        counter = {}

        for char in s1:
            counter[char] = counter.get(char, 0) + 1

        m = len(s1)
        n = len(s2)
        left = 0
        matchCount = 0

        for right in range(n):
            while left <= right and counter.get(s2[right], 0) == 0:
                if s2[left] in counter:
                    counter[s2[left]] += 1
                    matchCount -= 1
                left += 1

            if counter.get(s2[right], 0) > 0:
                counter[s2[right]] -= 1
                matchCount += 1

            if matchCount == m:
                return True

        return False
