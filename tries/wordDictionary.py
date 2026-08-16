"""
211. Design Add and Search Words Data Structure
-----------------------------------------------
Design a data structure that supports:
  - addWord(word)   : store word for future matching
  - search(word)    : return True if any stored word matches; '.' in the
                      pattern matches any single letter

Data representation:
  Trie of TrieNode objects.
  Each TrieNode has:
    - self.children : dict[str, TrieNode]  — edges keyed by character
    - self.is_end   : bool                 — marks end of a stored word

Key operations:
  addWord  → standard trie insert, character by character
  search   → recursive trie traversal; at a '.' node, branch into every
             child and return True if any branch matches the remainder

  Time:  addWord  O(n)      where n = len(word)
         search   O(n)      normal case; O(26^n) worst case (all dots)
  Space: O(total characters stored across all words)
"""


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_word: bool = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currentNode: TrieNode = self.root
        for character in word:
            currentNode = currentNode.children.setdefault(character,TrieNode())
        currentNode.is_word = True

    def search(self, word: str) -> bool:
        return self.depthFirstSearch(self.root, 0, word)
    
    def depthFirstSearch(self, node: TrieNode, index: int, word:str) -> bool:
        if index == len(word):
            return node.is_word
        if word[index] == ".":
            for child in node.children.values():
                if self.depthFirstSearch(child, index+1, word):
                    return True
        if word[index] in node.children:
            return self.depthFirstSearch(node.children[word[index]],index+1,word)
        return False
            

# --------------------------------------------------------------------------- #

if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")

    tests = [
        ("pad",  False),
        ("bad",  True),
        (".ad",  True),
        ("b..",  True),
        ("...",  True),
        ("....", False),
        ("b.d",  True),
        ("b.t",  False),
    ]

    for pattern, expected in tests:
        result = wd.search(pattern)
        status = "✅" if result == expected else "❌"
        print(f"{status} search({pattern!r:<6}) → got {result!r:<6}  expected {expected!r}")
