class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford Algorithm
        # Time: O(Ek) | Space: (V)
        # Initialize a cost map
        costs = [0 if i == src else float('Inf') for i in range(n)]
        # Iterate through every edge for k + 1 times
        for i in range(k + 1):
            # Copy the cost map to create a temp cost map
            temp = costs.copy()
            # Iterate through every edge
            for start, stop, price in flights:
                # If new lower cost found -> update to temp cost map
                temp[stop] = min(temp[stop], costs[start] + price)
            # Fill the cost map with temp values
            costs = [cost for cost in temp]
        # Return the cost map to destination
        return costs[dst] if costs[dst] != float('Inf') else -1
