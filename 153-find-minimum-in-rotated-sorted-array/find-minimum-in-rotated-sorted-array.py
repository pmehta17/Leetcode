class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        l = 0
        r = len(nums) - 1

        while l < r: 

            mid = l + (r-l)//2
            if nums[mid] < nums[r]:
                r = mid 
            else:
                l = mid + 1

            print(nums[l:r+1])
        return nums[l]


        #####################   BRUTE FORCE   ###########################################
        # brute force

        # # return min(nums)
        # m = float("inf")
        # for num in nums: 
        #     m = min(num, m)
        # return m

