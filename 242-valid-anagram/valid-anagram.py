class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)

        # two anagrams will have the same letter frequencies 


        
        