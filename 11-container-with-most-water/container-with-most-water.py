class Solution:
    def maxArea(self, height: List[int]) -> int:

        ans = 0

        l = 0
        r = len(height) - 1


        while l < r: 

            temp_area = (r - l) * min(height[l], height[r])
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            

            ans = max(ans, temp_area)
            
        return ans 


        