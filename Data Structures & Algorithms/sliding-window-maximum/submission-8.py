class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1 2 1 0 4 2 6] | k: 3
        #  L   R | p: - | d: [2 1] | m: 2 | r: [2]
        #    L   R | p: 1 | d: [2 1 0] | m: 2 | r: [2 2]
        #      L   R | p: 2 | d: [4] | m: 4 | r: [2 2 4]
        #        L   R | p: 1 | d: [4 2] | m: 4 | r: [2 2 4 4]
        #          L   R | p: 0 | d: [6] | m: 6 | r: [2 2 4 4 6]
        # Monotonic Decreasing Queue (Deque)
        # Time: O(n) | Space: O(k)
        n = len(nums)
        queue = deque([])

        for i in range(k):
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])

        result = [queue[0]]

        for right in range(k, n):
            left = right - k + 1

            prev_num = nums[left - 1]
            if queue[0] == prev_num:
                queue.popleft()

            new_num = nums[right]
            while queue and new_num > queue[-1]:
                queue.pop()

            queue.append(new_num)
            result.append(queue[0])

        return result
