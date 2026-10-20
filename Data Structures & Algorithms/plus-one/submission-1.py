class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Time: O(n) | Space: O(1)
        num = 0
        for i in range(len(digits)):
            num *= 10
            num += digits[i]

        num += 1
        result = []
        while num:
            result.append(num % 10)
            num //= 10

        result.reverse()
        return result
