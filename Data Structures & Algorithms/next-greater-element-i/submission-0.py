class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1: [4 1 2] | nums2: [1 3 4 2]
        # curr: 4 |                    ^ | -1
        # curr: 1 |                ^ | 3
        # curr: 2 |                      ^ | -1
        # [-1 3 -1]
        # i: 0, num: 1 | [(0, 1)] | { 1: -1: 2: -1, 4: -1 }
        # i: 1, num: 3 | 3 > 1 | [(1, 3)] | { 1: 3: 2: -1, 4: -1 }
        # i: 2, num: 4 | 4 > 3 | [(2, 4)] | { 1: 3: 2: -1, 4: -1 }
        # i: 3, num: 2 | 2 < 4 | [(2, 4), (3, 2)] | { 1: 3: 2: -1, 4: -1 }
        # [4 1 2] -> [-1 3 -1]
        # Monotonic Decreasing Stack
        # Time: O(m + n) | Space: O(m + n)
        nextGreaterNums = { num: -1 for num in nums1 }  # Mapping num -> next greater num
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                lastNum = stack.pop()
                if lastNum in nextGreaterNums:
                    nextGreaterNums[lastNum] = num
            stack.append(num)

        return [nextGreaterNums[num] for num in nums1]
