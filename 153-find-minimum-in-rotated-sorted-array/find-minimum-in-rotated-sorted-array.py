class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        l = 0
        r = len(nums) - 1

        while l < r: 

            mid = l + (r-l)//2

            # found rotation
            if nums[mid] > nums[mid + 1]:
                return nums[mid+1]
            elif nums[mid] < nums[mid + 1]:
                r = mid - 1


        #####################   BRUTE FORCE   ###########################################
        # brute force

        # return min(nums)
        m = float("inf")
        for num in nums: 
            m = min(num, m)
        return m

