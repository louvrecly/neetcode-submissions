class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1 2 1 0 4 2 6] | k: 3
        #  L   R | m: 2 | g: 2
        #    L   R | m: 2 | g: 2
        #      L   R | m: 4 | g: 4
        #        L   R | m: 4 | g: 4
        #          L   R | m: 6 | g: 6
        # [1 2 1 0 4 2 6] | k: 3
        #  L   R | l: max(1,2,1)=2 | g: 2
        #    L   R | l: max(1,2,1)=2 | g: 2
        # Time: O(k log k + (n - k) log k) | Space: O(n + k)
        n = len(nums)
        counter = {}  # Mapping num -> count
        max_heap = []
        for i in range(k):
            if nums[i] not in counter:
                heapq.heappush_max(max_heap, nums[i])
            counter[nums[i]] = counter.get(nums[i], 0) + 1
        output = [max_heap[0]]

        for right in range(k, n):
            left = right - k + 1
            counter[nums[left - 1]] -= 1
            while max_heap and counter.get(max_heap[0], 0) == 0:
                heapq.heappop_max(max_heap)

            output.append(max(max_heap[0] if max_heap else nums[right], nums[right]))
            if counter.get(nums[right], 0) == 0:
                heapq.heappush_max(max_heap, nums[right])

            counter[nums[right]] = counter.get(nums[right], 0) + 1

        return output
