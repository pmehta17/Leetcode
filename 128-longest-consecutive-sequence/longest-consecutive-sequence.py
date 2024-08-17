class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ## Questions:
        ## Are all numbers positive? How would we handle negative numbers?
        ## Decimals? 

        ## Brute force 
        ## sort the list. Check if next number is current + 1. 

        if len(nums) == 0:
            return 0
            
        nums.sort()
        
        max_count = 1
        current_count = 1

        # Iterate through the sorted list
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                # Skip duplicates
                continue
            elif nums[i] == nums[i - 1] + 1:
                # Increment the current sequence count
                current_count += 1
            else:
                # Reset count for a new sequence
                max_count = max(max_count, current_count)
                current_count = 1

        # Final check to ensure the last sequence is considered
        return max(max_count, current_count)
