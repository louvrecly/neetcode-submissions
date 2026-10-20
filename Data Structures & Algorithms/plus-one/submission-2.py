class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Time: O(n) | Space: O(1)
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] %= 10

        return [1] + digits
