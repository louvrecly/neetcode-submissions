class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # t: [X X Y Y] | n: 2
        # X > Y > _ > X > Y | c: 5
        # t: [A A A B C] | n: 3
        # A > B > C > _ > A > _ > _ > _ > A | c: 9
        # t: [A A A B B C D] | n: 2
        # A > B > C > A > B > D > A | c: 7
        # {A: 3, B: 2, C: 1, D: 1}
        # maxH: [(3 A) (2 B) (1 C) (1 D)] | - | q: [N N] | c: 0
        # maxH: [(2 B) (1 C) (1 D)] | (3 A) | q: [N (2 A)] | c: 1
        # maxH: [(1 C) (1 D)] | (2 B) | q: [(2 A) (1 B)] | c: 2
        # maxH: [(1 C) (1 D)] | (2 A) | q: [(1 B) (1 A)] | c: 3
        # maxH: [(1 C) (1 D)] | (1 B) | q: [(1 A) N] | c: 4
        # maxH: [(1 C) (1 D)] | (1 A) | q: [N N] | c: 5
        # maxH: [(1 D)] | (1 C) | q: [N N] | c: 6
        # maxH: [] | (1 D) | q: [N N] | c: 7
        # Time: O(nt log t) | Space: O(nt)
        counter = {}  # Mapping task -> count
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1

        max_heap = [(count, task) for task, count in counter.items()]
        heapq.heapify_max(max_heap)
        cooling = {}  # Mapping cycle -> (count, task)
        cycles = 0

        while max_heap or len(cooling):
            cycles += 1
            if cycles in cooling:
                task = cooling[cycles]
                heapq.heappush_max(max_heap, task)
                del cooling[cycles]

            if not max_heap:
                continue

            count, task = heapq.heappop_max(max_heap)
            if count > 1:
                cooling[cycles + n + 1] = (count - 1, task)

        return cycles
