class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # nums: [2 5 6]
        # 2: 0010
        # 5: 0101
        # 6: 0110
        # [2 5 6]
        #  ^ | [] [2]
        #    ^ | [] [5]
        #      ^ | [] [6]
        #      ^ | [5] [5 6]
        #    ^ | [2] [2 5]
        #      ^ | [2] [2 6]
        #      ^ | [2 5] [2 5 6]
        # [2 5 6]
        # 2:  0  0  1  0
        # 4:  0  1  0  0
        # 6:  0  1  1  0
        #     -  -  -  -
        # 0   1 .5 .5  1
        # 1   0 .5 .5  0
        # combinations: 2**3
        # _ _ _ _
        # ^ | 1 * 0
        #   ^ | 1 * 2**(3-1)
        #     ^ | 1 * 2**(3-1)
        #       ^ | 1 * 0
        # (2**2 + 2**1) * 2**(3-1)
        # or(nums) * 2**(n - 1)
        # or(nums) << (n - 1)
        # Time: O(n) | Space: O(1)
        result = 0
        for num in nums:
            result |= num
        return result << (len(nums) - 1)
