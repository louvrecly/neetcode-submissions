class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Time: O(n) | Space: O(n)
        n = len(nums)
        curr = []

        def dp(i: int) -> int:
            if i >= n:
                result = 0
                for num in curr:
                    result ^= num
                return result

            curr.append(nums[i])
            result = dp(i + 1)
            curr.pop()
            return result + dp(i + 1)

        return dp(0)
