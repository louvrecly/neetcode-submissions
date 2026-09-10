class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # [[0 2] [2 2]] | k: 1
        # dist: { (0 2): 2, (2 2): sqrt(8) }
        # minHeap: [(2, 0, 2) (sqrt(8) 2 2)] -> pop k times
        # Time: O(n) | Space: O(n)
        distances = {(x, y): math.sqrt(x ** 2 + y ** 2) for x, y in points}
        minHeap = []

        for x, y in points:
            heapq.heappush(minHeap, (distances[(x, y)], x, y))

        closest = []
        while len(closest) < k:
            _, x, y = heapq.heappop(minHeap)
            closest.append((x, y))

        return closest
