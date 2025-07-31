class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        max_ct = 0


        for n in nums_set: 
            if n - 1 in nums_set:
                continue

            c = n
            temp_ct = 1

            while c + 1 in nums_set:
                temp_ct += 1
                c += 1
            max_ct = max(temp_ct, max_ct)


            
        return max_ct




        