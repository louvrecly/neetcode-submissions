class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Time: O(n * sum(nums)) | Space: O(n * sum(nums))
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        n = len(nums)

        def possibleSumsOfSubArray(i: int) -> Set[int]:
            if i == n - 1:
                return set([0, nums[i]])

            sumSets = possibleSumsOfSubArray(i + 1)
            for num in sumSets.copy():
                sumSets.add(num + nums[i])

            return sumSets

        return target in possibleSumsOfSubArray(0)
