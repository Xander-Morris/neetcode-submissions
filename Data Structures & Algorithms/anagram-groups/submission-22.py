class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mp = defaultdict(str)

        for s in strs:
            sorted_s = "".join(sorted(s))

            if not sorted_s in mp:
                mp[sorted_s] = []
            
            mp[sorted_s].append(s)
        
        for sorted_s in mp:
            lst = []

            for s in mp[sorted_s]:
                lst.append(s)
            
            res.append(lst)

        return res