class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Time: O(2 ** n + n * log n) | Space: O(2 ** n)
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

            while i < n - 1 and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return results
