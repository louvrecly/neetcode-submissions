class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time: O(mn) | Space: O(1)
        m, n = len(matrix), len(matrix[0])
        left, right = 0, n - 1
        top, bottom = 0, m - 1
        spiral = []

        while left <= right and top <= bottom:
            for c in range(left, right + 1):
                spiral.append(matrix[top][c])
            top += 1
            for r in range(top, bottom + 1):
                spiral.append(matrix[r][right])
            right -= 1
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][c])
                bottom -= 1
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    spiral.append(matrix[r][left])
                left += 1

        return spiral
