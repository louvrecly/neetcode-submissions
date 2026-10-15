class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # nums: [4 2 3 7]
        # [1 4 2 3 7 1]
        #    L     R   | dp(1,4) = max(
        #    ^ | 1*4*1 + dp(1,0) + dp(2,4)
        #      ^ | 1*2*1 + dp(1,1) + dp(3,4)
        #        ^ | 1*3*1 + dp(1,2) + dp(4,4)
        #          ^ | 1*7*1 + dp(1,3) + dp(5,4)
        #              | )
        # dp(L,R) = max(
        #     nums[L-1]*nums[i]*nums[R+1] +
        #     dp(L,i-1) +
        #     dp(i+1,R) for i in range(L,R+1)
        # )
        # Time: O(n^3) | Space: O(n^2)
        nums.insert(0, 1)
        nums.append(1)
        memo = {}

        def dp(left: int, right: int) -> int:
            if left > right:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]
            memo[(left, right)] = max((
                nums[left - 1] * nums[i] * nums[right + 1] +
                dp(left, i - 1) +
                dp(i + 1, right) for i in range(left, right + 1)
            ))
            return memo[(left, right)]

        return dp(1, len(nums) - 2)
