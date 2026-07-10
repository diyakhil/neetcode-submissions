class MinStack:

    def __init__(self):
        self.stack = []
        self.minValue = float('inf')
        
    def push(self, val: int) -> None:
        if (not self.stack) or (self.stack and val < self.stack[-1][1]):
            self.stack.append([val, val])
            self.minValue = val
        else:
            self.stack.append([val, self.minValue])
        

    def pop(self) -> None:
        self.stack.pop()
        #need to update minValue here to the last element's minValue or reset it to infinity if stack is empty
        if self.stack:
            self.minValue = self.stack[-1][1]
        else:
            self.minValue = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
