class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1 2 4 6]
        # [2*4*6 1*4*6 1*2*6 1*2*4]
        # [48 24 12 8]
        # Brute Force
        # Time: O(n ** 2) | Space: O(1)
        # ====================
        # [1 2 4 6]
        # prefix: [1 1 2 8]
        # suffix: [48 24 6 1]
        # output: [48 24 12 8]
        # [-1 0 1 2 3]
        # prefix: [1 -1 0 0 0]
        # suffix: [0 6 6 3 1]
        # output: [0 -6 0 0 0]
        # Prefix & Suffix Products
        # Time: O(n) | Space: O(n)
        n = len(nums)
        prefixProducts = [1] * n
        suffixProducts = [1] * n

        for i in range(1, n):
            prefixProducts[i] = prefixProducts[i - 1] * nums[i - 1]
            suffixProducts[n - i - 1] = suffixProducts[n - i] * nums[n - i]

        return [prefixProducts[i] * suffixProducts[i] for i in range(n)]
