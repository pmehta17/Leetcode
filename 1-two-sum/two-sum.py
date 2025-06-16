class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find two numbers in the array that add to target and return indices

        

        # create lookup map 
        indices = {}
        for idx, num in enumerate(nums):
            indices[num] = idx # to find numbers by the value 

        for i, n in enumerate(nums):
            diff = target - n # what we are looking for 

            if diff in indices and indices[diff]!=i:
                return [i, indices[diff]]