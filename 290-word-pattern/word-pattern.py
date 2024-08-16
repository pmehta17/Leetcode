class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # Questions: 
        # 1. Can we assume the number of charcters in the pattern will be the same as the number of words in the string
        # 2. Will we only have characters and words? Should it be case senstive? Special characters?

        wordmap = {}
        str_set = set()


        s = list(s.split(" "))

        if len(pattern) != len(s): 
            return False

        for i in range(len(pattern)):
            if pattern[i] in wordmap:
                if wordmap[pattern[i]] != s[i]:
                    return False
                    
            else: 
                if s[i] in str_set: # If the word is already in the set, then it has already been mapped to. Therefore, the pattern is broken
                    return False
                    
                wordmap[pattern[i]] = s[i]
                str_set.add(s[i])

            print(wordmap.items())

        return True

        # Time Complexity: O(n) where n is the length of pattern
        # Space Complexity: O(n) where n is the length of patterns 
