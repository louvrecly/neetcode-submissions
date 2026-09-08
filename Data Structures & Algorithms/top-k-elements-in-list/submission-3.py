class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1 2 2 3 3 3] | k: 2
        # 3: 3 <--
        # 2: 2 <--
        # 1: 1
        # [1 3 3 2 3 1] | k: 2
        # 3: 3 <--
        # 1: 2 <--
        # 2: 1
        # Time: O(n) | Space: O(n)
        # Count all elements in hash map { num: count }
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        # Init max heap with (count, num)
        maxHeap = []
        for num, count in counter.items():
            heapq.heappush(maxHeap, (-count, num))

        # Init result as empty list
        result = []

        # Iterate while k greater than 0
        while k > 0:
            # Pop num from heap -> add to result list
            _, num = heapq.heappop(maxHeap)
            result.append(num)
            # Decrement k by 1
            k -= 1

        # Return result
        return result
