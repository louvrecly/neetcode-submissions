class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Time: O(mn) | Space: O(m + n)
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for r in rows:
            for c in range(n):
                matrix[r][c] = 0

        for r in range(m):
            for c in cols:
                matrix[r][c] = 0
