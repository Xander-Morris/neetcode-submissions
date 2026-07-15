class Solution:
    def _is_one_char_diff(self, a, b):
        diff = 0

        for i in range(len(a)):
            if b[i] == a[i]:
                continue

            diff += 1
            if diff > 1:
                return False
        
        return diff == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0 

        adj = defaultdict(list)

        for i in range(len(wordList) - 1):
            for j in range(i + 1, len(wordList)):
                if self._is_one_char_diff(wordList[i], wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        
        starting_words = list(set(word for word in wordList if self._is_one_char_diff(word, beginWord)))
        q = deque(starting_words)
        transformations = 1
        visited = set(starting_words)

        while q:
            transformations += 1

            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return transformations
                
                for nxt in adj[word]:
                    if nxt in visited:
                        continue
                    visited.add(nxt)
                    q.append(nxt)
            
        return 0