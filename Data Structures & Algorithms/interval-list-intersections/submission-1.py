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
            currI, currJ = firstList[i], secondList[j]
            if currI[1] >= currJ[0] and currI[0] <= currJ[1]:
                result.append([max(currI[0], currJ[0]), min(currI[1], currJ[1])])

            if i + 1 < m and j + 1 < n:
                nextI, nextJ = firstList[i + 1], secondList[j + 1]
                if nextI[0] <= currJ[1]:
                    i += 1
                elif nextJ[0] <= currI[1]:
                    j += 1
                else:
                    i, j = i + 1, j + 1
            elif i + 1 < m:
                i += 1
            elif j + 1 < n:
                j += 1
            else:
                i, j = i + 1, j + 1
            
        return result