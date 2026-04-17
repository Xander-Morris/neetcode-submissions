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
            inner = []

            for s in mp[sorted_s]:
                inner.append(s)
            
            res.append(inner)

        return res