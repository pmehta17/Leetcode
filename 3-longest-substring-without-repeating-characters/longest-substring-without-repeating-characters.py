class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0 or len(s) == 1:
            return len(s)

        ans = 0

        l = 0
        r = 1

        while r < len(s):
            letter_set = set()
            letter_set.add(s[l])
            temp_str = ""
            print(r)
            while r < len(s) and s[r] not in letter_set:
                letter_set.add(s[r])
                r += 1
                print(r)
            temp_str = s[l:r]
            print(temp_str)

            if len(temp_str) > ans:
                ans = len(temp_str)
            
            l += 1
            r = l + 1
            
        return ans
