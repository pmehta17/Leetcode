class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0 or len(s) == 1: 
            return len(s)

        l = 0 # left pointer
        chars = set() # set of characters currently in our string
        max_len = 0 # max length

        # iterate thru the string
        for r in range(len(s)): 
            # current char in sting
            while s[r] in chars: 
                # remove left 
                chars.remove(s[l]) 
                l += 1 

            # current char not in string
            chars.add(s[r])
            max_len = max(max_len, (r-l+1))
        return max_len

















        # edge case for empty string or only one char string
        if len(s) == 0 or len(s) == 1: 
            return len(s)
        
        
        l = 0
        charSet = set()
        res = 0 

        for r in range(len(s)): 
            while s[r] in charSet: 
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res=max(res, r - l + 1)
        return res

        


        ## __________________________________
        ##      Naive, semi-brute force
        # max_len = 0

        # subseq = []
        # idx = 0

        # for char in s:
        #     # char not in subseq, add it
        #     if char not in subseq:
        #         subseq.append(char)

        #     # char is in subseq, remove from beginning until we get to char
        #     else:
        #         popped = ""
        #         while popped != char:
        #             popped = subseq.pop(0)
        #         # after removing first instance of char, add 
        #         subseq.append(char)

        #     temp_len = len(subseq)
        #     max_len = max(temp_len, max_len)
            

        #     print(subseq)
        # return max_len
            

            
            



