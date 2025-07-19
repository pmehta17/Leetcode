class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        
        nums_set = set(nums)

        for i in range(0, len(nums) + 1):
            if i in nums_set:
                continue
            return i

