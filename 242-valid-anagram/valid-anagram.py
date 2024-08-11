class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        return collections.Counter(s) == collections.Counter(t)

        # if len(s) != len(t):
        #     return False

        # s_map = {}
        # t_map = {}

        # for c in s:
        #     if c in s_map:
        #         s_map[c] += 1
        #     else:
        #         s_map[c] = 1

        # for ch in t:
        #     if ch in t_map:
        #         t_map[ch] += 1
        #     else:
        #         t_map[ch] = 1

        # return s_map == t_map	





