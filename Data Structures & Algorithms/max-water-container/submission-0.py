class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0

        for i in range(len(heights)):
            for j in range(len(heights)):
                left_val = heights[i]
                right_val = heights[j]
                max_height = min(left_val, right_val)
                area = (j - i) * max_height
                best = max(best, area)

        return best