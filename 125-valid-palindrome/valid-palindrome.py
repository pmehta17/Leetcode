class Solution:
    def isPalindrome(self, s: str) -> bool:

        # method 2: two pointer

        s = s.lower()

        l = 0
        r = len(s) - 1

        while l < r:

            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True


        

        # ## Method 1: Clean and reverse string 
        # s_clean = ""
        # for ch in s: 
        #     if ch.isalnum():
        #         s_clean += ch.lower()        

        # return s_clean[::-1] == s_clean