class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp(i, t) = min(
        #     1 + dp(i, t - coins[i]),
        #     1 + dp(i + 1, t - coins[i]),
        #     dp(i + 1, t)
        # )
        # Time: O(n amount) | Space: O(amount)
        n = len(coins)
        cache = [amount + 1] * (amount + 1)
        cache[0] = 0

        for i in range(n - 1, -1, -1):
            temp = [amount + 1] * (amount + 1)
            for j in range(amount + 1):
                temp[j] = cache[j]
                k = j - coins[i]
                if k >= 0:
                    temp[j] = min(temp[j], 1 + temp[k], 1 + cache[k])
            cache = temp

        return temp[amount] if temp[amount] <= amount else -1
