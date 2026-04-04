class MinStack:
    # initialize the stack object
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    # Push val onto the stack
    def push(self, val: int) -> None:
        if not self.stack:
            self.min_stack.append(val)
        
        self.stack.append(val)
        current_min = self.min_stack[-1]
        self.min_stack.append(min(current_min, val))

    # Remove the top element of the stack
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    # Get the top element of the stack
    def top(self) -> int:
        return self.stack[-1]
        

    # Retrieve the minimum element in the stack
    def getMin(self) -> int:
        return self.min_stack[-1]
