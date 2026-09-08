class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # times: [[1 2 1] [2 3 1] [1 4 4] [3 4 1]] | n: 4 | k: 1
        #     1 <----
        #  1 / \
        #   2   |
        # 1 |   | 4
        #   3   |
        #  1 \ /
        #     4
        # adj: { 1: [(2,1) (4,4)], 2: [(3,1)], 3: [(4,1)] }
        # curr: 1 | [(2,1) (4,4))] | v: [1] | t: 0
        #   curr: 2 | [(3,1)] | v: [1 2] | t: 1
        #     curr: 3 | [(4,1)] | v: [1 2 3] | t: 2
        #       curr: 4 | [] | v: [1 2 3 4] | t: 3
        #   curr: 4 | [] | v: [1 4] | t: 4
        # output: 3
        # ======================================================
        # times: [[1 2 1] [2 3 1]] | n: 3 | k: 2
        #  1
        #  | 1
        #  2 <----
        #  | 1
        #  3
        # adj: { 1: [(2,1)], 2: [(3,1)] }
        # curr: 2 | [(3,1)] | v: [2] | t: 0
        #   curr: 3 | [] | v: [2 3] | t: 1
        # output: -1
        # ======================================================
        # times: [[1 2 1] [2 3 1] [2 4 4] [3 4 2]] | n: 4 | k: 2
        #     1
        #   1 |
        #     2 <---
        #  1 / \
        #   3   | 4
        #  2 \ /
        #     4
        # adj: { 1: [(2,1)], 2: [(3,1) (4,4)], 3: [(4,2)] }
        # curr: 2 | [(3,1) (4,4)] | v: [2] | t: 0
        #   curr: 4 | [] | v: [2 4] | t: 4 | len(v): 2 < 4 -> -1
        #   curr: 3 | [4,2] | v: [2 3] | t: 1
        #     curr: 4 | [] | v: [2 3 4] | t: 3 | len(v): 3 < 4 -> -1
        # ======================================================
        # times: [[1 2 1] [2 3 2] [1 3 2]] | n: 3 | k: 1
        #    1 <---
        # 1 / \
        #  2   | 2
        # 2 \ /
        #    3
        # Djikstra Algorithm -> BFS + min cummulative costs neighbor
        # Time: O(E * log V) | Space: O(E + V)
        adjacency = defaultdict(list)

        for node, neighbor, time in times:
            adjacency[node].append((neighbor, time))
        print(f"adjacency: {dict(adjacency)}")

        minHeap = [(0, k)]  # time, node
        visited = set()  # visited nodes
        minTime = 0

        while len(visited) < n and minHeap:
            time, node = heapq.heappop(minHeap)
            print("=" * 5)
            print(f"time: {time} | node: {node} | visited: {visited}")
            if node in visited:
                continue

            visited.add(node)
            print(f"minTime: {minTime} | time: {time}")
            minTime = max(minTime, time)
            print(f"adjacency[{node}]: {adjacency[node]}")

            for neighbor, cost in adjacency[node]:
                print("-" * 5)
                print(f"neighbor: {neighbor} | cost: {cost}")
                if neighbor not in visited:
                    heapq.heappush(minHeap, (time + cost, neighbor))
                print(f"minHeap: {minHeap}")

        print("=" * 5)
        print(f"minTime: {minTime} | visited: {visited}")
        return minTime if len(visited) == n else -1
