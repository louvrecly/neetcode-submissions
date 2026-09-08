class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # [
        #     [ 1  2  4  8]
        #     [10 11 12 13]
        #     [14 20 30 40]
        # ] | t: 12
        # ---------------------------------
        # [ 1  2  4  8] <- 12 > 8
        # [10 11 12 13] <- 10 < 12 < 13
        # [14 20 30 40]
        # ---------------------------------
        # [10 11 12 13]
        #   L  M     R | M: 11 < 12
        #      L  M  R | M: 12 = 12
        # Time: O(log(m * n)) | Space: O(1)
        m, n = len(matrix), len(matrix[0])

        def binarySearchRow(r: int) -> bool:
            row = matrix[r]
            left, right = 0, n - 1
            if row[left] == target or row[right] == target:
                return True
            while left < right:
                mid = (left + right) // 2
                num = row[mid]
                if num < target:
                    left = mid + 1
                elif num > target:
                    right = mid - 1
                else:
                    return True
            return False

        for r in range(m):
            if matrix[r][0] > target:
                return False
            if matrix[r][n - 1] >= target:
                return binarySearchRow(r)
        return False
