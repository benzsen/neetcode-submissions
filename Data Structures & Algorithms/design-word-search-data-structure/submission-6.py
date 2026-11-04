class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        
        def dfs(j, root):
            for i in range(j, len(word)):
                if word[i] == ".":
                    for c in root.children.values():
                        if dfs(i+1 , c):
                            return True
                    return False
                else:
                    if word[i] not in root.children:
                        return False
                    root = root.children[word[i]]
            return root.endOfWord

        return dfs(0, cur)
                

