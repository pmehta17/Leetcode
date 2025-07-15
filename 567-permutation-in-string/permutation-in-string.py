class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        l = 0
        r = l + len(s1) - 1
        s1_char_map = Counter(s1)

        while r <= len(s2):

            s2_char_map = Counter(s2[int(l): int(r)+1])

            if s1_char_map == s2_char_map:
                return True
        
            l += 1 
            r += 1

        return False



