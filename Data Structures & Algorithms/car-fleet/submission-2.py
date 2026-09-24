class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # t: 10 | p: [1 4] | s: [3 2]
        #    0 |       0           1
        #    1 |                   0       1
        #    2 |                               0   1
        #  2.5 |                                      01
        #    3 |                                           [01]
        #   ---+---+---+---+---+---+---+---+---+---+---+---> p
        #      0   1   2   3   4   5   6   7   8   9  10
        #   t: 10 | p: [4 1 0 7] | s: [2 2 1 1]
        #    0 |   2   1           0           3
        #    1 |       2       1           0       3
        #    2 |           2           1           0   3
        #    3 |               2               1          03
        #    4 |                       2               1       [03]
        #    5 |                               2               [1] [03]
        #    6 |                                       2       [1] [03]
        #  6.5 |                                           2   [1] [03]
        #    7 |                                               [2] [1] [03]
        #   ---+---+---+---+---+---+---+---+---+---+---+---+---> p
        #          0   1   2   3   4   5   6   7   8   9  10
        # sorted: [(0 1) (1 2) (4 2) (7 1)]
        # (7 1) | eta: (10-7)/1=3 > 0 | fleets: 1
        # (4 2) | eta: (10-4)/2=3 = 3 | fleets: 1
        # (1 2) | eta: (10-1)/2=4.5 > 3 | fleets: 2
        # (0 1) | eta: (10-0)/1=10 > 4.5 | fleets: 3
        # Time: O(n log n) | Space: O(n)
        cars = []
        n = len(position)
        for i in range(n):
            heapq.heappush_max(cars, (position[i], speed[i]))

        prevEta = 0
        count = 0
        while cars:
            p, s = heapq.heappop_max(cars)
            eta = (target - p) / s
            if eta > prevEta:
                count += 1
            prevEta = max(prevEta, eta)

        return count
