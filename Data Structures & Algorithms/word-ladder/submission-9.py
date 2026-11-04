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
            for pattern in getWordPatterns(word):
                adj[pattern].add(word)

        def getWordNeighbors(word: str) -> List[str]:
            neighbors = []
            for pattern in getWordPatterns(word):
                for neighbor in adj[pattern]:
                    neighbors.append(neighbor)
            return neighbors

        dist = {}  # mapping word -> distance from endWord
        for word in wordList:
            dist[word] = m
            for i in range(m):
                if word[i] == endWord[i]:
                    dist[word] -= 1

        frontier = [(dist[beginWord], 1, beginWord)]
        visited = set()

        while frontier:
            distance, cost, word = heapq.heappop(frontier)
            if distance == 0:
                return cost

            if word in visited:
                continue

            visited.add(word)
            for neighbor in getWordNeighbors(word):
                if neighbor not in visited:
                    heapq.heappush(frontier, (dist[neighbor], cost + 1, neighbor))

        return 0
