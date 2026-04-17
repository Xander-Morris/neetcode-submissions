class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1set = set(nums1)
        nums2set = set(nums2)
        res = []

        for num in nums1set:
            if not num in nums2set:
                continue
            
            res.append(num)

        return res