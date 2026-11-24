class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums: [1 2 3]
        #                       [ ]
        #                /                \
        #              [1]                [ ]
        #          /        \           /     \
        #      [1 2]        [1]       [2]     [ ]
        #       / \         / \       / \     / \
        # [1 2 3] [1 2] [1 3] [1] [2 3] [2] [3] [ ]
        # Time: O(2^n) | Space: O(2^n)
        n = len(nums)
        curr = []
        result = []

        def backtrack(i: int) -> None:
            if i >= n:
                result.append(curr.copy())
                return

            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()
            backtrack(i + 1)

        backtrack(0)
        return result
