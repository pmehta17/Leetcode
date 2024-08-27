class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Bit manipulation
        res = 0

        for n in nums:
            res = res ^ n
        return res
        

        ## Hash set solution
        seen = set()

        for n in nums:
            if n not in seen: 
                seen.add(n)
            else:
                seen.remove(n)

        return seen.pop()