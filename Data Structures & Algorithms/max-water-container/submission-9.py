class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = l = 0
        r = len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            area = (r - l) * height
            res = max(res, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res