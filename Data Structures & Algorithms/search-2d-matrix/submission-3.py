class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time: O(m + log(n)) | Space: O(1)
        for row in matrix:
            if target < row[0]:
                return False
            if target > row[-1]:
                continue
            left, right = 0, len(row) - 1
            if target in [row[left], row[right]]:
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
