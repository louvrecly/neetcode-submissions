class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1 1 3 2 3 1 | k: 2
        # counter: { 1: 3, 2: 1, 3: 2 }
        # (1, 3), (2, 1), (3, 2) | sort -> | (2, 1), (3, 2), (1, 3)
        # (2, 1), (3, 2) | (1, 3) | [1] | k: 1
        # (2, 1) | (3, 2) | [1, 3] | k: 0
        # Time: O(k * log n) | Space: O(n)
        counter = Counter(nums)
        maxHeap = []

        for num, count in counter.items():
            heapq.heappush(maxHeap, (-count, num))

        result = []

        for i in range(k):
            _, num = heapq.heappop(maxHeap)
            result.append(num)

        return result
        # # Time: O(n * log n) | Space: O(n)
        # counter = Counter(nums)
        # ranked = [(num, count) for num, count in counter.items()]
        # ranked.sort(key=lambda x: x[1])

        # return [ranked[len(ranked) - i - 1][0] for i in range(k)]