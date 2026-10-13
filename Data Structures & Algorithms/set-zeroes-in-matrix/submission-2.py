class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Time: O(mn(m + n)) | Space: O(1)
        m, n = len(matrix), len(matrix[0])

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    for i in range(m):
                        if matrix[i][c] != 0:
                            matrix[i][c] = float('inf')
                    for j in range(n):
                        if matrix[r][j] != 0:
                            matrix[r][j] = float('inf')

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == float('inf'):
                    matrix[r][c] = 0
