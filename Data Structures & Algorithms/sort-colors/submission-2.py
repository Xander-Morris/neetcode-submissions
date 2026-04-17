class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0

        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1
        
        i = 0

        for j in range(red):
            nums[i] = 0
            i += 1
        
        for j in range(white):
            nums[i] = 1
            i += 1
        
        for j in range(blue):
            nums[i] = 2
            i += 1