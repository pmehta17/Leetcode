class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Questions
        # How do we handle decimals? Negative numbers?
        # clarify list of size 0 or 1 defaults to 0 or 1 respectively

        
        numSet = set(nums) # Convert to set for O(1) lookup
        longest = 0 # Set intial max length to 0

        for n in numSet:

            # n is the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                # Keep checking if next value is in set, increae length

                while (n + length) in numSet:
                    length += 1
                    # will break when next value is not in list
                
                longest = max(longest, length)

        return longest

        # Time complexity: O(n)
