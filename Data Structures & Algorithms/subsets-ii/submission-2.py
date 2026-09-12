class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # [1 2 1]
        # sorted: [1 1 2]
        #          ^ | [1] []
        #            ^ | [1 1] [1] []
        #              ^ | [1 1 2] [1 1] [1 2] [1] []
        # Time: O(2 ** n) | Space: O(2 ** n)
        nums.sort()
        n = len(nums)
        curr = []
        results = []

        def backtrack(i: int) -> None:
            if i >= n:
                results.append(curr.copy())
                return

            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()

            while i + 1 < n and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return results
