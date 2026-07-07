class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heightCount = len(heights)
        maxArea = 0
        stack = []

        for index in range(heightCount + 1):
            while stack and (index == heightCount or heights[stack[-1]] >= heights[index]):
                currentHeight = heights[stack.pop()]
                currentWidth = index if not stack else index - stack[-1] -1
                maxArea = max(maxArea, currentHeight * currentWidth)

            stack.append(index)
        
        return maxArea