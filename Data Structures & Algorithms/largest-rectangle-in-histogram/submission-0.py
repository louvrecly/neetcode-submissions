class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # [3 3 4 1 1 0 6 5]
        #              X
        #              X X
        #      X       X X
        #  X X X       X X
        #  X X X       X X
        #  X X X X X   X X
        # Monotonic Increasing Stack
        # [3 3 4 1 1 0 6 5]
        #  ^ | 3 vs N | [(3 0)] | a: - | m: 0
        #    ^ | 3 = 3 | [(3 0) (3 1)] | a: - | m: 0
        #      ^ | 4 > 3 | [(3 0) (3 1) (4 2)] | a: - | m: 0
        #        ^ | 1 < 4 | [(3 0) (3 1) (4 2)] | a: (3-2)*4=4 | m: 4
        #        ^ | 1 < 3 | [(3 0) (3 1)] | a: (3-1)*3=6 | m: 6
        #        ^ | 1 < 3 | [(3 0)] | a: (3-0)*3=9 | m: 9
        #        ^ | 1 vs N | [(1 0)] | a: - | m: 9
        #          ^ | 1 = 1 | [(1 0) (1 4)] | a: - | m: 9
        #            ^ | 0 < 1 | [(1 0) (1 4)] | a: (5-4)*1=1 | m: 9
        #            ^ | 0 < 1 | [(1 0)] | a: (5-0)*1=5 | m: 9
        #            ^ | 0 vs N | [(0 0)] | a: - | m: 9
        #              ^ | 6 > 0 | [(0 0) (6 6)] | a: - | m: 9
        #                ^ | 5 < 6 | [(0 0) (6 6)] | a: (7-6)*6=6 | m: 9
        #                ^ | 5 > 0 | [(0 0) (5 6)] | a: - | m: 9
        #                  ^ | 0 < 5 | [(0 0) (5 6)] | a: (8-6)*5=10 | m: 10
        #                  ^ | 0 = 0 | [(0 0) (0 6)] | a: - | m: 10
        # Time: O(n) | Space: O(1)
        stack = []  # Monotonic Increasing (h, i)
        heights.append(0)
        maxArea = 0

        for r, h in enumerate(heights):
            start = r
            while stack and h < stack[-1][0]:
                hl, l = stack.pop()
                maxArea = max(maxArea, (r - l) * hl)
                start = l

            stack.append((h, start))

        return maxArea
