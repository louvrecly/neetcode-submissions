class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time: O(81) | Space: O(729)
        rowsNums = [[False] * 9 for _ in range(9)]
        colsNums = [[False] * 9 for _ in range(9)]
        gridsNums = [[[False] * 9 for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                value = int(board[r][c]) - 1
                if (
                    rowsNums[r][value] or
                    colsNums[c][value] or
                    gridsNums[r // 3][c // 3][value]
                ):
                    return False
                rowsNums[r][value] = True
                colsNums[c][value] = True
                gridsNums[r // 3][c // 3][value] = True

        return True