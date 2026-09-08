class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # [[0 2] [5 10] [13 23] [24 25]] | [[1 5] [8 12] [15 24] [25 26]]
        #   i                                j | 0 < 5 & 2 > 1 | T | [[1, 2]]
        #   i                                j | 5 = 5 & 2 < 8 | T | [[1, 2], [5, 5]]
        #         i                           j | 5 = 5 & 2 < 8 | T | [[1, 2], [5, 5]]
        # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        # Time: O(m + n) | Space: O(1)
        i, j = 0, 0
        m, n = len(firstList), len(secondList)
        result = []

        while i < m and j < n:
            firstStart, firstEnd = firstList[i]
            secondStart, secondEnd = secondList[j]

            if firstStart <= secondEnd and secondStart <= firstEnd:
                result.append([max(firstStart, secondStart), min(firstEnd, secondEnd)])

            if firstEnd <= secondEnd:
                i += 1
            else:
                j += 1

        return result
