class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # s: xyxxyzbzbbisl
        # 0 1 2 3 4 5 6 7 8 9 0 1 2
        # x y x x y z b z b b i s l
        # {b: [6 9] i: [10 10] l: [12 12] s: [11 11] x: [0 3] y: [1 4] z: [5 7]}
        # sorted: [(0 3) (1 4) (5 7) (6 9) (10 10) (11 11) (12 12)]
        #    [           ]
        #        [           ]
        #                        [       ]
        #                            [           ]
        #                                            I   I   I
        # ---+---+---+---+---+---+---+---+---+---+---+---+---+--->
        #    0   1   2   3   4   5   6   7   8   9  10  11  12
        #    [           I   ]   [       I       ]   I   I   I
        # ---+---+---+---+---+---+---+---+---+---+---+---+---+--->
        #    0   1   2   3   4   5   6   7   8   9  10  11  12
        # merged: [(0 4) (5 9) (10 10) (11 11) (12 12)]
        # result: [5 5 1 1 1]
        # Time: O(n log n) | Space: O(n)
        ranges = {}  # Mapping char -> [i, j]
        for i, char in enumerate(s):
            if char not in ranges:
                ranges[char] = [i, i]
            else:
                ranges[char][1] = i

        intervals = sorted(ranges.values())
        merged = []
        current = intervals[0]

        for i in range(1, len(intervals)):
            if current[1] >= intervals[i][0]:
                current[1] = max(current[1], intervals[i][1])
            else:
                merged.append(current)
                current = intervals[i]

        merged.append(current)
        return [end - start + 1 for start, end in merged]
