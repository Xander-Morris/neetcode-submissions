class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        max_left = defaultdict(int)
        max_right = defaultdict(int)
        max_left_height = max_right_height = 0

        for i in range(len(height)):
            max_left[i] = max_left_height
            max_left_height = max(max_left_height, height[i])

        for i in range(len(height) - 1, -1, -1):
            max_right[i] = max_right_height
            max_right_height = max(max_right_height, height[i])

        for i in range(len(height)):
            water = min(max_left[i], max_right[i]) - height[i]
            print(f"Water {water} for i {i}")
            res += water if water > 0 else 0

        return res