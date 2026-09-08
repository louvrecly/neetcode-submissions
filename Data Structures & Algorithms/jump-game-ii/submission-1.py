class Solution:
    def jump(self, nums: List[int]) -> int:
        # [2 4 1 1 1 1]
        #  ^ 1 2       | i: 0 | (i + j, nums[i + j]): [(1,4)=5 (2,1)=3] | j: 1
        #    ^ 1 2 3 4 | i: 1 | (i + j, nums[i + j]): [(2,1)=3 (3,1)=4 (4,1)=5 (5,1)=6] | j: 4
        #            ^ | i: 4 | (i + j, nums[i + j]): [(6,1)=7] | j: -
        # [2 1 2 1 0]
        #  ^ 1 2       | i: 0 | (i + j, nums[i + j]): [(1,1)=2 (2,2)=4] | j: 2
        #      ^ 1 2   | i: 2 | (i + j, nums[i + j]): [(3,1)=4 (4,0)=4] | j: 2
        # maxHeap
        # Time: O(n) | Space: O(n)
        n = len(nums)
        maxHeap = []  # Store (potential dest, dest): (i + j + nums[i + j], i + j)
        i = 0
        stepsCount = 0

        while i < n - 1:
            for j in range(1, nums[i] + 1):
                dest = min(n - 1, i + j)
                potentialDest = min(n - 1, dest + nums[dest])
                heapq.heappush(maxHeap, (-potentialDest, -dest))

            stepsCount += 1
            i = -maxHeap[0][1]
            maxHeap.clear()

        return stepsCount
