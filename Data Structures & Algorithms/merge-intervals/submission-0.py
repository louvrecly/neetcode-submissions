class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [1 3] [1 5] [6 7]
        #    [       ]
        #    [               ]
        #                        [   ]
        # ---+---+---+---+---+---+---+--->
        #    1   2   3   4   5   6   7
        #    [       I       ]   [   ]
        # ---+---+---+---+---+---+---+--->
        #    1   2   3   4   5   6   7
        # [1 5] [6 7]
        # Time: O(n log n) | Space: O(1)
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
