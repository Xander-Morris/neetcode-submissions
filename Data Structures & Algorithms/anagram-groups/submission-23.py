class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Fix: Use list instead of str to allow appending
        mp = defaultdict(list) 
        
        for s in strs:
            # Sort the string to use as a key
            sorted_s = "".join(sorted(s))
            # Append the original string to the list of anagrams
            mp[sorted_s].append(s)
            
        # Return the values (lists of anagrams) directly
        return list(mp.values())