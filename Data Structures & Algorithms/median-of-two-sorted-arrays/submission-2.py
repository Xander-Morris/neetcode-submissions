import bisect

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            i = bisect.bisect_left(nums1, num)
            nums1.insert(i, num)
        
        n = len(nums1)

        return nums1[n // 2] if n % 2 != 0 else (nums1[n // 2] + nums1[(n // 2) - 1]) / 2