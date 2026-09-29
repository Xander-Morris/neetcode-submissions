class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def _traverse(i, sub):
            nonlocal res

            if i == len(nums):
                res.append(sub[:])
                return

            sub.append(nums[i])
            _traverse(i + 1, sub)
            sub.pop()
            _traverse(i + 1, sub)

        _traverse(0, [])

        return res