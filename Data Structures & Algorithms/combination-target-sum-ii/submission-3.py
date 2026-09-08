class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # c: [2 1 1 3 1] | t: 5
        # [1 1 1 2] [1 1 3] [2 3]
        # [1 1 1 2 3]
        #                    []
        #              /            \
        #            [1]             []
        #        /        \         /   \
        #     [1 1]       *[1]    *[1]    []
        #    /     \       /  \    / \    / \
        # [1 1 1] [1 1] [1 1] [1] [1] [] [1] []
        #    3      2     2    1   1   0  1  0
        # DFS + backtracking
        # Time: O(n * 2 ** n) | Space: O(n * 2 ** n)
        candidates.sort()
        n = len(candidates)
        combos = []

        def dfs(i: int, combo: List[int], subtotal: int) -> None:
            if subtotal == target:
                combos.append(combo.copy())
                return

            if i >= n or subtotal > target:
                return

            # include i-th candidate
            combo.append(candidates[i])
            dfs(i + 1, combo, subtotal + candidates[i])
            combo.pop()

            # exclude i-th candidate
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, combo, subtotal)

        dfs(0, [], 0)
        return combos