class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30 38 30 36 35 40 28]
        #   ^--^ | [1]
        #      ^--------^ | [1 3]
        #         ^--^ | [1 3 1]
        #            ^-----^ | [1 3 1 2]
        #               ^--^ | [1 3 1 2 1]
        #                  ^-----^ | [1 3 1 2 1 0]
        #                      ^-^ | [1 3 1 2 1 0 0]
        # Monotonic Decreasing Stack
        # [30 38 30 36 35 40 28]
        #   ^ | 30 | [(0 30)] | [N N N N N N N]
        #      ^ | 38 > 30 | [(1 38)] | [1-0 N N N N N N]
        #         ^ | 30 < 38 | [(1 38) (2 30)] | [1 N N N N N N]
        #            ^ | 36 > 30 | [(1 38) (3 36)] | [1 N 3-2 N N N N]
        #               ^ | 35 < 36 | [(1 38) (3 36) (4 35)] | [1 N 3-2 N N N N]
        #                  ^ | 40 > 35, 36, 38 | [(5 40)] | [1 5-1 1 5-3 5-4 N N]
        #                     ^ | 28 < 40 | [(5 40) (6 28)] | [1 4 1 2 1 N N]
        #                       ^ | N | [(5 40) (6 28)] | [1 4 1 2 1 0 0]
        # Time: O(n) | Space: O(n)
        stack = []  # monotonic decreasing stack (index)
        output = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                output[j] = i - j
            stack.append(i)

        return output
