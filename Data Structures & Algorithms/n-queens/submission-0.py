class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Input: n = 1
        # Output: [["Q"]]
        # n: 3
        # [- - -]
        # [- - -]
        # [- - -]
        # ============ c: 0
        # [Q . .]
        # [. . -]
        # [. - .]
        # ============ c: 1
        # [Q . .]
        # [. . Q]
        # [. . .]
        # ============ c: 2 < 3 => 0
        # [. . -]
        # [Q . .]
        # [. . -]
        # ============ c: 1
        # [. . -]
        # [Q . .]
        # [. . -]
        # ============ c: 1
        # [# # # #]
        # [# # # #]
        # [# # # #]
        # [# # # #]
        # ============ c: 0
        # [Q . . .]
        # [. . # #]
        # [. # . #]
        # [. # # .]
        # ============ c: 1
        # [Q . . .]
        # [. . . #]
        # [. Q . .]
        # [. . . .]
        # ============ c: 2 | False
        # [. . # #]
        # [Q . . .]
        # [. . # #]
        # [. # . #]
        # ============ c: 1
        # [. . # #]
        # [Q . . .]
        # [. . . #]
        # [. Q . .]
        # ============ c: 2
        # [. . Q .]
        # [Q . . .]
        # [. . . #]
        # [. Q . .]
        # ============ c: 3
        # [. . Q .]
        # [Q . . .]
        # [. . . Q]
        # [. Q . .]
        # ============ c: 4 == n | True
        # Time: O(n ** 2) | Space: O(n ** 2)
        cols = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)
        board = [['.'] * n for _ in range(n)]
        solutions = []

        def backtrack(r: int) -> None:
            if r == n:
                solution = [''.join(row) for row in board]
                solutions.append(solution)
                return

            for c in range(n):
                if (
                    c in cols or
                    r + c in posDiag or
                    r - c in negDiag
                ):
                    continue
                
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1)
                
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'

        backtrack(0)
        return solutions
