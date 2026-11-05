class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # # Time: O(n) | Space: O(1)
        # result = []
        # for _ in range(2):
        #     for num in nums:
        #         result.append(num)
        # return result
        # Time: O(n) | Space: O(1)
        n = len(nums)
        result = [0] * 2 * n

        for i, num in enumerate(nums):
            result[i] = result[i + n] = num

        return result
