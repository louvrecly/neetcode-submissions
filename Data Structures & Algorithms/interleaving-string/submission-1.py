class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # s1: aaaa | s2: bbbb | s3: aabbbbaa
        # l1: 4 | l2: 4 | l3: 8 = 4 + 4
        # s3: a a b b b b a a
        #     ^ | a | s1[0]: a | s2[0]: b | p: N c: s1 | m: 1 | n: 0
        #       ^ | a | s1[1]: a | s2[0]: b | p: s1 c: s1 | m: 1 | n: 0
        #         ^ | b | s1[2]: a | s2[0]: b | p: s1 c: s2 | m: 1 | n: 1
        #           ^ | b | s1[2]: a | s2[1]: b | p: s2 c: s2 | m: 1 | n: 1
        #             ^ | b | s1[2]: a | s2[2]: b | p: s2 c: s2 | m: 1 | n: 1
        #               ^ | b | s1[2]: a | s2[3]: b | p: s2 c: s2 | m: 1 | n: 1
        #                 ^ | a | s1[2]: a | s2[4]: - | p: s2 c: s1 | m: 2 | n: 1
        #                   ^ | a | s1[3]: a | s2[4]: - | p: s1 c: s1 | m: 2 | n: 1
        #                   | 2 - 1 | <= 1
        # s1: aa | s2: bab | s3: ababa
        #    s1: a | s2: bab | s3: baba
        #    s1: aa | s2: ab | s3: ababa
        # dp(i, j, k) = dp(i + 1, j, k + 1) or dp(i, j + 1, k + 1)
        #   i 0 0 0 1 1 1 2 2 2 3 3 3
        #   j 0 1 2 0 1 2 0 1 2 0 1 2
        #   0 T   T   T   T         F
        #   1   T   T   T   T       F
        # k 2     T   T   T   T     F
        #   3           T   T   T   F
        #   4                 T   T F
        #   5 F F F F F F F F F F F T
        # Time: O(mn(m + n)) | Space: O(mn(m + n))
        p, q, r = len(s1), len(s2), len(s3)
        if p + q != r:
            return False

        memo = {}  # Mapping (i, j, k) -> bool
        def dp(i: int, j: int, k: int) -> bool:
            if i == p and j == q and k == r:
                return True
            if k >= r:
                return False

            if (i, j, k) in memo:
                return memo[(i, j, k)]
            useS1 = i < p and s1[i] == s3[k] and dp(i + 1, j, k + 1)
            useS2 = j < q and s2[j] == s3[k] and dp(i, j + 1, k + 1)
            memo[(i, j, k)] = useS1 or useS2
            return memo[(i, j, k)]

        return dp(0, 0, 0)
