class Solution:
    def jump(self, nums: List[int]) -> int:
        # [2 4 1 1 1 2 2 3 1] | n: 9
        # LR [ ]              | s: 0
        #    L R [   ]        | s: 1
        #        L   R [ ]    | s: 2
        #              L R [] | s: 3
        #                  LR | s: 4
        # Time: O(n) | Space: O(1)
        n = len(nums)
        left, right = 0, 0
        jumps = 0

        while right < n - 1:
            maxRight = right + 1
            for i in range(left, right + 1):
                maxRight = max(maxRight, i + nums[i])

            left, right = right + 1, maxRight
            jumps += 1

        return jumps
