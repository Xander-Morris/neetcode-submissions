class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mp = defaultdict(str)

        for s in strs:
            sorted_s = "".join(sorted(s))
            
            if not sorted_s in mp:
                mp[sorted_s] = [s]
            else:
                mp[sorted_s].append(s)
            
        for sorted_s in mp:
            new_l = []

            for s in mp[sorted_s]:
                new_l.append(s)

            res.append(new_l)
        
        return res