class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Time: O(mn + nm log n) | Space: O(n^2)
        m = len(endWord)
        if len(beginWord) != m:
            return 0

        wordList = [word for word in wordList if len(word) == m]
        wordList.append(beginWord)

        def getWordPatterns(word: str) -> List[str]:
            return [word[:i] + '*' + word[i + 1:] for i in range(len(word))]

        adj = defaultdict(set)
        for word in wordList:
            patterns = getWordPatterns(word)
            for pattern in patterns:
                adj[pattern].add(word)

        frontier = [(1, beginWord)]
        visited = set()
        while frontier:
            cost, word = heapq.heappop(frontier)
            if word == endWord:
                return cost

            if word in visited:
                continue

            visited.add(word)
            patterns = getWordPatterns(word)
            for pattern in patterns:
                for neighbor in adj[pattern]:
                    if neighbor not in visited:
                        heapq.heappush(frontier, (cost + 1, neighbor))

        return 0
