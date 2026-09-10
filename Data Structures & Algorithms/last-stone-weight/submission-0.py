class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # [2 3 6 2 4]
        # sorted: [2 2 3 4 6]
        # 4 vs 6 -> 2 | [2 2 2 3]
        # 2 vs 3 -> 1 | [1 2 2]
        # 2 vs 2 -> 0 | [0 1]
        # 0 vs 1 -> 1 | [1]
        # [2 3 6 2 4]
        # maxHeap -> 6 vs 4 -> 2 | [2 3 2 2]
        # maxHeap -> 3 vs 2 -> 1 | [2 2 1]
        # maxHeap -> 2 vs 2 -> 0 | [0 1]
        # maxHeap -> 1 vs 0 -> 1 | [1]
        # Time: O(n) | Space: O(n)
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        while len(maxHeap) > 1:
            stone1 = -heapq.heappop(maxHeap)
            stone2 = -heapq.heappop(maxHeap)
            remain = stone1 - stone2
            heapq.heappush(maxHeap, -remain)

        return -heapq.heappop(maxHeap)
