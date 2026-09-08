#       *
#    /  |  \
#  d    b    m
#  |    |    |
#  a    a    a
#  |    |   / \
#  y*   y* n*  y*
#          |
#          y*

class TrieNode:
    def __init__(self):
        self.children = {}  # mapping char -> TrieNode
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        pointer = self.root
        for char in word:
            if char not in pointer.children:
                pointer.children[char] = TrieNode()
            pointer = pointer.children[char]
        pointer.isEnd = True

    def _searchWordInNode(self, word: str, node: TrieNode) -> bool:
        n = len(word)
        if n == 0:
            return node.isEnd

        char = word[0]
        if char == '.':
            for child in node.children.values():
                if self._searchWordInNode(word[1:], child):
                    return True
            return False

        if char not in node.children:
            return False

        nextNode = node.children[char]
        return self._searchWordInNode(word[1:], nextNode)

    def search(self, word: str) -> bool:
        return self._searchWordInNode(word, self.root)
