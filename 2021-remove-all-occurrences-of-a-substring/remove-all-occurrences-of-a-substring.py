class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:


        l = 0
        r = 1

        while part in s:
            idx = s.index(part)
            s = s[:idx] + s[idx + len(part):]

        return s

