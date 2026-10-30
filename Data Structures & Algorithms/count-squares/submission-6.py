class CountSquares:

    def __init__(self):
        self.counter = {}  # mapping x -> y -> count

    def add(self, point: List[int]) -> None:
        # Time: O(1) | Space: O(1)
        x, y = point
        self.counter[x] = self.counter.get(x, {})
        self.counter[x][y] = self.counter[x].get(y, 0) + 1

    def count(self, point: List[int]) -> int:
        # Time: O(n) | Space: O(n)
        x, y = point
        y_maps = self.counter.get(x, {})
        total = 0

        for y1, count in y_maps.items():
            if y1 == y or not count:
                continue

            side = abs(y - y1)
            for x1 in [x - side, x + side]:
                counter = self.counter.get(x1, {})
                total += count * counter.get(y, 0) * counter.get(y1, 0)

        return total
