from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        min_len = min(len(word) for word in words)
        max_len = max(len(word) for word in words)

        @cache 
        def _traverse(i, sentence):
            if i >= len(s):
                return sentence 

            res = []

            for j in range(i + min_len, i + max_len + 1):
                if j > len(s):
                    break 
                
                word = s[i:j]
                
                if word in words:
                    trav_res = _traverse(j, sentence + word if len(sentence) == 0 else sentence + " " + word)

                    if len(trav_res) > 0:
                        if max(len(w) for w in trav_res) == 1:
                            res.append("".join(trav_res))
                        else:
                            res.extend(trav_res)
            
            return res 

        return _traverse(0, "")