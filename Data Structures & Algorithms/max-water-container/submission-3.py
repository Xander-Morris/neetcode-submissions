class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            left_val = heights[i]
            right_val = heights[j]
            max_height = min(left_val, right_val)
            area = (j - i) * max_height
            best = max(best, area)

            if left_val <= right_val:
                i += 1
            else:
                j -= 1

        return best