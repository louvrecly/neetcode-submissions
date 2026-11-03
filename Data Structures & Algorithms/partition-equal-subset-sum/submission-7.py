class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Time: O(n * sum(nums)) | Space: O(sum(nums))
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        n = len(nums)
        sums_set = set([0, nums[n - 1]])

        for i in range(n - 2, -1, -1):
            if target in sums_set:
                return True

            for prev in sums_set.copy():
                num = prev + nums[i]
                if num == target:
                    return True

                sums_set.add(num)

        return False
