class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Time: O(n * log n) | Space: O(1)
        stones.sort()

        while len(stones) > 1:
            stone1 = stones.pop()
            stone2 = stones.pop()
            remain = stone1 - stone2
            if remain > 0:
                stones.append(remain)
                stones.sort()

        return stones.pop() if stones else 0
