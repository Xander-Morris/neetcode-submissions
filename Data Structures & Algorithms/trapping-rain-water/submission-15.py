class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        # prefix maximums for left and right are calculated first 
        res = 0
        max_left = defaultdict(int)
        max_right = defaultdict(int)
        curr_max = 0

        for i in range(len(height)):
            max_left[i] = curr_max
            curr_max = max(curr_max, height[i])

        curr_max = 0

        for i in range(len(height) - 1, -1, -1):
            max_right[i] = curr_max
            curr_max = max(curr_max, height[i])

        for i in range(len(height)):
            min_h = min(max_left[i], max_right[i])
            # water we can store at this location is min_height of left and right minus height at current index
            water = min_h - height[i]
            res += water if water > 0 else 0 # just in case water is <= 0

        return res