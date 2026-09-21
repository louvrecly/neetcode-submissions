class Solution:
    def getSum(self, a: int, b: int) -> int:
        # a: 3 | b: 5
        # =======================[0]
        # a: 0 0 1 1
        # b: 0 1 0 1
        # -----------XOR: 0 1 1 0
        # -----------AND: 0 0 0 1
        # =======================[1]
        # a: 0 1 1 0
        # b: 0 0 1 0
        # -----------XOR: 0 1 0 0
        # -----------AND: 0 0 1 0
        # =======================[2]
        # a: 0 1 0 0
        # b: 0 1 0 0
        # -----------XOR: 0 0 0 0
        # -----------AND: 0 1 0 0
        # =======================[3]
        # a: 0 0 0 0
        # b: 1 0 0 0
        # -----------XOR: 1 0 0 0
        # -----------AND: 0 0 0 0
        # Time: O(1) | Space: O(1)
        mask = 0xFFFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry
        maxInt = 0x7FFFFFFF
        return a if a <= maxInt else ~(a ^ mask)
