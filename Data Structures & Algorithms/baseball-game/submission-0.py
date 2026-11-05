class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # ops: [1 2 + C 5 D]
        # [1 2 + C 5 D]
        #  ^ | 1 | [1]
        #    ^ | 2| [1 2]
        #      ^ | + | [1 2 3]
        #        ^ | C | [1 2]
        #          ^ | 5 | [1 2 5]
        #            ^ | D | [1 2 5 10] => 18
        # ops: [5 D + C]
        # [5 D + C]
        #  ^ | 5 | [5]
        #    ^ | D | [5 10]
        #      ^ | + | [5 10 15]
        #        ^ | C | [5 10] => 15
        # Time: O(n) | Space: O(n)
        scores = []

        for op in operations:
            if op == "C":
                if not scores:
                    raise Exception("Invalid Operation")
                scores.pop()
                continue

            if op == "D":
                if not scores:
                    raise Exception("Invalid Operation")
                scores.append(scores[-1] * 2)
                continue

            if op == "+":
                if len(scores) < 2:
                    raise Exception("Invalid Operation")
                a = scores[-2]
                b = scores[-1]
                scores.append(a + b)
                continue

            score = int(op)
            scores.append(score)

        return sum(scores)
