class Solution:
    def isValid(self, s: str) -> bool:
        # [ ]
        # ^   | [ |
        #   ^ | ] | ]
        # ( [ { } ] )
        # ^           | ( |
        #   ^         | [ | )
        #     ^       | { | ) ]
        #       ^     | } | ) ] }
        #         ^   | ] | ) ]
        #           ^ | ) | )
        # Time: O(n) | Space: O(n)
        parenMap = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for char in s:
            if char in parenMap:
                stack.append(parenMap[char])
            else:
                if not stack or stack[-1] != char:
                    return False
                stack.pop()

        return len(stack) == 0
