class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # w: [hrn hrf er enn rfnn]
        # hrn vs hrf | h=h r=r n<f | adj: { n: [f] }
        # hrf vs er | h<e | adj: { n: [f] h: [e] }
        # er vs enn | e=e r<n | adj: { n: [f] h: [e] r: [n] }
        # enn vs rfnn | e<r | adj: { n: [f] h: [e] r: [n] e: [r] }
        # h -> e -> r -> n -> f
        # Topological Sort (Post Order DFS)
        # h -> e -> r -> n -> f
        #      ^ | e: [r] | on_path: { e: T } | []
        #           ^ | r: [n] | on_path: { e: T r: T } | []
        #                ^ | n: [f] | on_path: { e: T r: T n: T } | []
        #                     ^ | f: [] | on_path: { e: T r: T n: T f: T } | []
        #                     ^ | f: [] | on_path: { e: T r: T n: T f: F } | [f]
        #                ^ | n: [] | on_path: { e: T r: T n: F f: F } | [f n]
        #           ^ | r: [] | on_path: { e: T r: F n: F f: F } | [f n r]
        #      ^ | e: [] | on_path: { e: F r: F n: F f: F } | [f n r e]
        # ^ | h: [e] | on_path: { e: F r: F n: F f: F h: T } | [f n r e]
        #      ^ | e: [r] | on_path: { e: F r: F n: F f: F h: T } | [f n r e]
        # ^ | h: [] | on_path: { e: F r: F n: F f: F h: F } | [f n r e h]
        # hernf
        # Time: O(n) | Space: O(n)
        adj = {char: set() for word in words for char in word}  # Adjacency List

        for i in range(len(words) - 1):
            word_1, word_2 = words[i], words[i + 1]
            if len(word_1) > len(word_2) and word_1[:len(word_2)] == word_2:
                return ''

            minLen = min(len(word_1), len(word_2))
            for i in range(minLen):
                if word_1[i] != word_2[i]:
                    adj[word_1[i]].add(word_2[i])
                    break

        visiting = {}  # Mapping char -> True=Visiting | False=Visited (absent=unseen)
        result = []

        def dfs(char: str) -> bool:
            if char in visiting:
                return visiting[char]

            visiting[char] = True
            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True
                
            result.append(char)
            visiting[char] = False
            return visiting[char]

        for char in adj:
            if dfs(char):
                return ''

        result.reverse()
        return ''.join(result)
