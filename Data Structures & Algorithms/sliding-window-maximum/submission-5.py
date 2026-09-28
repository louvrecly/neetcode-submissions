class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        l, r = 0, k
        max_num = max(nums[l:r])

        while r <= n:
            res.append(max_num)
            prev_num = nums[l]
            l += 1
            r += 1
            new_num = nums[r-1] if r<=n else -1
            if new_num > max_num:
                max_num = new_num
            elif max_num == prev_num and r<=n:
                max_num = max(nums[l:r])

        return res