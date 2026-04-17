class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                # Can extend backward since we know the top of the stack
                # had a higher height value than the current height of the "i" index
                # we are looking at. 
                # That means that the current height can fit all the way back to
                # where the top of the stack was that was taller than this current
                # height.
                start = index

            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea