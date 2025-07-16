
class MinStack:

    def __init__(self):

        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:

        self.stack.append(val)

        if len(self.minStack) == 0:
            self.minStack.append(val)
        else: 
            temp_min = min(val, self.minStack[-1])
            self.minStack.append(temp_min)
        

    def pop(self) -> None:


        self.stack.pop()
        self.minStack.pop()

        

    def top(self) -> int:

        return self.stack[-1]

        # not modifying the list, dont need to work with minStack
        

    def getMin(self) -> int:

        return self.minStack[-1]
        

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()