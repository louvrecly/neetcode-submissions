class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # i: [[4,5],[5,6],[2,9],[8,10],[2,6]] | q: [7,9,3,9,1,3]
        # i: [[4 5] [5 6] [2 9] [8 10] [2 6]] | q: [7 9 3 9 1 3]
        # i: [[2 6] [2 9] [4 5] [5 6] [8 10]] | q: [7 9 3 9 1 3] | qL: {}
        #    [       ]         | [2 6]
        #    [             ]   | [2 9]
        #        [ ]           | [4 5]
        #          [ ]         | [5 6]
        #                [   ] | [8 10]
        # -+-+-+-+-+-+-+-+-+-+
        #  1 2 3 4 5 6 7 8 9 10
        #  ^   ^       ^   ^
        # Time: O(m * log m + n * log n) | Space: O(m + n)
        intervals.sort()
        queryLengths = {}  # Mapping query -> length
        minHeap = []  # Store (length, right)
        i = 0

        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                heapq.heappush(minHeap, (right - left + 1, right))
                i += 1

            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)

            if minHeap:
                queryLengths[query] = minHeap[0][0]

        return [queryLengths[query] if query in queryLengths else -1 for query in queries]
