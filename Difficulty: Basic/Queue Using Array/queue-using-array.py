class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.list = []
        self.n = n

    
    def isEmpty(self):
        # Check if queue is empty
        if len(self.list) == 0:
            return True
        return False
    
    def isFull(self):
        # Check if queue is full
        if len(self.list) == self.n:
            return True
        return False
    
    def enqueue(self, x):
        # Enqueue
        if not self.isFull():
            self.list.append(x)
            return
    
    def dequeue(self):
        if not self.isEmpty():
            del self.list[0]
        return
        # Dequeue

    
    def getFront(self):
        # Get front element
        if not self.isEmpty():
            return self.list[0]
        else:
            return -1
       
    
    def getRear(self):
        # Get rear element 
        if not self.isEmpty():
            return self.list[-1]
        else:
            return -1
        
        