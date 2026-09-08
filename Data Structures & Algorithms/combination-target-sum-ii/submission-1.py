class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # c: [9 2 2 4 6 1 5] | t: 8
        # [2 2 4]
        # [2 6]
        # [2 1 5]
        # o: [1 2 2 4 5 6 9] | t: 8
        #     ^ [         ] | [1] (8-1=7)
        #       ^ [       ] | [2] (8-2=6)
        #         ^ [     ] | [2] (8-2=6)
        #           ^ [   ] | [4] (8-4=4)

        #                          []
        #              +1  /              \
        #                [1]               []
        #          +2  /      \           /  \
        #         [1 2]        [1]      [2]  []
        #     +2   /    \     /   \     /  \ /\ /\
        #     [1 2 2] [1 2] [1 2] [1] [2 2]
        # Time: O(n * 2 ** n) | Space: O(n * 2 ** n)
        combos = []
        n = len(candidates)
        candidates.sort()

        def backtrack(i: int, combo: List[int], k: int) -> None:
            # print('=' * 5)
            # print(f"i: {i} | combo: {combo} | k: {k}")
            if k == 0:
                combos.append(combo.copy())
                # print(f"combo: {combo} | combos: {combos}")
                return

            if k < 0 or i >= n:
                return

            num = candidates[i]
            combo.append(num)
            backtrack(i + 1, combo, k - num)
            combo.pop()

            while i < n and candidates[i] == num:
                i += 1
            backtrack(i, combo, k)

        backtrack(0, [], target)
        return combos
