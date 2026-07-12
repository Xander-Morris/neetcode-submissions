class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {n: True}

        def dfs(i):
            if i in dp:
                return dp[i]  

            for word in wordDict:
                endI = i + len(word)
                if endI not in range(n + 1):
                    continue
                wordFromS = s[i:endI]
                if wordFromS == word:
                    if dfs(endI):
                        dp[i] = True 
                        return True 
            
            dp[i] = False 
            return False 

        return dfs(0)