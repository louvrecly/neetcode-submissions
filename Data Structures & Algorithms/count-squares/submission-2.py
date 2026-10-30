class CountSquares:

    def __init__(self):
        # counter: mapping x -> y -> count
        self.counter = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        # Time: O(1) | Space: O(1)
        x, y = point
        self.counter[x][y] += 1

    def count(self, point: List[int]) -> int:
        # Time: O(1000) | Space: O(1000)
        x, y = point
        limit = max(y, 1000 - y)
        total = 0

        for length in range(1, limit + 1):
            for y1 in [y - length, y + length]:
                if not 0 <= y1 <= 1000:
                    continue

                x_peers = self.counter[x][y1]
                if not x_peers:
                    continue

                diff = abs(y - y1)
                for x1 in [x - diff, x + diff]:
                    if not 0 <= x1 <= 1000:
                        continue

                    y_peers = self.counter[x1][y]
                    if not y_peers:
                        continue

                    diagonals = self.counter[x1][y1]
                    total += x_peers * y_peers * diagonals

        return total
