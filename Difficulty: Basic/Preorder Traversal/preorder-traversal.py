'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def preOrder(self, root):
    # code here
        stack = []
        answer = []
        
        if root is not None:
            stack.append(root)
            
        while (len(stack) > 0):
            temp = stack.pop()
            
            answer.append(temp.data)
            if temp.right is not None:
                stack.append(temp.right)
                
            if temp.left is not None:
                stack.append(temp.left)
        
        return answer
        