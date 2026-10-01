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

        def backtrack(op: int, cl: int) -> None:
            if op == 0 and cl == 0:
                result.append(''.join(combo))
                return

            if op > 0:
                combo.append('(')
                backtrack(op - 1, cl)
                combo.pop()

            if cl > op:
                combo.append(')')
                backtrack(op, cl - 1)
                combo.pop()

        backtrack(n, n)
        return result
