class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time: O(t) | Space: O(t)
        counter = {}  # Mapping task -> count
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1

        max_freq = max(counter.values())
        max_count = 0
        for count in counter.values():
            if count == max_freq:
                max_count += 1

        most_freq_cycles = (max_freq - 1) * (n + 1) + max_count
        return max(most_freq_cycles, len(tasks))
