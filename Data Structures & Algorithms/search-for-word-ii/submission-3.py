class TrieNode:
    def __init__(self):
        self.children = {}  # mapping char -> TrieNode
        self.wordEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # [
        #     [a b c d]
        #     [s a a t]
        #     [a c k e]
        #     [a c d n]
        # ]
        # [bat cat back backend stack]
        # Trie/Prefix Tree
        #         *
        #     /   |   \
        #    b    c    s
        #    |    |    |
        #    a    a    t
        #   / \   |    |
        #  c  *t *t    a
        #  |           |
        # *k           c
        #  |           |
        #  e          *k
        #  |
        #  n
        #  |
        # *d
        # Time: O(m * n * 4 ** (m * n) + w * c) | Space: O(4 ** (m * n) + w + c * log w)
        dictionary = TrieNode()

        def registerWord(word: str) -> None:
            # Time: O(c) | Space: O(c)
            node = dictionary
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.wordEnd = True

        for word in words:
            # Time: O(w * c) | Space: O(w + c * log w)
            registerWord(word)

        m, n = len(board), len(board[0])
        found = set()

        def dfs(
            r: int,
            c: int,
            visited: Set[Tuple[int]],
            node: TrieNode=dictionary,
            word: str=''
        ) -> None:
            # Time: O(4 ** (m * n)) | Space: O(4 ** (m * n))
            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return
            
            visited.add((r, c))
            char = board[r][c]
            word += char
            node = node.children[char]

            if node.wordEnd:
                found.add(word)

            dfs(r - 1, c, visited.copy(), node, word)
            dfs(r, c - 1, visited.copy(), node, word)
            dfs(r + 1, c, visited.copy(), node, word)
            dfs(r, c + 1, visited.copy(), node, word)

        for r in range(m):
            for c in range(n):
                dfs(r, c, set())

        return list(found)
