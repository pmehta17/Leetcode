class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:
            return False 

        stack = []

        bracket_mapping = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s: 
            # close bracket 
            if c in bracket_mapping: 
                if len(stack) < 1 or stack[-1] != bracket_mapping[c]:
                    return False # unmatched bracket
                stack.pop(-1)

            # open bracket 
            else:
                stack.append(c)
                


        return len(stack) == 0

        