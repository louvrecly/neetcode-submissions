class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Time: O(n * sum(nums)) | Space: O(n * sum(nums))
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        n = len(nums)
        cache = [set() for _ in range(n)]

        def possibleSumsOfSubArray(i: int) -> Set[int]:
            if i in cache:
                return cache[i]

            if i == n - 1:
                cache[i] = set([0, nums[i]])
                return cache[i]

            sumSets = possibleSumsOfSubArray(i + 1)
            for num in sumSets.copy():
                sumSets.add(num + nums[i])

            cache[i] = sumSets
            return cache[i]

        return target in possibleSumsOfSubArray(0)
