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
            # we can start j from i + 1 since this is an undirected adjacency list we are building here
            # so any of i's adjacent nodes that came before index i
            # would have been found and added to adjacency list already by now
            # changing j to run from 0 to end of list, just like i, wouldn't make this solution suddenly faulty, though
            # it would just be pointless
            for j in range(i + 1, len(wordList)):
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
                # already added to initial queue 
                continue
            if not self.is_one_char_diff(word, beginWord):
                # only looking for words that are one char diff from beginWord
                continue
            # add to initial queue and visited set
            visited.add(word)
            q.append(mp[word]) # add the INDEX to queue, not the word itself 
        
        res = 1 # res starts at 1 since we are given a beginWord, meaning we start with 1 word to begin with
        while q:
            res += 1
            # pop all nodes off on current level
            for _ in range(len(q)):
                node = q.popleft()
                if wordList[node] == endWord:
                    # we built end word, so return res already 
                    return res
                for nei in adj[node]:
                    # search from here, going to any words that are only one char diff from this current word we just popped off
                    if nei in visited:
                        continue
                    visited.add(nei)
                    q.append(nei)
            
        return 0