class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            total_time = 0

            for p in piles:
                total_time += math.ceil(float(p) / k)
            if total_time <= h:
                # If the total time is <= h, then we can set the result to this k so far
                # and search the remaining values that are lower than this one
                res = k
                r = k - 1
            else:
                # Otherwise, we must use k values that are larger than this one
                # since this k value is not large enough to eat all of the piles
                # within the amount of hours we have.  
                l = k + 1

        return res
