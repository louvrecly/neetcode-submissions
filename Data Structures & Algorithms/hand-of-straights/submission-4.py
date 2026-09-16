class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Time: O(n log n) | Space: O(n)
        if len(hand) % groupSize:
            return False

        counter = {}
        for num in hand:
            counter[num] = counter.get(num, 0) + 1

        heapq.heapify(hand)
        while hand:
            smallest = heapq.heappop(hand)
            if not counter.get(smallest, 0):
                continue

            for i in range(groupSize):
                num = smallest + i
                if not counter.get(num, 0):
                    return False
                counter[num] -= 1

        return True
