class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = ("+", "-", "*", "/")

        stack = []

        for val in tokens: 
            if val in ops: 
                num_two = int(stack.pop())
                num_one = int(stack.pop())
                stack.append(self.solve(num_one, num_two, val))
            else: 
                stack.append(int(val))


        return stack[0]



    def solve(self, num_one, num_two, op):
        if op == "+":
            return num_one + num_two
        elif op == "-":
            return num_one - num_two
        elif op == "*":
            return num_one * num_two
        elif op == "/":
            return int(num_one / num_two)
        
        