class Solution:
    def trap(self, height: List[int]) -> int:
        # [0 2 0 3 1 0 1 3 2 1]
        # 3 |       X       X
        # 2 |   X   X       X X
        # 1 |   X   X X   X X X X
        # 0 | 0 2 0 3 1 0 1 3 2 1
        # Monotonic Decreasing Stack
        # [0 2 0 3 1 0 1 3 2 1]
        #  ^ | 0 vs N | s: [0] | w: (1-0-1)*(min(0,2)-0)=0 | t: 0
        #    ^ | 2 > 0 | s: [2] | w: - | t: 0
        #      ^ | 0 < 2 | s: [2 0] | w: - | t: 0
        #        ^ | 3 > 2 > 0 | s: [3] | w: (3-1-1)*(min(2,3)-0)=2 | t: 2
        #          ^ | 1 < 3 | s: [3 1] | w: - | t: 2
        #            ^ | 0 < 1 | s: [3 1 0] | w: - | t: 2
        #              ^ | 1 = 1 > 0 | s: [3 1] | w: (6-4-1)*(min(1,1)-0)=1 | t: 3
        #                ^ | 3 = 3 > 1 | s: [3] | w: (7-3-1)*(min(3,3)-1)=6 | t: 9
        #                  ^ | 2 < 3 | s: [3 2] | w: - | t: 9
        #                    ^ | 12 < 3 | s: [3 2] | w: - | t: 9
        # [4 2 0 3 2 5]
        #            X
        #  X         X
        #  X     X   X
        #  X X   X X X
        #  X X   X X X
        # Time: O(n) | Space: O(n)
        stack = []  # Monotonic Decreasing (h, i)
        water = 0

        for i, hi in enumerate(height):
            start = i
            while stack and hi > stack[-1][0]:
                hj, j = stack.pop()
                if stack:
                    water += (i - j) * (min(hi, stack[-1][0]) - hj)
                    start = j

            stack.append((hi, start))

        return water
