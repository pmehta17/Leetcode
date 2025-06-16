class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # two anagrams will be the same when sorted
        # time complexity: nlogn + mlogm
        # return sorted(s) == sorted(t)

        

        # two anagrams will have the same letter frequencies 

        if len(s) != len(t): 
            return False
        
        sCount, tCount = {}, {}          

        for i in range(len(s)):
            # update hashmap to add current char to count
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
        return sCount == tCount

        
        