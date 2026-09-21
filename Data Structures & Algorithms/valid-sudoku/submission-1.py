class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time: O(81) | Space: O(81)
        rowsSet = [set() for _ in range(9)]
        colsSet = [set() for _ in range(9)]
        gridsSet = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == '.':
                    continue
                if (
                    value in rowsSet[r] or
                    value in colsSet[c] or
                    value in gridsSet[r // 3][c // 3]
                ):
                    return False
                rowsSet[r].add(value)
                colsSet[c].add(value)
                gridsSet[r // 3][c // 3].add(value)

        return True
