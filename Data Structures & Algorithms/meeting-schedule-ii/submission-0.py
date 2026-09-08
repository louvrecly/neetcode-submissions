"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # [(0 40) (5 10) (15 20)]
        # sorted: [(0 40) (5 10) (15 20)]
        #    [                               ]
        #        [   ]
        #                [   ]
        # ---+---+---+---+---+---+---+---+---+--->
        #    0   5  10  15  20  25  30  35  40
        #    [                               ]
        #        [   ]   [   ]
        # ---+---+---+---+---+---+---+---+---+--->
        #    0   5  10  15  20  25  30  35  40
        # [(0 35) (15 30) (5 15) (20 40)]
        # sorted: [(0 35) (5 15) (15 30) (20 40)]
        #    [                           ]
        #        [       ]
        #                [           ]
        #                    [               ]
        # ---+---+---+---+---+---+---+---+---+--->
        #    0   5  10  15  20  25  30  35  40
        #    [                           ]
        #        [       |           ]
        #                    [               ]
        # ---+---+---+---+---+---+---+---+---+--->
        #    0   5  10  15  20  25  30  35  40
        # sorted: [(0 35) (5 15) (15 30) (20 40)]
        #           ^ | [] vs 0 | [35] | 1
        #                  ^ | [35] vs 5 | [35 15] | 2
        #                          ^ | [35 15] vs 15 | [35 30] | 2
        #                                  ^ | [35 30] vs 20 | [35 30 40] | 3
        # Time: O(n * log n) | Space: O(n)
        # Sort the intervals
        intervals.sort(key=lambda i: (i.start, i.end))
        # Init previous end times stack (min heap)
        minHeap = []
        # Init max rooms count
        maxRooms = 0

        # Iterate through intervals
        for i in range(len(intervals)):
            # While non-empty stack and min end <= current start -> pop min end time
            while minHeap and minHeap[0] <= intervals[i].start:
                heapq.heappop(minHeap)
            # Push current end time to stack
            heapq.heappush(minHeap, intervals[i].end)
            # Update max room count
            maxRooms = max(maxRooms, len(minHeap))

        # Return max room count
        return maxRooms
