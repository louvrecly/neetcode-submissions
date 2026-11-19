# board: [
#     [a b c d]
#     [s a a t]
#     [a c k e]
#     [a c d n]
# ]
# words: [back backend bat cat stack]
# [back backend cat]
# Prefix Tree
#       [ ]
#    /   |   \
#   b    c    s
#   |    |    |
#   a    a    t
#  / \   |    |
# c   t* t*   a
# |           |
# k*          c
# |           |
# e           k*
# |
# n
# |
# d*
class TrieNode:
    def __init__(self):
        self.children = {}  # mapping char -> TrieNode
        self.word = ""


class Trie:
    def __init__(self, words: List[str]=[]):
        self.root = TrieNode()
        for word in words:
            self.registerWord(word)

    def registerWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Time: O(mn(4^mn) + l) | Space: O(mn(4^mn) + l)
        m, n = len(board), len(board[0])
        root = Trie(words).root
        visited = set()
        found = set()

        def dfs(r: int, c: int, node: TrieNode=root) -> None:
            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]

            if node.word:
                found.add(node.word)

            dfs(r + 1, c, node)
            dfs(r, c + 1, node)
            dfs(r - 1, c, node)
            dfs(r, c - 1, node)
            visited.remove((r, c))

        for r in range(m):
            for c in range(n):
                dfs(r, c)

        return list(found)
