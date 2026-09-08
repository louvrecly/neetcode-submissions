class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1 0 1 2 -1 -4]
        # [
        #     [-1 0 1]
        #     [-1 -1 2]
        # ]
        # [-1 0 1 2 -1 -4]
        # [-4 -1 -1 0 1 2]
        #   L           R | -4 + 2 = -2 | []
        #   L         M R | -2 + 1 = -1 < 0 | []
        #      L        R | -1 + 2 = 1 | []
        #      L  M     R | 1 - 1 = 0 = 0 | [-1 -1 2]
        #      L  M     R | 1 - 1 = 0 = 0 | [-1 -1 2]
        #         L     R | -1 + 2 = 1 | [-1 -1 2]
        #         L M   R | 1 + 0 = 1 > 0 | [-1 -1 2]
        #         L   R | -1 + 1 = 0 | [-1 -1 2]
        #         L M R | 0 + 0 = 0 | [-1 -1 2] [-1 0 1]
        # Time: O(n ** 2) | Space: O(n)
        nums.sort()
        n = len(nums)
        results = []

        for i in range(n):
            if nums[i] > 0:
                break

            if i and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                subtotal = nums[i] + nums[j] + nums[k]
                if subtotal < 0:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif subtotal > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    results.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return results
