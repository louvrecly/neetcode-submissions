class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1 1 2 3] | t: 5
        # [2 3]
        # [1 1 2 3 5] | t: 5
        #  L       R  | 1 + 5 = 6 > 5
        #  L     R    | 1 + 3 = 4 < 5
        #    L   R    | 1 + 3 = 4 < 5
        #      L R    | 2 + 3 = 5 = 5
        # Time: O(n) | Space: O(1)
        n = len(numbers)
        left, right = 0, n - 1

        while left < right:
            current = numbers[left] + numbers[right]
            if current > target:
                right -= 1
            elif current < target:
                left += 1
            else:
                return [left + 1, right + 1]
