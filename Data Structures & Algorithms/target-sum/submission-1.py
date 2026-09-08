class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # [1 1] | target: 0
        #  + -
        #  - +
        # [2 2 2] | target: 2
        #  + + -
        #  + - +
        #  - + +
        # [1 4 2] | target: 3
        #            1
        #        /       \
        #      -1         +1
        #     /   \      /  \
        #   -4    +4   -4   +4 
        #   /\    /\    /\   /\
        # -2 +2 -2 +2 -2 +2 -2 +2 
        # -7 -3  1  5 -5 -1  3  7
        #                    ^
        # [1 2] | target: 1
        #            1
        #        /       \
        #      -1         +1
        #     /   \      /  \
        #   -2    +2   -2   +2
        #   -3     1   -1    3 
        #          ^
        # [2 1] | target: 1
        #            2
        #        /       \
        #      -2         +2
        #     /   \      /  \
        #   -1    +1   -1   +1
        #   -3    -1    1    3 
        #               ^
        # [2 1] | target: 1
        #          S
        #  2|   -/    +\
        #      -2      +2
        #  1| -/ +\   -/ +\
        #    -3   -1  1    3 
        #             ^
        n = len(nums)
        count = [0]

        def backtrack(i: int, total: int) -> None:
            if i == n:
                if total == target:
                    count[0] += 1
                return

            num = nums[i]
            backtrack(i + 1, total - num)
            backtrack(i + 1, total + num)

        backtrack(0, 0)
        return count[0]