class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #        [ ]            |             [1 2 3]
        #    /    |    \        |      /         |         \
        #   1     2     3       |   [2 3]      [1 3]      [1 2]
        #  / \   / \   / \      |   /   \      /   \      /   \
        # 2   3 1   3 1   2     | [3]   [2]  [3]   [1]  [2]   [1]
        # |   | |   | |   |     |  |     |    |     |    |     |
        # 3   2 3   1 2   1     | [ ]   [ ]  [ ]   [ ]  [ ]   [ ]
        # Time: O(n! * n ** 2) | Space: O(n! * n)
        self.results = []
        self._backtrack([], nums)
        return self.results

    def _backtrack(self, curr: List[int], nums: List[int]) -> None:
        # Time: O(n! * n ** 2) | Space: O(n! * n)
        n = len(nums)

        if n == 0:
            self.results.append(curr.copy())
            return

        for i in range(n):
            num = nums[i]
            curr.append(num)
            self._backtrack(curr, nums[:i] + nums[i + 1:])
            curr.pop()
