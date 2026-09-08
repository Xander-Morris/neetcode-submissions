class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def _traverse(sub, i):
            if len(sub) >= k:
                if len(sub) == k:
                    res.append(sub[:])
                return
            
            for j in range(i + 1, n + 1):
                sub.append(j)
                _traverse(sub, j)
                sub.pop()

        for i in range(1, n - k + 2):
            _traverse([i], i)
        
        return res