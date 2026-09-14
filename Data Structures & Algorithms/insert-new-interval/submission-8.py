class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Time: O(n) | Space: O(1)
        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]

        inserted = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                inserted.append(newInterval)
                return inserted + intervals[i:]
            if newInterval[0] > intervals[i][1]:
                inserted.append(intervals[i])
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]

        inserted.append(newInterval)
        return inserted
