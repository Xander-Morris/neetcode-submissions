class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        max_left = defaultdict(int)
        max_right = defaultdict(int)
        curr_max_left = 0
        curr_max_right = 0

        for i in range(len(height)):
            max_left[i] = curr_max_left
            curr_max_left = max(curr_max_left, height[i])

        for i in range(len(height) - 1, -1, -1):
            max_right[i] = curr_max_right
            curr_max_right = max(curr_max_right, height[i])

        for i in range(len(height)):
            l_max = max_left[i]
            r_max = max_right[i]
            h = min(l_max, r_max)
            water = h - height[i]
            res += water if water > 0 else 0

        return res