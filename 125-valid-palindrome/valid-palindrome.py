import re
class Solution: 


    def isPalindrome(self, s: str) -> bool:
       
        # METHOD 1 - CLEAN STRING AND COMPARE REVERSES
        # clean_string = ""
        # for a in s: 
        #     if a.isalnum() or a.isdigit(): 
        #         clean_string += a.lower()
        # return a == a[::-1]

        ## METHOD 2 - TWO POINTERS

        l = 0
        r = len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            else:
                l += 1
                r -= 1

        return True


