class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {n: True}

        def dfs(i):
            if i in dp:
                return dp[i]  

            for word in wordDict:
                endI = i + len(word)
                # python's slicing already handles the index being larger than the last index in the string, so no need to manually check that before slicing
                wordFromS = s[i:endI]
                if wordFromS == word:
                    # sliced word matches, so if dfs call on that end index is also True, then dp at this index is True 
                    if dfs(endI):
                        dp[i] = True 
                        return True 
            
            dp[i] = False 
            return False 

        return dfs(0)