class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time: O(1) | Space: O(1)
        # check row
        for r in range(9):
            numsSet = set()
            for c in range(9):
                if board[r][c] in numsSet:
                    return False
                if board[r][c] != '.':
                    numsSet.add(board[r][c])

        # check column
        for c in range(9):
            numsSet = set()
            for r in range(9):
                if board[r][c] in numsSet:
                    return False
                if board[r][c] != '.':
                    numsSet.add(board[r][c])

        # (0 0) (0 3) (0 6)
        # (3 0) (3 3) (3 6)
        # (6 0) (6 3) (6 6)
        # check grid
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                numsSet = set()
                for i in range(3):
                    for j in range(3):
                        if board[r + i][c + j] in numsSet:
                            return False
                        if board[r + i][c + j] != '.':
                            numsSet.add(board[r + i][c + j])

        return True
