class TrieNode:
    def __init__(self):
        self.children = [None] * 26 # 26 characters exist 
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end_of_word = True  

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                char = word[i]
                idx = ord(char) - ord('a')
                if char == ".":
                    if curr:
                        for child in curr.children:
                            if dfs(i + 1, child):
                                return True
                    return False
                else:
                    if not curr or not curr.children[idx]:
                        return False
                    curr = curr.children[idx]
            return curr and curr.is_end_of_word
        
        return dfs(0, self.root)
