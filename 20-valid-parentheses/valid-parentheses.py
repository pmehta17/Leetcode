class Solution:
    def isValid(self, s: str) -> bool:

        # Questions
        # Are all characters in this string going to some type of bracket? We can assume there are no letters, numbers, etc?
        # Are the three brackets in the example all types of brackets I can expect?
        # How do nested brackets work here?

        if len(s) % 2 == 1:
            return False

        stack = []

        closeToOpen = {
            ")" : "(", 
            ']' : '[', 
            '}' : "{"
        }

        for c in s: 
            # Check if closing bracket
            if c in closeToOpen:
                if len(stack) > 0 and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False

            # Open bracket
            else:
                stack.append(c)

        
        return len(stack) == 0

        #Time Complexity: O(n) where n is length of string
        # Space complexity: Worst case O(n) bc we could have to add every element to the stack (assuming there are no closing brackets)