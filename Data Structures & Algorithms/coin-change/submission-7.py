class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time: O(n amount) | Space: O(amount)
        cache = [amount + 1] * (amount + 1)
        cache[0] = 0

        for coin in coins:
            for i in range(amount + 1):
                if i - coin >= 0:
                    cache[i] = min(cache[i], 1 + cache[i - coin])

        return cache[amount] if cache[amount] <= amount else -1
