class Solution:
    def checkValidString(self, s: str) -> bool:
        # Time: O(n) | Space: O(1)
        open_range = [0, 0]

        for char in s:
            if char == "(":
                open_range[0] += 1
                open_range[1] += 1
                continue
            if char == "*":
                open_range[0] = max(0, open_range[0] - 1)
                open_range[1] += 1
                continue
            if char == ")":
                if open_range[1] == 0:
                    return False
                open_range[0] = max(0, open_range[0] - 1)
                open_range[1] -= 1

        min_open, max_open = open_range
        return min_open <= 0 <= max_open
