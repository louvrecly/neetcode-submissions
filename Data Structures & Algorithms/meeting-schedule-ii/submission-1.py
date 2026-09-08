"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # [(0 35) (10 20) (5 10) (25 40)]
        #    [                           ]
        #        [   ]
        #            [       ]
        #                        [           ]
        # ---+---+---+---+---+---+---+---+---+--->
        #    0   5  10  15  20  25  30  35  40
        #    [                           ]
        #        [   |       ]   [           ]
        # ---+---+---+---+---+---+---+---+---+--->
        #    0   5  10  15  20  25  30  35  40
        # s: [ 0  5 10 25]
        # e: [10 20 35 40]
        #      v | 0 < 10 | c: 1 | m: 1
        # s: [ 0  5 10 25]
        # e: [10 20 35 40]
        #      ^
        #         v | 5 < 10 | c: 2 | m: 2
        # s: [ 0  5 10 25]
        # e: [10 20 35 40]
        #      ^
        #            v | 10 = 10 | c: 2 | m: 2
        # s: [ 0  5 10 25]
        # e: [10 20 35 40]
        #      ^
        #               v | 25 > 20 | c: 1 | m: 2
        # s: [ 0  5 10 25]
        # e: [10 20 35 40]
        #         ^
        # Two pointers
        # Time: O(n * log n) | Space: O(n)
        # Sort start times & end times
        starts = [i.start for i in sorted(intervals, key=lambda i: i.start)]
        ends = [i.end for i in sorted(intervals, key=lambda i: i.end)]
        # Init count and max count
        count = 0
        maxCount = 0
        j = 0

        # Iterate each start time
        for i in range(len(starts)):
            # Compare start vs end times
            # Keep decreasing count & moving to next end until start < end
            while starts[i] >= ends[j]:
                j += 1
                count -= 1
            # Increase count and update max count
            count += 1
            maxCount = max(maxCount, count)
        # Return max count
        return maxCount
