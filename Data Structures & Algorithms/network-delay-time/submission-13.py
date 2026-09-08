class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # [
        #     1 -> 2: 1
        #     2 -> 3: 1
        #     1 -> 4: 4
        #     3 -> 4: 1
        # ]
        # n: 4 | k: 1
        #     1
        #  1 / \
        #   2   |
        # 1 |   | 4
        #   3   |
        #  1 \ /
        #     4
        #        [1]
        #       /  \
        #   [1 2]  [1 4] X (4)
        #     |
        #  [1 2 3]
        #     |
        # [1 2 3 4] O (3)
        # Djikstra's Algorithm
        # Time: O(E + V * log E) | Space: O(E + V)
        # Init adjacency list for each node { u: (v, t)[] }
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        # Init queue with node k with time
        queue = [(0, k)]  # min heap (time, node)
        visited = set()  # visited nodes (node)
        time = 0

        # Iterate nodes while visited < n or queue is non-empty
        while queue and len(visited) < n:
            # Dequeue min time node
            t, u = heapq.heappop(queue)
            # Mark node as visited
            if u in visited:
                continue

            visited.add(u)
            # Update time
            time = t
            # BFS unvisited neighbors with times to enqueue
            for v, t in adj[u]:
                if v not in visited:
                    heapq.heappush(queue, (t + time, v))

        # Return min time
        return time if len(visited) == n else -1
