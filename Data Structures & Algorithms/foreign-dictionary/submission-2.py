class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # w: [ab adc ade be cc cd]
        # adj: { a:[b] b:[c d] c:[d e] d:[] e: [] }
        # a -> b -> c -> e
        #      |    v 
        #      `--> d
        # Time: O(n) | Space: O(n)
        adj = {char: set() for word in words for char in word}  # Adjacency List

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ''

            minLength = min(len(w1), len(w2))
            for j in range(minLength):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        ordering = []
        visiting = {}  # Mapping char -> True=Visiting | False=Visited

        def dfs(char: str) -> bool:
            if char in visiting:
                return visiting[char]

            visiting[char] = True
            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True

            ordering.append(char)
            visiting[char] = False
            return visiting[char]

        for char in adj:
            if dfs(char):
                return ''

        ordering.reverse()
        return ''.join(ordering)
