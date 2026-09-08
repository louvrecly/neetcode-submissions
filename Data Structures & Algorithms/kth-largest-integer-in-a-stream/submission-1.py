class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Time: O(n) | Space: O(n)
        self.k = k
        self.maxHeap = []
        self.minHeap = []
        for num in nums:
            heapq.heappush(self.maxHeap, -num)

        for _ in range(self.k):
            if self.maxHeap:
                num = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -num)

    def add(self, val: int) -> int:
        # Time: O(1) | Space: O(1)
        if not self.minHeap or val > self.minHeap[0]:
            heapq.heappush(self.minHeap, val)
            while len(self.minHeap) > self.k:
                num = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -num)

        return self.minHeap[0]
