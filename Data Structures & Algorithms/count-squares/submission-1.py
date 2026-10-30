class CountSquares:
    # y ^
    # 5 +     ^
    # 4 +     |
    # 3 + <-- x -->
    # 2 +     |
    # 1 +     v
    # --+-+-+-+-+-+->
    #   | 1 2 3 4 5

    def __init__(self):
        self.xy = defaultdict(dict)  # mapping x -> y -> count
        self.yx = defaultdict(dict)  # mapping y -> x -> count

    def add(self, point: List[int]) -> None:
        # Time: O(1) | Space: O(1)
        x, y = point
        self.xy[x][y] = self.xy[x].get(y, 0) + 1
        self.yx[y][x] = self.yx[y].get(x, 0) + 1

    def count(self, point: List[int]) -> int:
        # Time: O(1) | Space: O(1)
        x, y = point
        total = 0
        for x1 in range(1001):
            if x1 == x:
                continue

            y_peers = self.xy[x1].get(y, 0)
            if not y_peers:
                continue

            diff = abs(x - x1)

            y1 = y - diff
            if 0 <= y1 <= 1000:
                x_peers = self.yx[y1].get(x, 0)
                if x_peers:
                    diagonals = self.yx[y1].get(x1, 0)
                    if diagonals:
                        total += y_peers * x_peers * diagonals

            y1 = y + diff
            if 0 <= y1 <= 1000:
                x_peers = self.yx[y1].get(x, 0)
                if x_peers:
                    diagonals = self.yx[y1].get(x1, 0)
                    total += y_peers * x_peers * diagonals

        return total
