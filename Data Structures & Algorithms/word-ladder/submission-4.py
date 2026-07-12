class Solution:
    def is_one_char_diff(self, a, b):
        if a == b:
            return False 
        
        diff_chars = 0
        for c_i in range(len(a)):
            if a[c_i] == b[c_i]:
                continue
            diff_chars += 1
            if diff_chars > 1:
                return False
        return diff_chars == 1 

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        mp = {word: i for i, word in enumerate(wordList)}
        adj = [[] for _ in range(len(wordList))]

        # build adjacency list for each word mapping it to all words that are only one character different
        # from itself
        for i, i_word in enumerate(wordList):
            for j in range(len(wordList)):
                j_word = wordList[j]
                if not self.is_one_char_diff(i_word, j_word):
                    continue
                adj[i].append(j)
                adj[j].append(i)
        
        q = deque()
        visited = set()
        # find all words that are only ONE character different from beginWord to add to initial queue
        for word in wordList:
            if word in visited:
                continue
            if not self.is_one_char_diff(word, beginWord):
                continue
            visited.add(word)
            q.append(mp[word])
        
        res = 1
        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                if wordList[node] == endWord:
                    return res
                for nei in adj[node]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    q.append(nei)
            
        return 0