class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # d: [1 2 3 4]
        # [1 2 3 4]
        #        ^ | 4 + 1 = 5
        # [1 2 3 5]
        # d: [9 9 9]
        # [9 9 9]
        #      ^ | 9 + 1 = 10
        # [9 9 0]
        #    ^ | 9 + 1 = 10
        # [9 0 0]
        #  ^ | 9 + 1 = 10
        # [1 0 0 0]
        #  ^ | 0 + 1 = 1
        # Time: O(n) | Space: O(1)
        i = len(digits) - 1
        carry = 1

        while carry and i >= 0:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            i -= 1

        if carry:
            digits.insert(0, 1)

        return digits
