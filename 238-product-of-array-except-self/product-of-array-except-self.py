class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1] * len(nums)
        pre = [1] * len(nums)
        post = [1] * len(nums)


        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i - 1]

        for j in range(len(nums) - 2, -1, -1):
            post[j] = post[j + 1] * nums[j + 1]

        for i in range(len(nums)):
            ans[i] = pre[i] * post[i]

        
        return ans