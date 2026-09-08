class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # [aba bcb ece aa e] | [[0,2],[1,4],[1,1]]
        # [T F T T T]
        # [0 1 2 3 4]
        # prefixCount: [1 1 2 3 4]
        # [0 2] | p[2] - p[0 - 1] = 2 - 0 = 2
        # [1 4] | p[4] - p[1 - 1] = 4 - 1 = 3
        # [1 1] | p[1] - p[1 - 1] = 1 - 0 = 1
        # [2 3 0]
        # PrefixCount
        # Time: O(n) | Space: O(n)
        n = len(words)
        prefixCount = [0] * (n + 1)
        vowels = set('aeiou')

        for i in range(n):
            word = words[i]
            startAndEndWithVowels = word[0] in vowels and word[-1] in vowels
            prefixCount[i + 1] = prefixCount[i] + int(startAndEndWithVowels)

        result = []

        for li, ri in queries:
            count = prefixCount[ri + 1] - prefixCount[li]
            result.append(count)

        return result
        # PrefixCount
        # # Time: O(n) | Space: O(n)
        # vowels = set('aeiou')
        # n = len(words)
        # prefixCount = [1 if word[0] in vowels and word[-1] in vowels else 0 for word in words]

        # for i in range(n - 1):
        #     prefixCount[i + 1] += prefixCount[i]

        # results = []

        # for li, ri in queries:
        #     count = prefixCount[ri] - (prefixCount[li - 1] if li > 0 else 0)
        #     results.append(count)

        # return results
