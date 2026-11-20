from collections import defaultdict 

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')

            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        
        curr.is_word = True
    
    def is_valid_prefix(self, prefix):
        curr = self.root

        for c in prefix:
            idx = ord(c) - ord('a')

            if not curr.children[idx]:
                return False

            curr = curr.children[idx]
        
        return True 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words = set(words)
        max_len = max(len(w) for w in words)
        trie = Trie()

        for word in words:
            trie.add_word(word)

        def _traverse(r, c, visited, word):
            if not trie.is_valid_prefix(word):
                return set() 
            if len(word) > max_len:
                return set()

            res = set()

            if word in words:
                res.add(word)

            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc

                if nr not in range(len(board)) or nc not in range(len(board[nr])):
                    continue
                if (nr, nc) in visited:
                    continue
                
                new_word = word + board[nr][nc]

                if new_word in words:
                    res.add(new_word)

                visited.add((nr, nc))
                trav_res = _traverse(nr, nc, visited, word + board[nr][nc])
                visited.remove((nr, nc))
                res.update(trav_res)
            
            return res 
        
        res = []

        for r in range(len(board)):
            for c in range(len(board[r])):
                trav_res = _traverse(r, c, set([(r, c)]), board[r][c])
                res.extend(trav_res)

        return list(set(res)) 