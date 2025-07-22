class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()

        for i in range(len(nums)):

            # skip duplicates for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue # skip to next iteration of i

            l = i + 1
            r = len(nums) - 1

            while l < r: 
                total = nums[i] + nums[l] + nums[r]


                if total == 0: 
                    ans.append([nums[i], nums[l], nums[r]])

                    #update pointers and skip duplicates
                    l += 1
                    r -= 1
                    
                    while l < r and nums[l] == nums[l - 1]: 
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                
                elif total > 0: 
                    r -= 1
                else:
                    l += 1
        
        return ans

