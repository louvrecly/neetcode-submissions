class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # s1: ac | s2: ab | s3: aabc
        # dp(i, j) = dp(i + 1, j) or dp(i, j + 1)
        #    j  0  1  2
        #    0  T  T  F      
        # i  1  T  T  T
        #    2  F  F  T
        # Time: O(mn) | Space: O(mn)
        p, q, r = len(s1), len(s2), len(s3)
        if p + q != r:
            return False

        memo = {}
        def dp(i: int, j: int) -> bool:
            if i + j >= r:
                return True

            if (i, j) in memo:
                return memo[(i, j)]
            useS1 = i < p and s1[i] == s3[i + j] and dp(i + 1, j)
            useS2 = j < q and s2[j] == s3[i + j] and dp(i, j + 1)
            memo[(i, j)] = useS1 or useS2
            return memo[(i, j)]

        return dp(0, 0)
