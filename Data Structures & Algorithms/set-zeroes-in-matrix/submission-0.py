class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # [
        #     [1 2 3]
        #     [4 0 5]
        #     [6 7 8]
        # ]
        # [
        #     [1 0 3]
        #     [0 0 0]
        #     [6 0 8]
        # ]
        # Time: O(mn) | Space: O(mn)
        m, n = len(matrix), len(matrix[0])
        zeroes = set()

        # Iterate each row
        for r in range(m):
            # Iterate each column
            for c in range(n):
                # Found 0 -> mark r, c as sources
                if matrix[r][c] == 0:
                    zeroes.add((r, c))

        # Iterate through source
        for r, c in zeroes:
            # Update column
            for i in range(m):
                matrix[i][c] = 0
            # Update row
            for j in range(n):
                matrix[r][j] = 0
