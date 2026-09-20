class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Time: O(mn) | Space: O(1)
        n = len(matrix)

        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for row in matrix:
            row.reverse()
