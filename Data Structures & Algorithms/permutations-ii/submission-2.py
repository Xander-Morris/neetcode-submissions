class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def _traverse(sub, used):
            if len(used) == len(nums):
                res.add(tuple(sub))
                return
            
            for i, num in enumerate(nums):
                if i in used:
                    continue
                used.add(i)
                sub.append(num)
                _traverse(sub, used)
                sub.pop()
                used.remove(i)

        _traverse([], set())

        return list(res)