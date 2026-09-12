class Solution:
    def rob(self, nums: List[int]) -> int:
        # [3 4 3]
        #  ^ x x | 3
        #  x ^ x | 4
        #  x x ^ | 3
        # [2 9 8 3 6]
        #  ^ x     x | 2
        #  x ^ x     | 9
        #    x ^ x   | 8
        #      x ^ x | 3
        #  x     x ^ | 6
        #                     * [2 9 8 3 6]
        #          /                      \
        #   [8 3] 2                        0 [9 8 3 6]
        #        / \              /                  \
        #   [] 10   2 [3]  [3 6] 9                    0 [8 3 6]
        #          / \          / \              /         \
        #      [] 5   2 [] [] 11   9 [6]    [6] 8           0 [3 6]
        #                         / \          / \         / \
        #                    [] 15   9 [] [] 14   8 [] [] 3   0 [6]
        #                                                    / \
        #                                                [] 6   0 []
        # bt(i, curr, nums):
        #     curr.append(nums[i])
        #     bt(i + 2, curr, nums)
        #     curr.pop()
        #     bt(i + 1, curr, nums)
        # dp(i, noLast) = max(dp(i + 2, noLast) + nums[i], dp(i + 1, noLast))
        # Time: O(n) | Space: O(n)
        n = len(nums)
        memo = {}

        def dp(i: int, forbidLast: bool=False) -> int:
            if i >= n:
                return 0

            if forbidLast and i >= n - 1:
                return 0

            if (i, forbidLast) in memo:
                return memo[(i, forbidLast)]

            memo[(i, forbidLast)] = max(
                dp(i + 2, True if i == 0 else forbidLast) + nums[i],
                dp(i + 1, forbidLast)
            )
            return memo[(i, forbidLast)]

        return dp(0)
