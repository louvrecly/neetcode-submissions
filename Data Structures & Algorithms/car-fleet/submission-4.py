class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Time: O(n log n) | Space: O(n)
        cars = sorted(zip(position, speed), reverse=True)
        prevArrival = 0
        count = 0

        for p, s in cars:
            arrival = (target - p) / s
            if arrival > prevArrival:
                count += 1
                prevArrival = arrival

        return count
