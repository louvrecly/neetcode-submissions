class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Time: O(n log k) | Space: O(n + k)
        n = len(nums)
        counter = {}  # Mapping num -> count
        window = []  # max heap

        for i in range(k):
            if counter.get(nums[i], 0) == 0:
                heapq.heappush_max(window, nums[i])
            counter[nums[i]] = counter.get(nums[i], 0) + 1

        result = [window[0]]

        for right in range(k, n):
            left = right - k + 1

            # Remove prev num
            prev_num = nums[left - 1]
            counter[prev_num] -= 1
            while window and counter.get(window[0], 0) == 0:
                heapq.heappop_max(window)

            # Add new num
            new_num = nums[right]
            if counter.get(new_num, 0) == 0:
                heapq.heappush_max(window, new_num)
            counter[new_num] = counter.get(new_num, 0) + 1

            # Compute current max
            result.append(window[0])

        return result
