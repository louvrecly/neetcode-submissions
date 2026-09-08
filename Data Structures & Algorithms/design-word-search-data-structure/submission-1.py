#       *
#    /  |  \
#  d    b    m
#  |    |    |
#  a    a    a
#  |    |   / \
#  y*   y* n*  y*
#          |
#          y*

class Node:
    def __init__(self):
        self.children = {}  # mapping char -> Node
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.children = {}  # mapping char -> Node
        self.isEnd = False

    def addWord(self, word: str) -> None:
        pointer = self
        for char in word:
            if char not in pointer.children:
                pointer.children[char] = Node()
            pointer = pointer.children[char]
        pointer.isEnd = True

    def _searchWordInNode(self, word: str, node: Node) -> bool:
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
        return self._searchWordInNode(word, self)
