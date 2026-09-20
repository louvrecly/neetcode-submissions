class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Time: O(n^2) | Space: O(1)
        lower, upper = 0, len(matrix) - 1

        while lower < upper:
            left, right = lower, upper
            top, bottom = lower, upper
            for i in range(upper - lower):
                topLeft = matrix[top][left + i]
                # bottom left -> top left
                matrix[top][left + i] = matrix[bottom - i][left]
                # bottom right -> bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                # top right -> bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                # top left -> top right
                matrix[top + i][right] = topLeft
            lower, upper = lower + 1, upper - 1
