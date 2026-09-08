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
        memo = {}  # Map (index, total) -> count

        def backtrack(i: int, total: int) -> int:
            if (i, total) in memo:
                return memo[(i, total)]

            if i == n:
                return 1 if total == target else 0

            num = nums[i]
            memo[(i, total)] = backtrack(i + 1, total - num) + backtrack(i + 1, total + num)
            return memo[(i, total)]

        return backtrack(0, 0)
        # # Time: O(2 ** n) | Space: O(2 ** n)
        # n = len(nums)
        # suffixSum = nums[:]

        # for i in range(n - 1):
        #     suffixSum[n - i - 2] += suffixSum[n - i -1]

        # def backtrack(i: int, total: int) -> int:
        #     if i == n:
        #         return 1 if total == target else 0

        #     num = nums[i]
        #     count = 0

        #     if total - suffixSum[i] <= target:
        #         count += backtrack(i + 1, total - num)

        #     if total + suffixSum[i] >= target:
        #         count += backtrack(i + 1, total + num)

        #     return count

        # return backtrack(0, 0)