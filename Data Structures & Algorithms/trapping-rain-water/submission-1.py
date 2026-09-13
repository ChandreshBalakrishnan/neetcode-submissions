class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftmax = 0
        water = 0
        rightmax = 0
        for h in height:
            if leftmax <= rightmax:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    water += leftmax - height[left]
                left += 1
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    water += rightmax - height[right]
                right -= 1
        return water
