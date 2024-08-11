class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = nums[i-1] * pre[i-1]

        print(f"pre: {pre}")


        post = [1] * len(nums)

        for j in range(len(nums)-2, -1, -1):
            post[j] = post[j+1] * nums[j+1]    
      
        print(f"post: {post}")


        ans = [1] * len(nums)
        for k in range(len(nums)):
            ans[k] = pre[k] * post[k]

        
        return ans

        # O(n)

        #Solution: In the answer, each index is the product of all numbers to the left and to the right, but not the number itself. 
        #   Have two arrays (pre and post). Pre has the product of all numbers to the left of a certain index, and psot has the product of all numbers to the right. 
        #   THe answer will be an array where each index is the product of the two values in the pre and post arrays at the same index
            
        


