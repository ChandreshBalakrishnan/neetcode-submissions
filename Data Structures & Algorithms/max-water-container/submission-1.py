class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = right*min(heights[left],heights[right])
        while left < right:
            if heights[left] <= heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            area = max(area,(right - left)*min(heights[left],heights[right]))
        return area