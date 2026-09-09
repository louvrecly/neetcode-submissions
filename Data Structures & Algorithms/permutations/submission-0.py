class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # [1 2 3]
        # [
        #     [1 2 3]
        #     [1 3 2]
        #     [2 1 3]
        #     [2 3 1]
        #     [3 1 2]
        #     [3 2 1]
        # ]
        # [1 2 3]
        #        [ ]
        #    /    |    \
        #   1     2     3
        #  / \   / \   / \
        # 2   3 1   3 1   2
        # |   | |   | |   |
        # 3   2 3   1 2   1
        # Time: O(n ** 2) | Space: O(n ** 2)
        n = len(nums)
        results = []

        def backtrack(curr: List[int], nums: List[int]) -> None:
            m = len(nums)
            if m == 0:
                results.append(curr.copy())
                return

            for i in range(m):
                num = nums[i]
                curr.append(num)
                backtrack(curr, nums[:i] + nums[i + 1:])
                curr.pop()

        backtrack([], nums)
        return results
