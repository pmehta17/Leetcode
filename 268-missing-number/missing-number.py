class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        expected_sum =  len(nums) * (len(nums)+1) // 2

        true_sum = sum(nums)

        return expected_sum - true_sum