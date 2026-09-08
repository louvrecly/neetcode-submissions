class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # [2 3 1 3 2]
        # { 2: 2, 3: 2, 1: 1 }
        # [1] [2, 3]
        counter = Counter(nums)
        return sorted(nums, key=lambda num: (counter[num], -num))
        # Frequency Bucket Sort
        # # Time: O(n * log n) | Space: O(n)
        # counter = Counter(nums)
        # print(f"counter: {counter}")

        # freqBuckets = [[] for _ in range(len(nums))]
        # for num, count in counter.most_common()[::-1]:
        #     freqBuckets[count - 1].append(num)

        # result = []
        # for i in range(len(nums)):
        #     freqBuckets[i].sort()
        #     while freqBuckets[i]:
        #         num = freqBuckets[i].pop()
        #         result.extend([num] * (i + 1))
            
        # return result