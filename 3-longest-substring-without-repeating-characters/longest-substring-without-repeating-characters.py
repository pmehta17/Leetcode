class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0

        subseq = []
        idx = 0

        for char in s:
            # char not in subseq, add it
            if char not in subseq:
                subseq.append(char)

            # char is in subseq, remove from beginning until we get to char
            else:
                popped = ""
                while popped != char:
                    popped = subseq.pop(0)
                # after removing first instance of char, add 
                subseq.append(char)

            temp_len = len(subseq)
            max_len = max(temp_len, max_len)
            

            print(subseq)
        return max_len
            

            
            



