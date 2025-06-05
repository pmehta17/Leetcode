class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        nums_set = set(nums)
        n = len(nums)
        ans = [] 
         
        for i in range(1, n+1):
            if i not in nums_set:
                ans.append(i)

        return ans
        