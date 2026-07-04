class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.list = []
        self.n = n

    
    def isEmpty(self):
        # Check if stack is empty
        if not self.list:
            return True
        return False
        
    def isFull(self):
        # Check if stack is full
        if len(self.list) == self.n:
            return True
        return False
    
    def push(self, x):
        # Insert x at the top of the stack
        if not self.isFull():
            self.list.append(x)
        return
    
    def pop(self):
        # Removes an element from the top of the stack
        if not self.isEmpty():
            self.list.pop()
        return
    
    def peek(self):
        # Returns the top element of the stack
        if not self.isEmpty():
            return self.list[-1]
            
        return -1