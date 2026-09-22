class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time: O(mn) | Space: O(mn)
        spiral = []

        def traverse(i: int, vertical: bool, start: int, stop: int, step: int=1) -> None:
            if vertical:
                for r in range(start, stop, step):
                    spiral.append(matrix[r][i])
            else:
                for c in range(start, stop, step):
                    spiral.append(matrix[i][c])

        m, n = len(matrix), len(matrix[0])
        bounds = [
            0,     # top
            n - 1, # right
            m - 1, # bottom
            0      # left
        ]
        i = 0
        while len(spiral) < m * n:
            vertical = i % 2 > 0
            lower = bounds[0] if vertical else bounds[3]  # top or left
            upper = bounds[2] if vertical else bounds[1]  # bottom or right
            ascending = (i // 2) % 2 == 0
            start = lower if ascending else upper
            stop = upper + 1 if ascending else lower - 1
            step = 1 if ascending else -1
            current = i % len(bounds)
            traverse(bounds[current], vertical, start, stop, step)
            bounds[current] += 1 if ((i + 1) // 2) % 2 == 0 else -1
            i += 1

        return spiral