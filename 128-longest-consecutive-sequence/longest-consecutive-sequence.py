class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Solution: 
        # Add all values to a set. If it the start of a sequence, count the number of new numbers. 

        # Questions
        # 1. How do we handle duplicates?
        # 2. Decimals and negative numbers?

        numSet = set(nums)
        longest = 0

        for num in numSet:
            
            
            # Start of sequence
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1  
            
            # not start of sequence
            else:
                continue       

            longest = max(longest, length)

        return longest
    
