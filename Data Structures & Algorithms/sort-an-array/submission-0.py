class Solution:
    def merge(self, l: List[int], r: List[int]) -> List[int]:
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

    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(left: int, right: int):
            if left >= right:
                return [nums[left]] if left == right else []
            
            mid = (left + right) // 2
            l = merge_sort(left, mid)
            r = merge_sort(mid + 1, right)

            return self.merge(l, r)
        
        return merge_sort(0, len(nums) - 1)