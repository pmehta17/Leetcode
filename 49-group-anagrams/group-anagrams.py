class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         
         # all anagrams have same letter maps

         # hashmap. key = string with letter freqs, value = list of words 

         # create key 

        anagrams = {}
        for word in strs: 

            arr = self.charmap(word)
            if arr in anagrams:
                anagrams[arr].append(word)
            else:
                anagrams[arr] = [word]
        
        return list(anagrams.values())
        
    def charmap(self, word):
    
        arr = [0] * 26
        for char in word: 
            arr[ord(char) - ord("a")] += 1
        return tuple(arr)  # key change: use tuple instead of string
