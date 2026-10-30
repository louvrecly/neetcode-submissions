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
                if not 0 <= x1 <= 1000:
                    continue

                y_peers = self.counter.get(x1, {}).get(y, 0)
                if y_peers:
                    diagonals = self.counter.get(x1, {}).get(y1, 0)
                    total += count * y_peers * diagonals

        return total
