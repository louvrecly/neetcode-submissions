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
        # Time: O(2 ** n) | Space: O(2 ** n)
        n = len(nums)

        def backtrack(i: int, total: int) -> int:
            if i == n:
                return 1 if total == target else 0

            num = nums[i]
            return (
                backtrack(i + 1, total - num) +
                backtrack(i + 1, total + num)
            )

        return backtrack(0, 0)