class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        ct = 0 # keep longest sequence count 
        nums_set = set(nums)


        for num in nums_set: 
            streak = 1 # temp streak count
            if num - 1 in nums_set: 
                continue # not start of sequence

            
            current = num
            while current + 1 in nums_set:
                current += 1
                streak += 1 
        
            ct = max(streak, ct)

        return ct
                
            


            
    
