class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        l = 1
        r = max(piles)
        res = r + 1

        while l <= r:
            k = (l + r) // 2    
            total_time = 0

            for pile in piles:
                total_time += math.ceil(float(pile) / k)
            
            if total_time <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res