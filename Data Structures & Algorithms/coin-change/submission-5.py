class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time: O(n amount) | Space: O(n amount)
        n = len(coins)
        memo = {}  # Mapping (i, target) -> count

        def dp(i: int, target: int) -> int:
            if target < 0 or i >= n:
                return float('inf')

            if target == 0:
                return 0

            if (i, target) in memo:
                return memo[(i, target)]

            memo[(i, target)] = min(
                1 + dp(i, target - coins[i]),
                1 + dp(i + 1, target - coins[i]),
                dp(i + 1, target)
            )
            return memo[(i, target)]

        result = dp(0, amount)
        return result if result <= amount else -1
