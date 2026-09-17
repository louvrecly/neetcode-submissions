class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time: O(n log n) | Space: O(1)
        heapq.heapify(intervals)
        merged = []
        while intervals:
            start, end = heapq.heappop(intervals)
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged
