class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # a: 5 | c: [1 2 5]
        # [1 1 1 1 1]
        # [1 1 1 2]
        # [1 2 2]
        # [5]
        #                 0
        #              /  |\
        #             1   2 5
        #          /  |\  |\*
        #         2   3 6 4 7
        #      /  |\  |\  |\
        #     3   4 7 5 8 6 9
        #    /|\  |\  *
        #   4 5 8 6 9
        #  /|\*
        # 5 6 9
        # *
        # dp(i, j) = dp(i - coins[j], j) + dp(i, j + 1)
        #    | 1 | 2 | 5 |
        # ---+---+---+---+
        #  5 | 4 | 1 | 1 |
        # ---+---+---+---+
        #  4 | 3 | 1 | 0 |
        # ---+---+---+---+
        #  3 | 2 | 0 | 0 |
        # ---+---+---+---+
        #  2 | 2 | 1 | 0 |
        # ---+---+---+---+
        #  1 | 1 | 0 | 0 |
        # ---+---+---+---+
        #  0 | 1 | 1 | 1 |
        # ---+---+---+---+
        # Time: O(m * n) | Space: O(m)
        n = len(coins)
        memo = [[1 if i == 0 else 0 for i in range(amount + 1)]] * 2

        for j in range(n - 1, -1, -1):
            for i in range(1, amount + 1):
                memo[0][i] = memo[0][i]
                if i - coins[j] >= 0:
                    memo[0][i] += memo[1][i - coins[j]]
            for i in range(1, amount + 1):
                memo[0][i] = memo[1][i]

        return memo[1][amount]
