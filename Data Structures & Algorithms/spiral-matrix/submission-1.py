class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # [
        #     [ 1  2  3  4]
        #     [ 5  6  7  8]
        #     [ 9 10 11 12]
        # ]
        # directions: R | D | L | U
        # R: (0 1) | D: (1 0) | L: (0 -1) | U: (-1 0)
        # boundaries: m | n | i: 0 | j: 0
        # [0 0] -> R | c == n - 1 | i += 1
        # [0 n-1] -> D | r == m - 1 | n -= 1
        # [m-1 n-1] -> L | c == 0 | m -= 1
        # [m-1 0] -> U | r == 1 | j += 1
        # Time: O(mn) | Space: O(1)
        m, n = len(matrix), len(matrix[0])
        t_bound, b_bound = 0, m - 1
        l_bound, r_bound = 0, n - 1
        spiral = []

        while len(spiral) < m * n:
            # Moves right
            for c in range(l_bound, r_bound + 1):
                spiral.append(matrix[t_bound][c])
            if len(spiral) == m * n:
                return spiral
            t_bound += 1
            # Moves down
            for r in range(t_bound, b_bound + 1):
                spiral.append(matrix[r][r_bound])
            if len(spiral) == m * n:
                return spiral
            r_bound -= 1
            # Moves left
            for c in range(r_bound, l_bound - 1, -1):
                spiral.append(matrix[b_bound][c])
            if len(spiral) == m * n:
                return spiral
            b_bound -= 1
            # Moves up
            for r in range(b_bound, t_bound - 1, -1):
                spiral.append(matrix[r][l_bound])
            if len(spiral) == m * n:
                return spiral
            l_bound += 1

        return spiral
