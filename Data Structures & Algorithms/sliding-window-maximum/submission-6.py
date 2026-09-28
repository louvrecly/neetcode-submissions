class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Time: O((n - k) * k) | Space: O(k)
        n = len(nums)
        result = [max(nums[:k])]
        left = 1

        for right in range(k, n):
            prev_num = nums[left - 1]
            new_num = nums[right]
            if new_num >= result[-1]:
                result.append(new_num)
            elif prev_num < result[-1]:
                result.append(result[-1])
            else:
                result.append(max(nums[left:right + 1]))
            left += 1

        return result
