"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # [5 15] [20 30] [0 5] [25 30]
        # sort: [0 5] [5 15] [20 30] [25 30]
        #    [   ]
        #        [       ]
        #                    [       ]
        #                        [   ]
        # ---+---+---+---+---+---+---+--->
        #    0   5  10  15  20  25  30
        # sort: [0 5] [5 15] [20 30] [25 30]
        #          ^   ^ | 5 = 5
        #                 ^    ^ | 15 < 20
        #                         ^    ^ | 30 > 25 | False
        # Time: O(n * log n) | Space: O(n)
        # Sort the intervals
        intervals.sort(key=lambda interval: (interval.start, interval.end))

        # Iterate through the intervals
        for i in range(len(intervals) - 1):
            # Current end later than next start -> False
            if intervals[i].end > intervals[i + 1].start:
                return False

        # Return True
        return True
