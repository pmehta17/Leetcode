from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Hashmap; Key = count of each character, value = list of words

        wordmap = defaultdict(list)        

        for word in strs:
            char_freq = [0]*26
            for c in word.lower():
                char_freq[ord(c) - ord("a")] += 1
            wordmap[tuple(char_freq)].append(word)
            # char_str = ''.join(str(x) for x in char_freq)
            # wordmap[char_str] += word
            # print(word)
            # print(wordmap.items())

        return wordmap.values()