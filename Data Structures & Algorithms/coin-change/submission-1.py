class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # c: [1 5 10] | a: 12
        # 10 1 1 | 3
        # dp(i, a) = min(
        #     1 + dp(i, a-c[i]),  # Take current coin, stay
        #     1 + dp(i+1,a-c[i]),  # Take current coin, move on
        #     dp(i+1,a)  # Skip current coin, move on
        # )
        # Time: O(n*amount) | Space: O(n*amount)
        n = len(coins)
        memo = {}  # Mapping (i, target) -> count

        def dp(i: int, target: int) -> int:
            if target < 0 or i >= n:
                return amount + 1

            if target == 0:
                return 0

            if (i, target) in memo:
                return memo[(i, target)]

            memo[(i, target)] = min(
                1 + dp(i, target - coins[i]),  # take and stay
                1 + dp(i + 1, target - coins[i]),  # take and move on
                dp(i + 1, target)  # skip and move on
            )
            return memo[(i, target)]

        result = dp(0, amount)
        return result if result <= amount else -1
