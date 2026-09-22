class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time: O(mn) | Space: O(mn)
        m, n = len(matrix), len(matrix[0])
        bounds = [
            0,     # top
            n - 1, # right
            m - 1, # bottom
            0      # left
        ]
        spiral = []

        def traverse(index: int, horizontal: bool, ascending: bool) -> None:
            lower = bounds[3] if horizontal else bounds[0]  # top or left
            upper = bounds[1] if horizontal else bounds[2]  # bottom or right
            start = lower if ascending else upper
            stop = upper + 1 if ascending else lower - 1
            step = 1 if ascending else -1
            if horizontal:
                for c in range(start, stop, step):
                    spiral.append(matrix[index][c])
            else:
                for r in range(start, stop, step):
                    spiral.append(matrix[r][index])

        i = 0
        while len(spiral) < m * n:
            horizontal = i % 2 == 0
            ascending = (i // 2) % 2 == 0
            current = i % len(bounds)
            traverse(bounds[current], horizontal, ascending)
            bounds[current] += 1 if ((i + 1) // 2) % 2 == 0 else -1
            i += 1

        return spiral
