class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Time: O(max(t, n)) | Space: O(t)
        arrivals = [None] * (target + 1)
        n = len(position)
        for i in range(n):
            p = position[i]
            s = speed[i]
            arrivals[p] = (target - p) / s

        prev = 0
        count = 0
        for i in range(target, -1, -1):
            if arrivals[i] is None:
                continue
            if arrivals[i] > prev:
                count += 1
                prev = arrivals[i]

        return count
