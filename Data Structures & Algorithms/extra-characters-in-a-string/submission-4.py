class TrieNode:
    def __init__(self):
        self.children = {}  # mapping char -> TrieNode
        self.word = False


class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            self.registerWord(word)

    def registerWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    def checkWord(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Prefix Tree | Trie
        # Dynamic Programming
        # dp(i) = min(
        #     1 + dp(i + 1),  # skip current char
        #     dp(j + 1) for j in range(i, n) if root.checkWord(s[i:j + 1])
        # )
        # Time: O(n^2) | Space: O(n * 2)
        n = len(s)
        root = Trie(dictionary)
        cache = {}  # mapping i -> min extra chars

        def dp(i: int) -> int:
            if i >= n:
                return 0

            if i in cache:
                return cache[i]

            result = 1 + dp(i + 1)

            for j in range(i, n):
                if root.checkWord(s[i:j + 1]):
                    result = min(result, dp(j + 1))

            cache[i] = result
            return cache[i]

        return dp(0)
