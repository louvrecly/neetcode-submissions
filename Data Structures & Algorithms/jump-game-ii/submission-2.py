class Solution:
    def jump(self, nums: List[int]) -> int:
        # [2 4 1 1 1 2 2 3 1] | n: 9
        #  ^ * *              | i: 0 | j: [1,2] | des, pot: (1,5) (2,3) | next: 1
        #    ^ * * * *        | i: 1 | j: [1,4] | des, pot: (2,3) (3,4) (4,5) (5,7) | next: 5
        #            ^ * *    | i: 5 | j: [1,2] | des, pot: (6,8) (7,10)=(7,8) | next: 7
        #                ^ *  | i: 7 | j: [1,3] | des, pot: (8,9)=(8,8) | next: 8
        #                  ^  | i: 8 | j: [] | des, pot: () | next: -
        # maxHeap
        # Time: O(n) | Space: O(n)
        n = len(nums)
        maxHeap = []  # (potentialDest, dest): (i + j + nums[i + j], i + j)
        i = 0
        stepsCount = 0

        while i < n - 1:
            for j in range(1, nums[i] + 1):
                dest = min(n - 1, i + j)
                potentialDest = min(n - 1, dest + nums[dest])
                heapq.heappush(maxHeap, (-potentialDest, -dest))

            i = -maxHeap[0][1]
            maxHeap.clear()
            stepsCount += 1

        return stepsCount
