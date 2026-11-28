class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap = max(weights)
        max_cap = sum(weights)
        low = min_cap 
        high = max_cap
        res = float('inf')

        while low <= high:
            cap = (low + high) // 2
            days_used = curr_day_w = 0

            for i, w in enumerate(weights):
                if curr_day_w + w > cap:
                    days_used += 1
                    curr_day_w = 0

                curr_day_w += w
                
                if days_used > days:
                    break 
            
            if curr_day_w > 0:
                days_used += 1

            if days_used <= days:
                res = cap 
                high = cap - 1
            else:
                low = cap + 1

        return res