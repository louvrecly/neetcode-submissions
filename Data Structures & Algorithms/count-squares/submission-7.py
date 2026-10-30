class CountSquares:

    def __init__(self):
        self.counter = {}  # mapping (x, y) -> count

    def add(self, point: List[int]) -> None:
        # Time: O(1) | Space: O(1)
        x, y = point
        self.counter[(x, y)] = self.counter.get((x, y), 0) + 1

    def count(self, point: List[int]) -> int:
        # Time: O(n) | Space: O(n)
        x, y = point
        total = 0

        for point1, count in self.counter.items():
            x1, y1 = point1

            if x1 == x or y1 == y or not count:
                continue

            diff_x = x1 - x
            diff_y = y1 - y

            if abs(diff_x) != abs(diff_y):
                continue

            total += (
                count *
                self.counter.get((x1, y), 0) *
                self.counter.get((x, y1), 0)
            )

        return total
