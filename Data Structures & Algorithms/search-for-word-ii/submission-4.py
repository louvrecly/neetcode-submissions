# [
#     [a c]
#     [p e]
# ]
# w: [ace ape app cap cape]
#         *
#      /     \
#     a       c
#   /   \     |
#  c     p    a
#  |    / \   |
# *e  *e  *p *p
#             |
#            *e
class TrieNode:
    def __init__(self):
        self.children = {}  # mapping char -> TrieNode

    def addWord(self, word: str):
        # Time: O(c) | Space: O(c)
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.children['#'] = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Time: O(m * n * 4 ** (m * n)) | Space: O(m * n + c * log w)
        root = TrieNode()

        for word in words:
            root.addWord(word)

        m, n = len(board), len(board[0])
        found = set()  # found words
        visited = set()  # visited cells (r, c)

        def dfs(r: int, c: int, node: TrieNode=root) -> None:
            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return

            visited.add((r, c))
            char = board[r][c]
            node = node.children[char]

            if '#' in node.children:
                found.add(node.children['#'])

            dfs(r - 1, c, node)
            dfs(r, c - 1, node)
            dfs(r + 1, c, node)
            dfs(r, c + 1, node)
            visited.remove((r, c))

        for r in range(m):
            for c in range(n):
                dfs(r, c)

        return list(found)
