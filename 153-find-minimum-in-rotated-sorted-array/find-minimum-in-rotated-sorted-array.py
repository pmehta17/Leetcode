class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # brute force

        # return min(nums)
        m = float("inf")
        for num in nums: 
            m = min(num, m)
        return m