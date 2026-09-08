class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # a: 5 | c: [1 2 5]
        # [1 1 1 1 1]
        # [1 1 1 2]
        # [1 2 2]
        # [5]
        #                                       [0]
        #                               /        |  \
        #                             [1]       [2] [5]
        #                     /        | \      / \
        #                   [2]       [3] [6] [4] [7]
        #           /        |  \     / \  x  / \  x
        #         [3]       [4] [7] [5] [8] [6] [9]
        #       /  |  \     / \  x       x   x   x
        #     [4] [5] [8] [6] [9]
        #   /  |  \    x   x   x
        # [5] [6] [9]
        #      x   x
        # dp(i, j) = dp(i - coins[j], j) + dp(i, j + 1)
        # Time: O(m * n) | Space: O(m * n)
        n = len(coins)
        memo = {}  # Mapping (i, j) -> value

        def dp(i: int, j: int) -> int:
            if i < 0:
                return 0
            if j >= n:
                return 0
            if i == 0:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = dp(i - coins[j], j) + dp(i, j + 1)
            return memo[(i, j)]

        return dp(amount, 0)
