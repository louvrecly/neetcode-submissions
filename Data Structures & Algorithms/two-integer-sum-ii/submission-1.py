class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1 2 4 4 5 7] | t: 7
        #  L         R | sum: 8 > 7
        #  L       R | sum: 6 < 7
        #    L     R | sum: 7 = 7
        # Time: O(n) | Space: O(1)
        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
