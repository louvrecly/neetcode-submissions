class UnionFind:
    def __init__(self, size: int):
        self.roots = [i for i in range(size)]
        self.count = size

    def find(self, node: int) -> int:
        root = node
        while root != self.roots[root]:
            root = self.roots[root]

        pointer = node
        while self.roots[pointer] != root:
            nextNode = self.roots[pointer]
            self.roots[pointer] = root
            pointer = self.roots[nextNode]

        return root

    def union(self, node1: int, node2: int) -> None:
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return

        if root1 < root2:
            self.roots[root1] = root2
        else:
            self.roots[root2] = root1
        self.count -= 1

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Time: O(n^2 log n) | Space: O(n^2)
        edges = []
        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                xi, yi = points[i]
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                heapq.heappush(edges, (dist, i, j))
                heapq.heappush(edges, (dist, j, i))

        unionFind = UnionFind(n)
        cost = 0
        while edges and unionFind.count > 1:
            dist, i, j = heapq.heappop(edges)
            if unionFind.find(i) == unionFind.find(j):
                continue
            unionFind.union(i, j)
            cost += dist

        return cost
