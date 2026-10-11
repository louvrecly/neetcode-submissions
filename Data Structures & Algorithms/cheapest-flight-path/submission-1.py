class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Time: O(Ek) | Space: O(V)
        costs = [0 if i == src else float('Inf') for i in range(n)]

        for i in range(k + 1):
            temp = costs.copy()
            for start, stop, price in flights:
                temp[stop] = min(temp[stop], costs[start] + price)

            costs = [cost for cost in temp]

        return costs[dst] if costs[dst] < float('Inf') else -1
