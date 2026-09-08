class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # [1 2 + 3 * 4 -]
        # (1 + 2) * 3 - 4 = 5
        # 1 | [1] | r: 0
        # 2 | [1 2] | r: 0
        # + | [1 2] | r: 1 + 2 = 3
        # 3 | [3 3] | r: 3
        # * | [3 3] | r: 3 * 3 = 9
        # 4 | [9 4] | r: 9
        # - | [9 4] | r: 9 - 4 = 5
        # N | [5] | r: 5
        # Stack
        # Time: O(n) | Space: O(1)
        stack = []
        operators = set(['+', '-', '*', '/'])

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue

            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))

        return stack[0]
