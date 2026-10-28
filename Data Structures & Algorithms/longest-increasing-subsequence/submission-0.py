class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n: [9 1 4 2 3 3 7]
        #     ^ - - - - - - | 1
        #     - ^ - ^ ^ - ^ | 4*
        #     - - ^ - - - ^ | 2
        #     - - - ^ ^ - ^ | 3
        #     - - - - ^ - ^ | 2
        #     - - - - - ^ ^ | 2
        #     - - - - - - ^ | 1
        # dp(i, prev_min) = max(
        #     (1 if nums[j] > prev_min else 0) + dp(i + j, nums[j]) for j in range(i, n)
        # )
        # Dynamic Programming
        # Time: O(n * max(nums)) | Space: O(n * max(nums))
        n = len(nums)
        cache = {}

        def dp(i: int, prev_min: int) -> int:
            if i >= n:
                return 0

            if (i, prev_min) in cache:
                return cache[(i, prev_min)]

            cache[(i, prev_min)] = dp(i + 1, prev_min)
            if nums[i] > prev_min:
                cache[(i, prev_min)] = max(
                    cache[(i, prev_min)],
                    1 + dp(i + 1, nums[i]),
                )

            return cache[(i, prev_min)]

        return dp(0, -float('inf'))
