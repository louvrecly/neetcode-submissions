class Solution:
    def checkValidString(self, s: str) -> bool:
        # s: (((*)
        # ( ( ( * )
        # ^ | (:1 *:0
        #   ^ | (:2 *:0
        #     ^ | (:3 *:0
        #       ^ | (:3 *:1
        #         ^ | (:2 *:1 | False
        # s: (*))
        # ( * ) )
        # ^ | (:1 *:0
        #   ^ | (:1 *:1
        #     ^ | (:0 *:1
        #       ^ | (:0 *:0 | True
        # s: (*)))
        # ( * ) ) )
        # ^ | (:1 *:0
        #   ^ | (:1 *:1
        #     ^ | (:0 *:1
        #       ^ | (:0 *:0
        #         ^ | (:0 *:0 | False
        # stack = []
        # counter = {"(": 0, "*": 0}

        # for char in s:
        #     print("=" * 5)
        #     print(f"char: {char} | stack: {stack} | counter: {counter}")
        #     if char == ")":
        #         if counter["("] + counter["*"] <= 0:
        #             return False
        #         popped = stack.pop()
        #         counter[popped] -= 1
        #         continue
        #     counter[char] += 1
        #     stack.append(char)

        # if len(stack) == 0:
        #     return True

        # first_open = stack.index("(")
        # return counter["("] <= counter["*"] - first_open
        # Time: O(n) | Space: O(n)
        counts = {"(": [], "*": []}

        for i, char in enumerate(s):
            if char == ")":
                if not counts["("] and not counts["*"]:
                    return False
                if counts["("]:
                    counts["("].pop()
                else:
                    counts["*"].pop()
            else:
                counts[char].append(i)

        if len(counts["*"]) < len(counts["("]):
            return False

        while counts["("]:
            if not counts["*"] or counts["*"][-1] < counts["("][-1]:
                return False
            counts["*"].pop()
            counts["("].pop()

        return True
