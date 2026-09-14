class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # [[1 3] [4 6]] [2 5]
        # [[1 6]]
        #        [       ]   [       ]
        #            [           ]
        # ---+---+---+---+---+---+---+--->
        #    0   1   2   3   4   5   6
        #        [       ]
        #            [           ]
        # ---+---+---+---+---+---+---+--->
        #    0   1   2   3   4   5   6
        #        [   I           ]
        #                    [       ]
        # ---+---+---+---+---+---+---+--->
        #    0   1   2   3   4   5   6
        #        [   I       I       ]
        # ---+---+---+---+---+---+---+--->
        #    0   1   2   3   4   5   6
        # Time: O(n) | Space: O(1)
        n = len(intervals)
        i = 0
        while i < n:
            if intervals[i][0] >= newInterval[0]:
                intervals.insert(i, newInterval)
                break
            i += 1

        if i == n:
            intervals.append(newInterval)

        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.pop(i + 1)
                continue
            i += 1

        return intervals
