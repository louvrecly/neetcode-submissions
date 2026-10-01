class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n: 1
        # ()
        # n: 3
        # ()()() | (()()) | ((())) | ()(()) | (())()
        # n: 2
        # (()) | ()()
        #         [ ]               bt(2, 2)
        #         / \
        #       [(]                bt(1, 2)
        #     /      \
        #  [((]      [()]       bt(0, 2) bt(1, 1)
        #  /  \       / \ 
        #     [(()]     [()(]        bt(0, 1)   bt(0, 1)
        #      / \       / \
        #        [(())]    [()()]        bt(0, 0)
        # Time: O(2^n) | Space: O(2^n)
        result = []
        combo = []

        def backtrack(opening: int, closing: int) -> None:
            if opening == 0 and closing == 0:
                result.append(''.join(combo))
                return

            if opening > 0:
                combo.append('(')
                backtrack(opening - 1, closing)
                combo.pop()

            if closing > opening:
                combo.append(')')
                backtrack(opening, closing - 1)
                combo.pop()

        backtrack(n, n)
        return result
