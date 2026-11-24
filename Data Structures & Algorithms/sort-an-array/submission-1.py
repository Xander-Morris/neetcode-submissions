class Solution:
    def _merge(self, l: List[int], r: List[int]) -> List[int]:
        res = []
        i = j = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1

        res.extend(l[i:])
        res.extend(r[j:])

        return res

    def _merge_sort(self, nums: List[int], left: int, right: int):
        if left >= right:
            return [nums[left]] if left == right else []
        
        mid = (left + right) // 2
        l = self._merge_sort(nums, left, mid)
        r = self._merge_sort(nums, mid + 1, right)

        return self._merge(l, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self._merge_sort(nums, 0, len(nums) - 1)