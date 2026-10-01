class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Time: O(2^n) | Space: O(2^n)
        result = []

        def backtrack(combo: str, opening: int, closing: int) -> None:
            if len(combo) == n * 2:
                result.append(combo)
                return

            if opening > 0:
                backtrack(combo + '(', opening - 1, closing)

            if closing > opening:
                backtrack(combo + ')', opening, closing - 1)

        backtrack('', n, n)
        return result
