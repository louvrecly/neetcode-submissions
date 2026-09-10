class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # [[0 2] [2 2]] | k: 1
        # dist: (0 2) -> 2 | (2 2) -> sqrt(8)
        # sorted: [[0 2] [2 2]] -> pop (n - k) times
        # Time: O(n) | Space: O(n)
        distances = {}  # mapping (x, y) -> distance
        for x, y in points:
            distances[(x, y)] = math.sqrt(x ** 2 + y ** 2)

        points.sort(key=lambda p: distances[(p[0], p[1])])

        while len(points) > k:
            points.pop()

        return points
