class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_height = 0

        l = 0
        r = len(height) - 1

        while l < r:
            temp_height = int(min(height[l], height[r])) * (r - l)

            if temp_height > max_height: 
                max_height = temp_height

            if height[l] < height[r]:
                l += 1
            elif height[l] >= height[r]: 
                r -= 1

        return max_height