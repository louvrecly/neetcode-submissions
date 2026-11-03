class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Time: O(2 ^ n) | Space: O(2 ^ n)
        n = len(nums)
        diff = [sum(nums)]

        def dfs(i: int) -> bool:
            if diff[0] < 0:
                return False

            if i >= n:
                return diff[0] == 0

            diff[0] -= 2 * nums[i]
            result = dfs(i + 1)
            diff[0] += 2 * nums[i]
            return result or dfs(i + 1)

        return dfs(0)
