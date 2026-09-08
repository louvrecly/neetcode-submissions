class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Time: O(m * n) | Space: O(m * n)
        m, n = len(board), len(board[0])

        def capture(r: int, c: int) -> None:
            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                board[r][c] != 'O'
            ):
                return

            board[r][c] = 'B'

            capture(r + 1, c)
            capture(r, c + 1)
            capture(r - 1, c)
            capture(r, c - 1)

        for r in range(m):
            for c in range(n):
                if (
                    board[r][c] == 'O' and
                    (r in [0, m - 1] or c in [0, n - 1])
                ):
                    capture(r, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'B':
                    board[r][c] = 'O'
