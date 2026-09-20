class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # [1 2 3]     [7 4 1]
        # [4 5 6]  -> [8 5 2]
        # [7 8 9]     [9 6 3]
        # mid = (n - 1) / 2
        # r, c = mid + dr, mid + dc
        # dr, dc = r - mid, c - mid
        # r, c: (0 0) -> (0 2) | dr, dc: [-1 -1] -> [-1 1]
        # r, c: (0 1) -> (1 2) | dr, dc: [-1 0] -> [0 1]
        # r, c: (2 1) -> (1 0) | dr, dc: [1 0] -> [0 -1]
        # [1 2]  __\  [3 1]
        # [3 4]    /  [4 2]
        # r, c: (0 0) -> (0 1) | dr, dc: (-0.5 -0.5) -> (-0.5 0.5)
        # r, c: (1 0) -> (0 0) | dr, dc: (0.5 -0.5) -> (-0.5 -0.5)
        # r, c: (1 1) -> (1 0) | dr, dc: (0.5 0.5) -> (0.5 -0.5)
        # dr1, dc1 = dc, -dr
        # r1, c1 = mid + dr1, mid + dc1
        # r1, c1 = mid + dc, mid - dr
        # r1, c1 = mid + (c - mid), mid - (r - mid)
        # r1, c1 = c, 2 * mid - r
        # r1, c1 = c, n - r - 1
        # Time: O(mn) | Space: O(1)
        n = len(matrix)
        mid = (n - 1) / 2
        r, c = 0, 0

        while r < mid:
            while c <= mid:
                r1, c1 = r, c
                prev = matrix[r1][c1]
                for _ in range(4):
                    r2, c2 = c1, n - r1 - 1
                    temp = matrix[r2][c2]
                    matrix[r2][c2] = prev
                    prev = temp
                    r1, c1 = r2, c2
                c += 1
            r += 1
            c = 0
