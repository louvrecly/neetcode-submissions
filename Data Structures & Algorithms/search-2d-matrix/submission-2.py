class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time: O(m + n) | Space: O(1)
        for row in matrix:
            if target < row[0]:
                return False
            if target > row[-1]:
                continue
            if target in row:
                return True
        return False
