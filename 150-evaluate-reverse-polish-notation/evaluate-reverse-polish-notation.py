class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Questions
        # 1. Input validation: Are we only going to have numbers and the four valid operators?
        # 2. What if we only have 2 numbers? or only 1 operator? (Edge case)
        # 3. Divide by zero?
        stack = []

        for val in tokens:

            if val == "+":
                stack.append((stack.pop()) + stack.pop())
            elif val == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif val == "*":
                stack.append(stack.pop() * stack.pop())

            elif val == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(val))

        return stack[0]
