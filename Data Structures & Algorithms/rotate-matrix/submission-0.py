class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # [
        #     [1 2]
        #     [3 4]
        # ]
        # [
        #     [3 1]
        #     [1 2]
        # ]
        # (0 0) -> (0 1)
        # (0 1) -> (1 1)
        # (1 0) -> (0 0)
        # (1 1) -> (1 0)
        # [
        #     [1 2 3]
        #     [4 5 6]
        #     [7 8 9]
        # ]
        # [
        #     [7 4 1]
        #     [8 5 2]
        #     [9 6 3]
        # ]
        # dr1, dc1 = -dc, dr
        # Time: O(n^2) | Space: O(n^2)
        n = len(matrix)
        memo = [[0] * n for _ in range(n)]
        def new_position(r: int, c: int) -> Tuple[int]:
            # (0 0) -> (0 2) | [-1 -1] -> [-1 1]
            # (1 1) -> (1 2) | [-1 0] -> [0 1]
            # (1 0) -> (0 1) | [0 -1] -> [-1 0]
            dr, dc = r - (n - 1) / 2, c - (n - 1) / 2
            dr1, dc1 = dc, -dr
            return (round((n - 1) / 2 + dr1), round((n - 1) / 2 + dc1))

        for r in range(n):
            for c in range(n):
                r1, c1 = new_position(r, c)
                memo[r1][c1] = matrix[r][c]

        for r in range(n):
            for c in range(n):
                matrix[r][c] = memo[r][c]
