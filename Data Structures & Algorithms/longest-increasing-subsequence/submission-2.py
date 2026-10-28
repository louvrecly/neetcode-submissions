class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # nums: [0 3 1 3 2 3]
        # 0 3 | 0 1 2 3 | 0 3 | 0 2 3 | 0 3 | 0 -> 4
        # 3 -> 1
        # 1 3 | 1 2 3 | 1 3 | 1 -> 3
        # 3 -> 1
        # 2 3 | 2 -> 2
        # 3 -> 1
        # dp(i, j) = max(1 + dp(i + 1, nums[i]), dp(i + 1, j)) if nums[i] > j else dp(i + 1, j)
        # Time: O(n max(nums)) | Space: O(n max(nums))
        n = len(nums)
        memo = {}

        def dfs(i: int, j: int) -> int:
            if i >= n:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
            if nums[i] > j:
                memo[(i, j)] = max(1 + dfs(i + 1, nums[i]), dfs(i + 1, j))
                return memo[(i, j)]

            memo[(i, j)] = dfs(i + 1, j)
            return memo[(i, j)]

        return dfs(0, -float('inf'))
