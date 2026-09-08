"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # [0 30] [5 10] [15 20]
        #   [                       ]
        #       [   ]
        #               [   ]
        # --+---+---+---+---+---+---+-->
        #   0   5  10  15  20  25  30
        # ================================ False
        # [5 20] [25 30] [10 15] [0 5]
        # [0 5] [5 20] [10 15] [25 30] sorted
        #   [   ]
        #       [           ]
        #           [   ]
        #                       [   ]
        # --+---+---+---+---+---+---+-->
        #   0   5  10  15  20  25  30
        # [0 5] [5 20] [10 15] [25 30] sorted
        #    ^   ^ | 5 = 5
        #           ^    ^ | 20 < 10 | False
        # Time: O(n * log n) | Space: O(n)
        # Sort the intervals
        orderedIntervals = sorted([(interval.start, interval.end) for interval in intervals])

        # Iterate through interval
        for i in range(len(orderedIntervals) - 1):
            # Current end greater than next start -> return false
            if orderedIntervals[i][1] > orderedIntervals[i + 1][0]:
                return False

        # Return true
        return True
