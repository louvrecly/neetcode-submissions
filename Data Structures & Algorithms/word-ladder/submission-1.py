class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # b: cat | e: sag | w: [bat bag sag dag dot]
        # cat -> bat -> bag -> sag | 4
        # b: cat | e: sag | w: [bat bag sat dag dot]
        # cat -> bat -> bag -> dag
        #     -> sat -> bat -> bag -> dag | 0
        # b: cat | e: sag | w: [bat bag sag dag dat dot]
        # cat - bat - bag
        #     \  |     |  \
        #       dat - dag - sag
        #        |
        #       dot
        # adj: {
        #     cat: [bat dat]
        #     bat: [bag dat]
        #     bag: [bat dag sag]
        #     dag: [bag dat sag]
        #     dat: [bat dag dot]
        #     dot: [dat]
        #     sag: [bag dag]
        # }
        # dist: {
        #     cat: 2
        #     bat: 2
        #     bag: 1
        #     dag: 1
        #     dat: 2
        #     dot: 3
        #     sag: 0
        # }
        # - | f: [(cat 1)] | v: {}
        # cat, 1 | f: [(bat 2) (dat 2)] | v: {cat}
        # bat, 2 | f: [(dat 2) (bag 3) (dat 3)] | v: {cat bat}
        # dat, 2 | f: [(bag 3) (dat 3) (dag 3) (dot 3)] | v: {cat bat dat}
        # bag, 3 | f: [(dat 3) (dag 3) (dot 3) (dag 4) (sag 4)] | v: {cat bat dat bag}
        # dat, 3 | f: [(dag 3) (dot 3) (dag 4) (sag 4)] | v: {cat bat dat bag}
        # dag, 3 | f: [(dot 3) (dag 4) (sag 4) (sag 4)] | v: {cat bat dat bag dag}
        # dot, 3 | f: [(dag 4) (sag 4) (sag 4)] | v: {cat bat dat bag dag dot}
        # dag, 4 | f: [(sag 4) (sag 4)] | v: {cat bat dat bag dag dot}
        # sag, 4 | f: [(sag 4)] | v: {cat bat dat bag dag dot sag} | 4
        # Djikstra's Algorithm - BFS with Min Heap and Distance as Heuristic
        # Time: O(V^2 + EV) | Space: O(E + V)
        def countCharMatches(word1: str, word2: str) -> int:
            n = min(len(word1), len(word2))
            count = 0
            for i in range(n):
                if word1[i] == word2[i]:
                    count += 1
            return count

        m = len(endWord)
        if len(beginWord) != m:
            return 0

        wordList.append(beginWord)
        wordList = [word for word in wordList if len(word) == m]
        adj = defaultdict(list)  # mapping word -> neighbor[]
        n = len(wordList)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if countCharMatches(wordList[i], wordList[j]) == m - 1:
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])

        frontier = [(1, beginWord)]
        visited = set()
        while frontier:
            cost, word = heapq.heappop(frontier)
            if word == endWord:
                return cost

            if word in visited:
                continue

            visited.add(word)
            for neighbor in adj[word]:
                if neighbor not in visited:
                    heapq.heappush(frontier, (cost + 1, neighbor))

        return 0
