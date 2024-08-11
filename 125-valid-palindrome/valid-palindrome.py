import re
class Solution: 


    def isPalindrome(self, s: str) -> bool:
       
        clean_string = ""
        for a in s: 
            if a.isalnum() or a.isdigit(): 
                clean_string += a.lower()

        l = 0
        r = len(clean_string)-1

        while l < r:
            if clean_string[l] != clean_string[r]:
                return False
            else:
                l += 1
                r -=1
        return True


