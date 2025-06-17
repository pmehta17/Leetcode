class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_clean = ""
        for ch in s: 
            if ch.isalnum():
                s_clean += ch.lower()        

        return s_clean[::-1] == s_clean