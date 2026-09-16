class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Time: O(n log n) | Space: O(n)
        if len(hand) % groupSize:
            return False

        counter = {}
        for num in hand:
            counter[num] = counter.get(num, 0) + 1

        minHeap = list(counter.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(groupSize):
                num = first + i
                if not counter.get(num, 0):
                    return False

                counter[num] -= 1
                if not counter.get(num, 0):
                    if num != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True
