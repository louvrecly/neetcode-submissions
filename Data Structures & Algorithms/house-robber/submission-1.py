class Solution:
    def rob(self, nums: List[int]) -> int:
        # [1 1 3 3]
        #  R   R   | 1+3=4
        #    R   R   | 1+3=4
        # [2 9 8 3 6]
        #  R   R   R | 2+8+6=16
        #  R     R   | 2+3=5
        #    R   R   | 9+3=11
        #    R     R | 9+6=15
        #                         []
        #              /                      \
        #            [2]                       []
        #          /      \               /          \ 
        #      [2 8]       [2]         [9]            []
        #       /  \        / \        / \          /    \
        # [2 8 6]  [2 8] [2 3] [2] [9 3] [9]      [8]     []
        #                      / \       / \      / \     / \
        #                  [2 6] [2] [9 6] [9] [8 6] [8] [3] []
        # dp(i) = max(nums[i] + dp(i + 2), dp(i + 1))
        # Time: O(n) | Space: O(1)
        n = len(nums)
        memo1, memo2 = nums[-1], 0

        for i in range(n - 2, -1, -1):
            temp = max(memo1, nums[i] + memo2)
            memo1, memo2 = temp, memo1

        return memo1
