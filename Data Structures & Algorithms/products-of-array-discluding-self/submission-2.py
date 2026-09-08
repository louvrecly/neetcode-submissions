class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time: O(n) | Space: O(n)
        n = len(nums)
        product = 1
        zeroIndexes = []

        for i in range(n):
            if nums[i] == 0:
                zeroIndexes.append(i)
            else:
                product *= nums[i]

        output = [0] * n
        if len(zeroIndexes) > 1:
            return output

        if len(zeroIndexes) == 1:
            output[zeroIndexes[0]] = product
            return output

        for i in range(n):
            output[i] = product // nums[i]

        return output
