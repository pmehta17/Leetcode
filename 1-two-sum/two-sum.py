class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {} # key: number, value: index


        for i in range(len(nums)): 
            temp = target - nums[i]
            if temp in map:
                return [i, map[temp]]
            map[nums[i]] = i

        
        
