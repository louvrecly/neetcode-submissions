class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time: O(n) | Space: O(n)
        maxHeap = []
        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, (-distance, (x, y)))

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)

        return [point for _, point in maxHeap]
