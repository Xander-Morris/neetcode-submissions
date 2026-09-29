from collections import defaultdict 

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mp = defaultdict(int)

        for bill in bills:
            mp[bill] += 1
            leftover = bill - 5

            if leftover == 0:
                continue
            
            keys = sorted(mp.keys())

            for i in range(len(keys) - 1, -1, -1):
                key = keys[i]

                if key > leftover or mp[key] <= 0:
                    continue
                
                can_take = min(leftover // key, mp[key])
                leftover -= (can_take * key)
                mp[key] -= can_take

            if leftover > 0:
                return False
        
        return True 