class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # n: [2 4 -3 5]
        # [2 4 -3 5]
        #  LR | p: 2 | m: 2
        #  L R | p: 8 | m: 8
        #  L    R | p: -24 | m: 8
        #  L      R | p: -120 | m: 8
        #    L    R | p: -60 | m: 8
        #       L R | p: -15 | m: 8
        #         LR | p: 5 | m: 8
        # [2 4 -3 5]
        # pref: [2 8 -24 -120]
        # suff: [-120 -60 -15 5]
        # sliding window
        # dp(l, r) = max(
        #     dp(l, r - 1) * nums[r],  # take right, shrink to the left
        #     dp(l + 1, r) * nums[l],  # take left, shrink to the right
        #     dp(l, r - 1),  # skip right, shrink to the left
        #     dp(l + 1, r)  # skip left, shrink to the right
        # )
        # Time: O(n) | Space: O(n)
        max_p, min_p = 1, 1
        max_prod = -float('inf')

        for num in nums:
            temp = max_p
            max_p = max(num, num * temp, num * min_p)
            min_p = min(num, num * temp, num * min_p)
            max_prod = max(max_prod, max_p, min_p)

        return max_prod
